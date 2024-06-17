import streamlit as st
import pandas as pd 
import random
def acb_show():
    st.header('Bye Election to Assembly Constituencies: Results June-2024', divider='green')
    data = pd.read_csv('data/last_page.csv')
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
 