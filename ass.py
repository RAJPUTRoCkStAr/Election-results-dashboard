# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(layout="wide")
# st.write('election commission of india')

# # Sample dataframe
# first_data = pd.DataFrame({
#     "Party": ["Bharatiya Janata Party - BJP", "Indian National Congress - INC", "Samajwadi Party - SP", "All India Trinamool Congress - AITC", "Dravida Munnetra Kazhagam - DMK", "Telugu Desam - TDP", "Janata Dal  (United) - JD(U)", "Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT", "Nationalist Congress Party - Sharadchandra Pawar - NCPSP", "Shiv Sena ", "Others", "Total"],
#     "Won": [100, 80, 70, 60, 50, 40, 30, 20, 10, 5, 3, 1000]
# })

# # Sort dataframe by 'Won' column in ascending order
# first_data = first_data.sort_values(by='Won')

# # Define specific colors for each party using hexadecimal values
# color_discrete_map = {
#     "Bharatiya Janata Party - BJP": "#ff8331",
#     "Indian National Congress - INC": "#17aaed",
#     "Samajwadi Party - SP": "#ff0000",
#     "All India Trinamool Congress - AITC": "#aebedf",
#     "Dravida Munnetra Kazhagam - DMK": "#o5f89e",
#     "Telugu Desam - TDP":"#204795",
#     "Janata Dal  (United) - JD(U)":"#39ac57",
#     "Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT":"#61da8c",
#     "Nationalist Congress Party - Sharadchandra Pawar - NCPSP":"#457a8b",
#     "Shiv Sena ":"#d2691e",
#     "Others":"#b3b3b3"
# }

# # Create a donut chart using Plotly
# fig = px.pie(first_data, values=first_data['Won'], names=first_data['Party'], title='Votes Distribution by State', color='Party', color_discrete_map=color_discrete_map)

# # Update layout to create donut chart effect and start angle at 270 degrees
# fig.update_traces(hole=0.4, hoverinfo="label+percent+name")

# # Display the donut chart in Streamlit
# st.plotly_chart(fig)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.write('election commission of india')

# Sample dataframe
first_data = pd.DataFrame({
    "Party": ["Bharatiya Janata Party - BJP", "Indian National Congress - INC", "Samajwadi Party - SP", "All India Trinamool Congress - AITC", "Dravida Munnetra Kazhagam - DMK", "Telugu Desam - TDP", "Janata Dal  (United) - JD(U)", "Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT", "Nationalist Congress Party - Sharadchandra Pawar - NCPSP", "Shiv Sena ", "Others", "Total"],
    "Won": [100, 80, 70, 60, 50, 40, 30, 20, 10, 5, 3, 1000]
})

# Sort dataframe by 'Won' column in ascending order, excluding "Total" row
first_data = first_data[first_data['Party'] != 'Total'].sort_values(by='Won')

# Concatenate "Total" row at the end
first_data = pd.concat([first_data, first_data[first_data['Party'] == 'Total']])

# Define specific colors for each party using hexadecimal values
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

# Create a donut chart using Plotly
fig = px.pie(first_data, values=first_data['Won'], names=first_data['Party'], title='Votes Distribution by State', color='Party', color_discrete_map=color_discrete_map)

# Update layout to create donut chart effect
fig.update_traces(hole=0.4, hoverinfo="label+percent+name")

# Display the donut chart in Streamlit
st.plotly_chart(fig)
