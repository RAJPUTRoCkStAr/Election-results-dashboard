import streamlit as st
import pandas as pd
import plotly.express as px

def ad_lss(selected_option, data):
    data['votes'] = pd.to_numeric(data['votes'], errors='coerce')
    states = data['state'].unique()
    if selected_option in states:
        st.subheader('General Election to Parliamentary Constituencies: Trends & Results June-2024')
        col1, col2, col3 = st.columns([2, 3, 2])
        with col1:
            st.empty()
        with col2:
            st.subheader(f":blue[{selected_option}]", divider="red")
        with col3:
            st.empty()
        df_state = data[data['state'] == selected_option]
        constituencies = sorted(df_state['constituency'].unique())
        constituency_details = []
        for constituency in constituencies:
            df_constituency = df_state[df_state['constituency'] == constituency]
            df_constituency = df_constituency.sort_values(by='votes', ascending=False)
            leading_candidate = df_constituency.iloc[0]['name']
            leading_party = df_constituency.iloc[0]['party_name']
            trailing_candidate = df_constituency.iloc[-1]['name']
            trailing_party = df_constituency.iloc[-1]['party_name']
            margin = df_constituency.iloc[0]['votes'] - df_constituency.iloc[1]['votes']
            status = 'Result Declared'
            constituency_details.append({
                'Constituency': constituency,
                'Leading Candidate': leading_candidate,
                'Leading Party': leading_party,
                'Trailing Candidate': trailing_candidate,
                'Trailing Party': trailing_party,
                'Margin': margin,
                'Status': status
            })
        constituency_details_df = pd.DataFrame(constituency_details)
        st.dataframe(constituency_details_df, hide_index=True, use_container_width=True)
    else:
        st.write("State not found in the data.")

def ac_lss(selected_option, data):
    data['votes'] = pd.to_numeric(data['votes'], errors='coerce')
    states = data['state'].unique()
    if selected_option in states:
        st.subheader('General Election to Parliamentary Constituencies: Trends & Results June-2024')
        col1, col2, col3 = st.columns([2, 3, 2])
        with col1:
            st.empty()
        with col2:
            st.subheader(f":red[{selected_option}]", divider="blue")
        with col3:
            st.empty()
        df_state = data[data['state'] == selected_option]
        constituencies = sorted(df_state['constituency'].unique())
        constituency_details = []
        for constituency in constituencies:
            df_constituency = df_state[df_state['constituency'] == constituency]
            df_constituency = df_constituency.sort_values(by='votes', ascending=False)
            leading_candidate = df_constituency.iloc[0]['name']
            leading_party = df_constituency.iloc[0]['party_name']
            trailing_candidate = df_constituency.iloc[-1]['name']
            trailing_party = df_constituency.iloc[-1]['party_name']
            margin = df_constituency.iloc[0]['votes'] - df_constituency.iloc[1]['votes']
            status = 'Result Declared'
            constituency_details.append({
                'Constituency': constituency,
                'Leading Candidate': leading_candidate,
                'Leading Party': leading_party,
                'Trailing Candidate': trailing_candidate,
                'Trailing Party': trailing_party,
                'Margin': margin,
                'Status': status
            })
        constituency_details_df = pd.DataFrame(constituency_details)
        st.dataframe(constituency_details_df, hide_index=True, use_container_width=True)
    else:
        st.write("State not found in the data.")

