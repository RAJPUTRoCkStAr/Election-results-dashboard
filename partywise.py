import streamlit as st
import pandas as pd
def detail_page():
    selected_party = st.experimental_get_query_params().get("party", [None])[0]
    if selected_party:
        st.markdown(f"# {selected_party} Page")
    try:
        pages = pd.read_csv(f'partywise/{selected_party}.csv')
        st.dataframe(pages)
    except FileNotFoundError:
        st.error(f"No data available for {selected_party}")