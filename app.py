import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
st.write('election commission of india')
tab = option_menu(None, ["Parliament Constituency General", "Assembly Constituency General", "Assembly Constituency Bye"], orientation="horizontal", styles={
        "container": {"padding": "10!important", "background-color": "red"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "color": "white",
            "background-color": "red",
        },
        "nav-link-selected": {"background-color": "darkred"},
    }
)
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader('General Election to Parliamentary Constituencies: Trends & Results June-2024 :')

with col2:
    options = ["Select State wise", 
               "Andaman & Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh","Assam", "Bihar", 
               "Chandigarh", "Chhattisgarh", "Dadra & Nagar Haveli and Daman & Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "NCT OF Delhi", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    selected_option = st.selectbox('Select State wise', options)
col3, col4, col5 = st.columns([3, 4, 1])
with col3:
    st.empty()
with col4:
    first_data = pd.read_csv('gauge-chart.csv')
    second_data = pd.read_csv('firstpage-table.csv')
    color_discrete_map = {
    "Bharatiya Janata Party - BJP": "#ff8331",
    "Indian National Congress - INC": "#17aaed",
    "Samajwadi Party - SP": "#ff0000",
    "All India Trinamool Congress - AITC": "#aebedf",
    "Dravida Munnetra Kazhagam - DMK": "#o5f89e",
    "Telugu Desam - TDP":"#204795",
    "Janata Dal  (United) - JD(U)":"#39ac57",
    "Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT":"#61da8c",
    "Nationalist Congress Party - Sharadchandra Pawar - NCPSP":"#457a8b",
    "Shiv Sena ":"#d2691e",
    "Others":"#b3b3b3",
    "Total":"black"
}
    fig = px.pie(first_data, values=first_data['Won'], names=first_data['Party'], title='Votes Distribution by State',color='Party', color_discrete_map=color_discrete_map)
    fig.update_traces(hole=0.4, hoverinfo="label+percent+name", sort=False)
    fig.update_layout(height=700, width=800)
    st.plotly_chart(fig)
with col5:
    st.empty()


col6,col7 = st.columns([3,3])
with col6:
    st.subheader('Party Wise Vote Share')
    fig2 = px.pie(second_data, values=second_data['Won'], names=second_data['Party'],color='Party',labels=None)
    fig2.update_traces(hole=0.4, sort=False)
    fig2.update_layout(height=700, width=800)
    st.plotly_chart(fig2)

with col7:
    st.subheader('Party Wise Results Status')
    st.dataframe(second_data,use_container_width=True,height=600,hide_index=True)