def andhra_show():
    query_params = st.experimental_get_query_params()
    selected_party = query_params.get("party", [None])[0]
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
                    textcolor = "green" if row['won_status'] == 'won' else "red"
                    with columns[index % 5]:
                        st.markdown(
                        f"""
                        <div class="card" style="background-color: #f5f5f5; border-radius: 10px; padding: 15px; margin: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border: 2px solid {textcolor}; transition: transform 0.3s; text-align: center;">
                            <img src="{row['img_link']}" style="width: 200px; height: 200px; border-radius: 50%; border: 3px solid {textcolor}; margin-bottom: 10px;">
                            <p style="color: {textcolor}; font-weight: 600; text-transform: capitalize;">{row['won_status']}</p>
                            <p style="color: {textcolor};">{row["votes"]}</p>
                            <p style="font-size: 17.6px; font-weight: 600; color: #094DE0;">{row["name"]}</p>
                            <p style="color: blue; font-weight: 500; font-size: 16px;">{row["party_name"]}</p>
                        </div>
                        """, unsafe_allow_html=True
                    )
        except FileNotFoundError:
            st.error(f"No data available for {selected_constituency}")
    if selected_party:
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
    st.subheader(f':blue[Andhra Pradesh Election Results]',divider="red")
    data = pd.read_csv('data/secpageda.csv')
    won_data = data[data['won_status'] == 'won']
    stat_data = won_data[won_data['state'] == 'Andhra Pradesh']
    parties_colors = [
        {"name": "Independent", "short_name": "IND", "color": "#808080"},
        {"name": "Communist Party of India  (Marxist)", "short_name": "CPI(M)", "color": "#FF0000"},
        {"name": "Indian National Congress", "short_name": "INC", "color": "#00A2E8"},
        {"name": "Biju Janata Dal", "short_name": "BJD", "color": "#008000"},
        {"name": "Bharatiya Janata Party", "short_name": "BJP", "color": "#FF9933"},
        {"name": "Yuvajana Sramika Rythu Congress Party", "short_name": "YSRCP", "color": "#00BFFF"},
        {"name": "Janasena Party", "short_name": "JSP", "color": "#FF4500"},
        {"name": "Telugu Desam", "short_name": "TDP", "color": "#FFD700"},
    ]
    party_info = {party["name"]: {"short_name": party["short_name"], "color": party["color"]} for party in parties_colors}

    def get_winners_by_state(state_name):
        state_winners = won_data[won_data['state'] == state_name]
        return state_winners[['won_status', 'party_name']]

    selected_option = 'Andhra Pradesh'
    state_winners_data = get_winners_by_state(selected_option)
    party_counts = state_winners_data['party_name'].value_counts()

    cols = st.columns(len(party_counts))
    st.subheader(":red-background[Party Wise Results]")
    for col, (party, count) in zip(cols, party_counts.items()):
        party_info_entry = party_info.get(party, {"color": "transparent", "short_name": party})
        color = party_info_entry["color"]
        short_name = party_info_entry["short_name"]
        with col:
            st.markdown(f"""
            <div style="background-color:{color}; text-align:center; border: 1px solid black; margin: 5px; padding: 10px;">
                <p><strong>{short_name}</strong></p>
                <p>{count}</p>
            </div>
            """, unsafe_allow_html=True)
    
    party_counted = pd.DataFrame({
        'party': party_counts.index,
        'won': party_counts.values,
        'leading': [0] * len(party_counts),
        'total': party_counts.values
    })

    col1, col2 = st.columns([2, 2])
    with col1:
        def create_clickable_link(party_name, won):
            return f'<a href="?party={party_name}" target="_blank">{won}</a>'
        st.subheader(':red-background[Party Wise Results Status]')
        party_counted['won'] = party_counted.apply(lambda row: create_clickable_link(row['party'], row['won']), axis=1)
        st.markdown(party_counted.to_html(escape=False, index=False,justify="center"), unsafe_allow_html=True)
    with col2:
        col3, col4 = st.columns([2, 3])
        with col3:
            st.subheader(f':red-background[Constituency Wise Results]')
        with col4:
            st.write('I am coming soon')

    col5, col6 = st.columns([2, 2])
    with col5:
        st.subheader(':red-background[Party Wise Vote Share]')
        state_data = data[data['state'] == selected_option]
        result_df = state_data[['constituency', 'party_name', 'votes']].drop_duplicates()
        fig = px.pie(result_df, values='votes', names='party_name', color='party_name',
                     color_discrete_map={party["name"]: party["color"] for party in parties_colors})
        fig.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none', showlegend=False)
        fig.update_layout(height=500, width=700)
        st.plotly_chart(fig)

    with col6:
        st.subheader(":red-background[Party Wise Results]")
        fig1 = px.pie(party_counted, values='won', names='party', color='party',
                      color_discrete_map={party["name"]: party["color"] for party in parties_colors})
        fig1.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none', showlegend=False)
        fig1.update_layout(height=500, width=700)
        st.plotly_chart(fig1)

    ad_button = st.button('All Constituencies at a glance', use_container_width=True, type="primary")
    if ad_button:
        ad_lss('Andhra Pradesh', data)


