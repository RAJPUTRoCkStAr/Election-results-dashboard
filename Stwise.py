import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
def ac_lss(selected_option,da):
    da['votes'] = pd.to_numeric(da['votes'], errors='coerce')
    states = da['state'].unique()
    if selected_option in states:
        st.subheader('General Election to Parliamentary Constituencies: Trends & Results June-2024')
        col1,col2,col3 = st.columns([2,3,2])
        with col1:
            st.empty()
        with col2:
            st.subheader(f":blue[{selected_option}]",divider="green")
        with col3:
            st.empty()    

        df_state = da[da['state'] == selected_option]
        constituencies = sorted(df_state['constituency'].unique())
        constituency_details = []
        for constituency in constituencies:
            df_constituency = df_state[df_state['constituency'] == constituency]
            df_constituency = df_constituency.sort_values(by='votes', ascending=False)
            image = df_constituency.iloc[0]['img_link']
            leading_candidate = df_constituency.iloc[0]['name']
            leading_party = df_constituency.iloc[0]['party_name']
            trailing_candidate = df_constituency.iloc[-1]['name']
            timage = df_constituency.iloc[-1]['img_link']
            trailing_party = df_constituency.iloc[-1]['party_name']
            margin = df_constituency.iloc[0]['votes'] - df_constituency.iloc[1]['votes']
            status = 'Result Declared'
            constituency_details.append({
                'Constituency': constituency,
                'Image Preview':image,
                'Leading Candidate': leading_candidate,
                'Leading Party': leading_party,
                'Trailing Candidate': trailing_candidate,
                'Image Previ': timage,
                'Trailing Party': trailing_party,
                'Margin': margin,
                'Status': status
            })
        constituency_details_df = pd.DataFrame(constituency_details)
        st.data_editor(constituency_details_df,column_config={
           "Image Preview": st.column_config.ImageColumn("Preview Image"),
        "Image Previ": st.column_config.ImageColumn("Preview Image"),
    },hide_index=True,use_container_width=True,width=800,column_order=['Constituency','Leading Party','Leading Candidate','Image Preview','Trailing Candidate','Image Previ','Margin'])
    else:
        st.write("State not found in the data.")    

