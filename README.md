# Election Results Dashboard

This Streamlit application displays election results for various constituencies, parties, and states in India. The dashboard provides a user-friendly interface to explore the results of the General Election to Parliamentary Constituencies in June 2024.

## Features

- **Constituency-specific Results**: Displays detailed election results for selected constituencies, including candidate information, votes, and winning status.
- **Party-specific Results**: Shows election results for a selected party, with links to individual constituencies.
- **State-specific Results**: Presents state-wise election trends and results.
- **General Election Overview**: Provides a general overview of the election results, including pie charts and tables with party-wise vote shares and results.

## Installation

To run the application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RAJPUTRoCkStAr/Election-py.git
    cd Election-results-dashboard
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

## Usage

The application provides several ways to explore the election results:

1. **Query Parameters**:
    - You can directly access specific results by setting query parameters in the URL.
    - Example: `http://localhost:8501/?party=BJP`, `http://localhost:8501/?state=Karnataka`, `http://localhost:8501/?constituency=Bangalore South`

2. **Option Menu**:
    - If no query parameters are set, you can use the option menu to select between "Parliament Constituency General", "Assembly Constituency General", and "Assembly Constituency Bye".
    - Depending on the selection, the application displays relevant results and trends.

3. **Dataframe_config**:
   - Which shows the image of the candidate and whether they have won or lost
   - Also how to use dataframe_config efficently



For live usage and demo, visit [Indian election result dashboard](https://india-election.streamlit.app/).
## License

This project is licensed under the MIT License.