def odisha_show():
    query_params = st.experimental_get_query_params()
    selected_party = query_params.get("party", [None])[0]
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
                    textcolor = "green" if row['won_status'] == 'won' else "red"
                    with columns[index % 5]:
                        st.markdown(
                        f"""
                        <div class="card" style="background-color: #f5f5f5; border-radius: 10px; padding: 15px; margin: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border: 2px solid {textcolor}; transition: transform 0.3s; text-align: center;">
                            <img src="{row['img_link']}" style="width: 200px; height: 200px; border-radius: 50%; border: 3px solid {textcolor}; margin-bottom: 10px;">
                            <p style="color: {textcolor}; font-weight: 600; text-transform: capitalize;">{row['won_status']}</p>
                            <p style="color: {textcolor};">{row["votes"]}</p>
                            <p style="font-size: 17.6px; font-weight: 600; color: #094DE0;">{row["name"]}</p>
                            <p style="color: blue; font-weight: 500; font-size: 16px;">{row["party_name"]}</p>
                        </div>
                        """, unsafe_allow_html=True
                    )
        except FileNotFoundError:
            st.error(f"No data available for {selected_constituency}")
    if selected_party:
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
    st.subheader(f':red[Odisha Election Results]',divider="blue")
    data = pd.read_csv('data/secpageda.csv')
    won_data = data[data['won_status'] == 'won']
    stat_data = won_data[won_data['state'] == 'Odisha']
    parties_colors = [
        {"name": "Independent", "short_name": "IND", "color": "#808080"},
        {"name": "Communist Party of India  (Marxist)", "short_name": "CPI(M)", "color": "#FF0000"},
        {"name": "Indian National Congress", "short_name": "INC", "color": "#00A2E8"},
        {"name": "Biju Janata Dal", "short_name": "BJD", "color": "#008000"},
        {"name": "Bharatiya Janata Party", "short_name": "BJP", "color": "#FF9933"},
        {"name": "Yuvajana Sramika Rythu Congress Party", "short_name": "YSRCP", "color": "#00BFFF"},
        {"name": "Janasena Party", "short_name": "JSP", "color": "#FF4500"},
        {"name": "Telugu Desam", "short_name": "TDP", "color": "#FFD700"},
    ]
    party_info = {party["name"]: {"short_name": party["short_name"], "color": party["color"]} for party in parties_colors}

    def get_winners_by_state(state_name):
        state_winners = won_data[won_data['state'] == state_name]
        return state_winners[['won_status', 'party_name']]

    selected_option = 'Odisha'
    state_winners_data = get_winners_by_state(selected_option)
    party_counts = state_winners_data['party_name'].value_counts()

    cols = st.columns(len(party_counts))
    st.subheader(":red-background[Party Wise Results]")
    for col, (party, count) in zip(cols, party_counts.items()):
        party_info_entry = party_info.get(party, {"color": "transparent", "short_name": party})
        color = party_info_entry["color"]
        short_name = party_info_entry["short_name"]
        with col:
            st.markdown(f"""
            <div style="background-color:{color}; text-align:center; border: 1px solid black; margin: 5px; padding: 10px;">
                <p><strong>{short_name}</strong></p>
                <p>{count}</p>
            </div>
            """, unsafe_allow_html=True)
    
    party_counted = pd.DataFrame({
        'party': party_counts.index,
        'won': party_counts.values,
        'leading': [0] * len(party_counts),
        'total': party_counts.values
    })

    col7, col8 = st.columns([2, 2])
    with col7:
        def create_clickable_link(party_name, won):
            return f'<a href="?party={party_name}" target="_blank">{won}</a>'
        st.subheader(':red-background[Party Wise Results Status]')
        party_counted['won'] = party_counted.apply(lambda row: create_clickable_link(row['party'], row['won']), axis=1)
        st.markdown(party_counted.to_html(escape=False, index=False,justify="center"), unsafe_allow_html=True)
    with col8:
        col9, col10 = st.columns([2, 3])
        with col9:
            st.subheader(f':red-background[Constituency Wise Results]')
        with col10:
            st.write('I am coming soon')

    col11, col12 = st.columns([2, 2])
    with col11:
        st.subheader(':red-background[Party Wise Vote Share]')
        state_data = data[data['state'] == selected_option]
        result_df = state_data[['constituency', 'party_name', 'votes']].drop_duplicates()
        fig2 = px.pie(result_df, values='votes', names='party_name', color='party_name',
                      color_discrete_map={party["name"]: party["color"] for party in parties_colors})
        fig2.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none', showlegend=False)
        fig2.update_layout(height=500, width=700)
        st.plotly_chart(fig2)

    with col12:
        st.subheader(":red-background[Party Wise Results]")
        fig3 = px.pie(party_counted, values='won', names='party', color='party',
                      color_discrete_map={party["name"]: party["color"] for party in parties_colors})
        fig3.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none', showlegend=False)
        fig3.update_layout(height=500, width=700)
        st.plotly_chart(fig3)

    od_button = st.button('All Constituencies at a glance', use_container_width=True, type="primary")
    if od_button:
        ac_lss('Odisha', data)