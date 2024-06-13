import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import random
from partywise import detail_page
st.set_page_config(layout="wide",page_title='Election Results')
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
        second_data = pd.read_csv('some_election_data.csv')
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
    "Total":"transparent"
    }
        fig = px.pie(first_data, values=first_data['Won'], names=first_data['Party'], title='Votes Distribution by State',color='Party', color_discrete_map=color_discrete_map)
        fig.update_traces(hole=0.6, hoverinfo="label+name", sort=False)
        fig.update_layout(height=700, width=800)
        fig.update_traces(rotation=90)
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
        def create_clickable_link(party, won):
            return f'<a href="?party={party}" target="_blank">{won}</a>'
        st.subheader('Party Wise Results Status')
        second_data['Won'] = second_data.apply(lambda row: create_clickable_link(row['Party'], row['Won']), axis=1)
        st.markdown(second_data.to_html(escape=False, index=False), unsafe_allow_html=True)
        if second_data:
            detail_page()
        

    
elif tab == 'Assembly Constituency General':
    st.subheader('General Election to Assembly Constituencies: Trends & Results June-2024', divider='rainbow')

    andh = ['TDP', 'JnP', 'YSRCP', 'BJP']
    wandh = [135, 21, 11, 8]

    odi = ['BJP', 'BJD', 'INC', 'IND', 'CPI(M)']
    wodi = [78, 51, 14, 1, 3]

    col8, col9 = st.columns([2, 2])
    with col8:
        st.markdown(f"""
        <div style="background-color: teal; border: solid 2px teal; border-radius: 10px; overflow: hidden; max-width: 600px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="background-color: white; color: teal;font-size:18.4px;font-weight:500; text-align: center; padding: 10px; border-bottom: solid 2px teal;">
            Andhra Pradesh
        </div>
        <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
            <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituency</p>
            <p style="background-color: grey; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">175</p>
        </div>
            <p style="font-size:12px;color:white;padding-left:15px">  Status of Top Five Parties</p>
        <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;">
            <table style="width: 80%;color:black;border-collapse: collapse;">
                <tr style="text-align: left; padding: 8px; background-color: teal; color: white;">
                    <th style="text-align: left; padding: 12px;">Parties</th>
                    <th style="text-align: left; padding: 12px;">Leading/Won</th>
                </tr>
                <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andh[0]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandh[0]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andh[1]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandh[1]}</td>
                </tr>
                <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andh[2]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandh[2]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andh[3]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandh[3]}</td>
                </tr>
            </table>
        </div>
        <div style="text-align:center; margin-top:20px;margin-bottom:20px;">
    <button  style="background-color:white;border-radius:15px; color: black; padding: 10px 20px; border: solid black;">Details ></button>
</div>
    </div>
    """, unsafe_allow_html=True)
    with col9:
        st.markdown(f"""
            <div style="background-color: maroon; border: solid 2px maroon; border-radius: 10px; overflow: hidden; max-width: 600px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <div style="background-color: white;font-size:18.4px;font-weight:500 ;color: maroon; text-align: center; padding: 10px; border-bottom: solid 2px maroon;">
            Odisha
            </div>
            <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
            <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituency</p>
            <p style="background-color: grey; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">147</p>
            </div>
            <p style="font-size:12px;color:white;padding-left:15px">  Status of Top Five Parties</p>
            <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;">
                <table style="width: 100%;color:black;border-collapse: collapse;">
                    <tr style="text-align: left; padding: 8px; background-color: maroon; color: white;">
                    <th style="text-align: left; padding: 12px;">Parties</th>
                    <th style="text-align: left; padding: 12px;">Leading/Won</th>
                    </tr>
                    <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[0]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[0]}</td>
                    </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[1]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[1]}</td>
                </tr>
                <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[2]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[2]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[3]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[3]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[4]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[4]}</td>
                </tr>
            </table>
        </div>
    <div style="text-align:center; margin-top:20px;margin-bottom:20px">
    <button style="background-color: white;border-radius:15px; color: black; padding: 10px 20px; border: solid black;">Details ></button>
    </div>
    </div>
    """, unsafe_allow_html=True)
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


