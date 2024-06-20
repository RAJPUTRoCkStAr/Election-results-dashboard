import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from Acb import acb_show
from Acg import acg_show
from Stwise import stwise_show

st.set_page_config(layout="wide", page_title='Election Results')

query_params = st.experimental_get_query_params()
selected_party = query_params.get("party", [None])[0]
selected_state = query_params.get("state", [None])[0]
selected_constituency = query_params.get("constituency", [None])[0]


if selected_constituency:
    try:
        pages = pd.read_csv('data/electiondata.csv')
        constituency = pages[pages['constituency'] == selected_constituency]
        selected_state = constituency['state'].iloc[0] if not constituency.empty else "Unknown State"
        st.subheader("General Election to Parliamentary Constituencies: Trends & Results June-2024")
        col1,col2,col3 = st.columns([2,2,2])
        with col1:
            st.empty()
        with col2:
            st.subheader("Parliamentary Constituency -")
            st.subheader(f":blue[{selected_constituency} ({selected_state})]",divider="green")
        with col3:
            st.empty()
        if not constituency.empty:
            num_constituencies = len(constituency)
            columns = st.columns(min(5, num_constituencies))
            for index, row in constituency.iterrows():
                textcolor = "lightgreen" if row['won_status'] == 'won' else "red"
                with columns[index % 5]:
                    st.markdown(
                        f"""
                        <div class="card" style="background-color: transparent; border-radius: 10px; padding: 15px; margin: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border: 2px solid {textcolor}; transition: transform 0.3s; text-align: center;">
                            <img src="{row['img_link']}" style="width: 200px; height: 200px; border-radius: 50%; border: 3px solid {textcolor}; margin-bottom: 10px;">
                            <p style="color: {textcolor}; font-weight: 600; text-transform: capitalize;">{row['won_status']}</p>
                            <p style="color: {textcolor};">{row["votes"]}</p>
                            <p style="font-size: 17.6px; font-weight: 600; color: purple;">{row["name"]}</p>
                            <p style="color: lightblue; font-weight: 500; font-size: 16px;">{row["party_name"]}</p>
                        </div>
                        """, unsafe_allow_html=True
                    )
    except FileNotFoundError:
        st.error(f"No data available for {selected_constituency}")
elif selected_party:
    col4, col5, col6 = st.columns([1, 4, 1])
    with col4:
        st.empty()
    with col5:
        st.header("General Election to Parliamentary Constituencies: Trends & Results June-2024")
        st.header(f":blue[Winning Candidate ({selected_party})]", divider="green")
    with col6:
        st.empty()
        with col5:
            try:
                pages = pd.read_csv(f'data/partywise/{selected_party}.csv')

                def create_clickable_party(constituency):
                    return f'<a href="?constituency={constituency}" target="_blank">{constituency}</a>'

                pages['Parliament Constituency'] = pages.apply(lambda row: create_clickable_party(row['Parliament Constituency']), axis=1)
                st.markdown(pages.to_html(na_rep='None',escape=False, index=False,justify="center",col_space = 55), unsafe_allow_html=True)
        
            except FileNotFoundError:
                st.error(f"No data available for {selected_party}")

elif selected_state:
    st.header("General Election to Parliamentary Constituencies: Trends & Results June-2024")
    col7, col8, col9 = st.columns([3, 3, 2])
    with col7:
        st.empty()
    with col8:
        st.header(f":blue[{selected_state}]", divider="green")
    with col9:
        st.empty()
    stwise_show(selected_state)
else:
    tab = option_menu(
        None,
        ["Parliament Constituency General", "Assembly Constituency General", "Assembly Constituency Bye"],
        orientation="horizontal",
        styles={
            "container": {"padding": "10!important", "background-color": "red"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "color": "white", "background-color": "red"},
            "nav-link-selected": {"background-color": "darkred"},
        }
    )
    if tab == 'Parliament Constituency General':
        col10, col11 = st.columns([4, 2])

        with col10:
            st.subheader('General Election to Parliamentary Constituencies: Trends & Results June-2024 :')

        with col11:
            options = [
                "Select State Wise",
                "Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
                "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman and Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
                "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh",
                "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "NCT OF Delhi", "Odisha", "Puducherry",
                "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
            ]
            selected_option = st.selectbox('Select State wise', options)

            if selected_option and selected_option != "Select State Wise":
                st.experimental_set_query_params(state=selected_option)
                st.experimental_rerun()

        col12, col13, col14 = st.columns([1, 4, 1])

        with col12:
            st.empty()

        with col13:
            first_data = pd.read_csv('data/gauge-chart.csv')
            second_data = pd.read_csv('data/some_election_data.csv')
            color_discrete_map = {
                "Bharatiya Janata Party - BJP": "#ff8331",
                "Indian National Congress - INC": "#17aaed",
                "Samajwadi Party - SP": "#ff0000",
                "All India Trinamool Congress - AITC": "#aebedf",
                "Dravida Munnetra Kazhagam - DMK": "#05f89e",
                "Telugu Desam - TDP": "#204795",
                "Janata Dal (United) - JD(U)": "#39ac57",
                "Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT": "#61da8c",
                "Nationalist Congress Party - Sharadchandra Pawar - NCPSP": "#457a8b",
                "Shiv Sena ": "#d2691e",
                "Others": "#b3b3b3",
                "Total": "transparent"
            }
            fig = px.pie(first_data, values='Won', names='Party', color='Party', color_discrete_map=color_discrete_map)
            fig.update_traces(hole=0.6, hoverinfo='none', hovertemplate='%{label} <br> %{value}', sort=False, textinfo='none')
            fig.update_layout(height=700, width=1200, showlegend=False)
            fig.update_layout(annotations=[dict(text='543/543', x=0.5, y=0.5, font_size=20, showarrow=False)])
            fig.update_traces(rotation=69)
            st.plotly_chart(fig)

        with col14:
            st.empty()

        col15, col16 = st.columns([3, 3])

        with col15:
            st.subheader(':red-background[Party Wise Vote Share]')
            fig2 = px.pie(second_data, values='Won', names='Party', color='Party')
            fig2.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none')
            fig2.update_layout(height=1200, width=800)
            fig2.update_layout(legend=dict(orientation='h', y=-1.7, yanchor='bottom', x=0.5, xanchor='center'))
            st.plotly_chart(fig2)

        with col16:
            def create_clickable_link(party, won):
                return f'<a href="?party={party}" target="_blank">{won}</a>'
            st.subheader(':red-background[Party Wise Results Status]')
            second_data['Won'] = second_data.apply(lambda row: create_clickable_link(row['Party'], row['Won']), axis=1)
            st.markdown(second_data.to_html(escape=False, index=False,justify="center"), unsafe_allow_html=True)

    elif tab == 'Assembly Constituency General':
        acg_show()

    elif tab == 'Assembly Constituency Bye':
        acb_show()