def stwise_show(selected_option):
    da = pd.read_csv('data/electiondata.csv')
    won_data = da[da['won_status'] == 'won']
    won_data_sorted = won_data.sort_values(by='state')
    party_info = {
    "Bharatiya Janata Party": {"color": "#ff8331", "short_name": "BJP"},
    "Indian National Congress": {"color": "#17aaed", "short_name": "INC"},
    "Samajwadi Party": {"color": "#ff0000", "short_name": "SP"},
    "All India Trinamool Congress": {"color": "#aebedf", "short_name": "AITC"},
    "Dravida Munnetra Kazhagam": {"color": "#05f89e", "short_name": "DMK"},
    "Telugu Desam": {"color": "#204795", "short_name": "TDP"},
    "Janata Dal  (United)": {"color": "#39ac57", "short_name": "JD(U)"},
    "Shiv Sena (Uddhav Balasaheb Thackrey)": {"color": "#61da8c", "short_name": "SHSUBT"},
    "Nationalist Congress Party - Sharadchandra Pawar": {"color": "#457a8b", "short_name": "NCPSP"},
    "Shiv Sena": {"color": "#d2691e", "short_name": "Shiv Sena"},
    "Lok Janshakti Party(Ram Vilas)": {"color": "#8a2be2", "short_name": "LJPRV"},
    "Yuvajana Sramika Rythu Congress Party": {"color": "#ff7f50", "short_name": "YSRCP"},
    "Rashtriya Janata Dal": {"color": "#228b22", "short_name": "RJD"},
    "Communist Party of India  (Marxist-Leninist)  (Liberation)": {"color": "#ff1493", "short_name": "CPI(M)"},
    "Indian Union Muslim League": {"color": "#ff6347", "short_name": "IUML"},
    "Aam Aadmi Party": {"color": "#008080", "short_name": "AAP"},
    "Jharkhand Mukti Morcha":{"color": "#008080", "short_name": "JMM"},
    "Janasena Party": {"color": "#ff69b4", "short_name": "JnP"},
    "Janata Dal  (Secular)": {"color": "#32cd32", "short_name": "JD(S)"},
    "Viduthalai Chiruthaigal Katchi": {"color": "#ffff00", "short_name": "VCK"},
    "Communist Party of India  (Marxist)": {"color": "#9400d3", "short_name": "CPI"},
    "Rashtriya Lok Dal": {"color": "#ff4500", "short_name": "RLD"},
    "Jammu & Kashmir National Conference": {"color": "#ff8c00", "short_name": "JKN"},
    "United People’s Party, Liberal": {"color": "#40e0d0", "short_name": "UPPL"},
    "Asom Gana Parishad": {"color": "#00fa9a", "short_name": "AGP"},
    "Hindustani Awam Morcha (Secular)": {"color": "#800000", "short_name": "HAMS"},
    "Kerala Congress": {"color": "#ffdead", "short_name": "KEC"},
    "Revolutionary Socialist Party": {"color": "#00ff00", "short_name": "RSP"},
    "Nationalist Congress Party": {"color": "#800080", "short_name": "NCP"},
    "Voice of the People Party": {"color": "#add8e6", "short_name": "VOTPP"},
    "Zoram People's Movement": {"color": "#ff00ff", "short_name": "ZPM"},
    "Shiromani Akali Dal": {"color": "#ff0000", "short_name": "SAD"},
    "Rashtriya Loktantrik Party": {"color": "#8b4513", "short_name": "RLTP"},
    "Bharat Adivasi Party": {"color": "#000080", "short_name": "BHRTADVSIP"},
    "Sikkim Krantikari Morcha": {"color": "#4b0082", "short_name": "SKM"},
    "Marumalarchi Dravida Munnetra Kazhagam": {"color": "#f08080", "short_name": "MDMK"},
    "Aazad Samaj Party (Kanshi Ram)": {"color": "#2e8b57", "short_name": "ASPKR"},
    "Apna Dal (Soneylal)": {"color": "#4682b4", "short_name": "ADAL"},
    "AJSU Party": {"color": "#00ced1", "short_name": "AJSUP"},
    "All India Majlis-E-Ittehadul Muslimeen": {"color": "#8b0000", "short_name": "AIMIM"},
    "Independent": {"color": "#20b2aa", "short_name": "IND"}
    }
    def get_winners_by_state(state_name):
        state_winners = won_data_sorted[won_data_sorted['state'] == state_name]
        return state_winners[['won_status', 'party_name']]
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
    col3, col4 = st.columns([2, 2])
    with col3:
        st.dataframe(party_counted,hide_index=True,use_container_width=True)
    with col4:
        st.subheader(":red-background[Party Wise Results by Constituency]")
        def get_winners_by_state(state_name):
            state_winners = won_data_sorted[won_data_sorted['state'] == state_name]
            return state_winners[['constituency', 'party_name']]
        state_winners_data = get_winners_by_state(selected_option)
        party_counts = state_winners_data.groupby(['party_name', 'constituency']).size().reset_index(name='won_count')
        for party, group in party_counts.groupby('party_name'):
            party_info_entry = party_info.get(party, {"color": "transparent", "short_name": party})
            color = party_info_entry["color"]
            short_name = party_info_entry["short_name"]
        party_coun = pd.DataFrame(party_counts)
        fig = px.bar(party_coun, x='party_name', y='won_count', color='constituency', 
             labels={'won_count': 'Won Count', 'constituency': 'Constituency'},
             color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(barmode='group', yaxis_title='Won Count',showlegend=False)
        st.plotly_chart(fig)
    col7,col8 = st.columns([2,2])
    with col7:
        st.subheader(':red-background[Party Wise Vote Share]')
        state_data = da[da['state'] == selected_option]
        result_df = state_data[['constituency', 'party_name', 'votes']]
        result_df = result_df.drop_duplicates()
        fig3 = px.pie(result_df, values='votes', names='party_name', color='party_name')
        fig3.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none',showlegend=False)
        fig3.update_layout(height=500, width=700)
        st.plotly_chart(fig3)
    with col8:
        st.subheader(":red-background[Party Wise Results]")
        fig4 = px.pie(party_counted, values='won', names='party', color='party')
        fig4.update_traces(hole=0.4, sort=False, hoverinfo='label', textinfo='none',showlegend=False)
        fig4.update_layout(height=500, width=700)
        st.plotly_chart(fig4)

    ac_button = st.button('All Constituencies at a glance',use_container_width=True,type="primary")
    if ac_button:
        ac_lss(selected_option,da)
warnings.resetwarnings()