import streamlit as st
import pandas as pd 
from Acgsecond import ascend_show,ascendse_show

def acg_show():
    st.subheader('General Election to Assembly Constituencies: Trends & Results June-2024')

    andh = ['TDP', 'JnP', 'YSRCP', 'BJP']
    wandh = [135, 21, 11, 8]

    odi = ['BJP', 'BJD', 'INC', 'IND', 'CPI(M)']
    wodi = [78, 51, 14, 1, 3]

    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown(f"""
            <div style="background-color: teal; border: solid 2px teal; border-radius: 10px; overflow: hidden; max-width: 600px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <div style="background-color: white; color: teal; font-size:18.4px; font-weight:500; text-align: center; padding: 10px; border-bottom: solid 2px teal;">
                Andhra Pradesh
            </div>
            <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
                <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituency</p>
                <p style="background-color: grey; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">175</p>
            </div>
                <p style="font-size:12px; color:white; padding-left:15px">Status of Top Five Parties</p>
            <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;">
                <table style="width: 80%; color:black; border-collapse: collapse;">
                    <tr style="text-align: left; padding: 8px; background-color: teal; color: white;">
                        <th style="text-align: left; padding: 12px;">Parties</th>
                        <th style="text-align: left; padding: 12px;">Leading/Won</th>
                    </tr>
                    <tr style="background-color: #f2f2f2;">
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{andh[0]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[0]}</td>
                    </tr>
                    <tr>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{andh[1]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[1]}</td>
                    </tr>
                    <tr style="background-color: #f2f2f2;">
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{andh[2]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[2]}</td>
                    </tr>
                    <tr>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{andh[3]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wandh[3]}</td>
                    </tr>
                </table>
            </div>
            </div>
        """, unsafe_allow_html=True)
        f_btn =  st.button("Details >")
        if f_btn:
            ascend_show()

    with col2:
        st.markdown(f"""
                <div style="background-color: maroon; border: solid 2px maroon; border-radius: 10px; overflow: hidden; max-width: 600px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <div style="background-color: white; font-size:18.4px; font-weight:500; color: maroon; text-align: center; padding: 10px; border-bottom: solid 2px maroon;">
                Odisha
                </div>
                <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
                <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituency</p>
                <p style="background-color: grey; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">147</p>
                </div>
                <p style="font-size:12px; color:white; padding-left:15px">Status of Top Five Parties</p>
                <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;">
                    <table style="width: 100%; color:black; border-collapse: collapse;">
                        <tr style="text-align: left; padding: 8px; background-color: maroon; color: white;">
                        <th style="text-align: left; padding: 12px;">Parties</th>
                        <th style="text-align: left; padding: 12px;">Leading/Won</th>
                        </tr>
                        <tr style="background-color: #f2f2f2;">
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{odi[0]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wodi[0]}</td>
                        </tr>
                    <tr>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{odi[1]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wodi[1]}</td>
                    </tr>
                    <tr style="background-color: #f2f2f2;">
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{odi[2]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wodi[2]}</td>
                    </tr>
                    <tr>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{odi[3]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wodi[3]}</td>
                    </tr>
                    <tr>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{odi[4]}</td>
                        <td style="text-align: left; font-size:13.6px; font-weight:600; padding: 12px;">{wodi[4]}</td>
                    </tr>
                </table>
            </div>
            </div>
        """, unsafe_allow_html=True)
        s_btn =  st.button("Detail>")
        if s_btn:
            ascendse_show()
