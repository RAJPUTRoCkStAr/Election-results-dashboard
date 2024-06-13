import streamlit as st
import pandas as pd

# Function to generate the URL for each party
def read_pages(party):
    return f"?party={party}"

# Function to create clickable links
def create_clickable_link(party, won):
    return f'<a href="{read_pages(party)}">{won}</a>'

# Function to display party details
def display_party_details(selected_party):
    try:
        pages = pd.read_csv(f'partywise/{selected_party}.csv')
        st.dataframe(pages)
    except FileNotFoundError:
        st.error(f"No data available for {selected_party}")

# Main function
def main():
    st.set_page_config(page_title='Party Details')
    query_params = st.experimental_get_query_params()
    if 'party' in query_params:
        selected_party = query_params['party'][0]
        st.write(f'Details for Party: {selected_party}')
        display_party_details(selected_party)

        # Add a button to redirect back to the main page with the selected party
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        if st.button("Go back to Main Page"):
            st.experimental_rerun()
    else:
        st.write("No party selected.")

if __name__ == "__main__":
    st.subheader('Party Wise Results Status')
    data = {
        'Party': ['Party A', 'Party B', 'Party C'],
        'Won': [100, 150, 200]
    }
    second_data = pd.DataFrame(data)
    second_data['Won'] = second_data.apply(lambda row: create_clickable_link(row['Party'], row['Won']), axis=1)
    st.markdown(second_data.to_html(escape=False, index=False), unsafe_allow_html=True)

    query_params = st.experimental_get_query_params()
    if 'party' in query_params:
        selected_party = query_params['party'][0]
        st.write(f'You selected: {selected_party}')
        main()
