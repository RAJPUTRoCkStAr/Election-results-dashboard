import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from Acb import acb_show
from Acg import acg_show
from Stwise import stwise_show

st.set_page_config(layout="wide", page_title='Election Results')

# Get the selected party and state from query parameters
query_params = st.experimental_get_query_params()
selected_party = query_params.get("party", [None])[0]
selected_state = query_params.get("state", [None])[0]


# Display results for the selected party
if selected_party:
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        st.empty()
    with col2:
        st.header("General Election to Parliamentary Constituencies: Trends & Results June-2024")
        st.header(f":blue[Winning Candidate ({selected_party})]", divider="green")
    with col3:
        st.empty()

    try:
        pages = pd.read_csv(f'partywise/{selected_party}.csv')
        st.dataframe(pages, use_container_width=True, hide_index=True, height=1500)
    except FileNotFoundError:
        st.error(f"No data available for {selected_party}")

# Display results for the selected state
elif selected_state:
        st.header(f"State-wise Election Results: {selected_state}")
        stwise_show(selected_state)

# Display the main menu and graphs
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
        col4, col5 = st.columns([4, 2])

        with col4:
            st.subheader('General Election to Parliamentary Constituencies: Trends & Results June-2024 :')

        with col5:
            options = [
                "Select State Wise",
                "Andaman & Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", 
                "Chandigarh", "Chhattisgarh", "Dadra & Nagar Haveli and Daman & Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", 
                "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", 
                "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "NCT OF Delhi", "Odisha", "Puducherry", 
                "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
            ]
            selected_option = st.selectbox('Select State wise', options)

            if selected_option and selected_option != "Select State Wise":
                st.experimental_set_query_params(state=selected_option)
                st.experimental_rerun()

        col6, col7, col8 = st.columns([1, 4, 1])
        
        with col6:
            st.empty()
        
        with col7:
            # Assuming gauge-chart.csv contains the necessary data
            first_data = pd.read_csv('gauge-chart.csv')
            second_data = pd.read_csv('some_election_data.csv')
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
            fig = px.pie(first_data, values='Won', names='Party', title='Votes Distribution by State', color='Party', color_discrete_map=color_discrete_map)
            fig.update_traces(hole=0.6, hoverinfo='none', hovertemplate='%{label} <br> %{value}', sort=False, textinfo='none')
            fig.update_layout(height=700, width=1200, showlegend=False)
            fig.update_layout(annotations=[dict(text='543/543', x=0.5, y=0.5, font_size=20, showarrow=False)])
            fig.update_traces(rotation=69)
            st.plotly_chart(fig)
        
        with col8:
            st.empty()

        col9, col10 = st.columns([3, 3])
        
        with col9:
            st.subheader('Party Wise Vote Share')
            fig2 = px.pie(second_data, values='Won', names='Party', color='Party')
            fig2.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none')
            fig2.update_layout(height=1200, width=800)
            fig2.update_layout(legend=dict(orientation='h', y=-1.7, yanchor='bottom', x=0.5, xanchor='center'))
            st.plotly_chart(fig2)

        with col10:
            st.subheader('Party Wise Results Status')
            st.dataframe(second_data)
            
    elif tab == 'Assembly Constituency General':
        acg_show()
    elif tab == 'Assembly Constituency Bye':
        acb_show()
