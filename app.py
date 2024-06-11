import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import random
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
if tab == 'Parliament Constituency General':
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

elif tab == 'Assembly Constituency General':
    st.write('fsdfjgosdjfog')
elif tab == 'Assembly Constituency Bye':
    st.write('Disclaimer: ECI is displaying the information as being filled in the system by the Returning Officers from their respective Counting Centres. The final data for each AC/PC will be shared in Form-20.')
    st.header('Bye Election to Assembly Constituencies: Results June-2024', divider='green')

    data = pd.read_csv('last_page.csv')

# Define colors for each party
    party_colors = {
    "Bharatiya Janata Party": "blue",
    "All India Trinamool Congress": "yellow",
    "Communist Party of India  (Marxist-Leninist)  (Liberation)": "orange",
    "Indian National Congress": "pink",
    "Jharkhand Mukti Morcha":"purple",
    "Samajwadi Party":"green",
    "Bharat Adivasi Party":"orange"

}
    def random_bright_color():
        return "#{:02x}{:02x}{:02x}".format(
            random.randint(128, 255), 
            random.randint(128, 255), 
            random.randint(128, 255)
    )

    num_columns = 4
    num_rows = (len(data) + num_columns - 1) // num_columns 

    for i in range(num_rows):
        columns = st.columns(num_columns)
        for j in range(num_columns):
            index = i * num_columns + j
            if index < len(data):
                cityname, statename, result, particpantname, partyname = data.iloc[index]
                color = party_colors.get(partyname)
                participant_color = random_bright_color()
                with columns[j]:
                    st.markdown(
                    f"""
                    <div style="padding: 20px; margin: 10px;border-radius: 15px; box-shadow:  0 4px 12px rgba(0, 0, 0, 0.2); border: solid {color} 4px;">
                        <p style="color:#004274;font-size:32px;text-align:center;font-weight:700">{cityname}</p>
                        <p style="color:#0187ec;font-size:20px;text-align:center;font-weight:500">{statename}</p>
                        <p style="color:#02a560;font-size:29.6px;text-align:center;font-weight:700">{result}</p>
                        <p style="text-align:center;font-size:21.6px;font-weight:500;color:{participant_color}">{particpantname}</p>
                        <p style="color:#73aafe;font-size:16px;text-align:center;font-weight:500">{partyname}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                with columns[j]:
                    st.empty()


