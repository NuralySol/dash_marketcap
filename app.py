from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd
from layout import create_layout
from util import get_data 

# Load the data from a fixture
PATH = "./data/LargestCompanies.csv"
data = get_data(PATH)

# Print the head to verify the data was loaded correctly
print("-" * 90)
print(data.head())

# Initialize the main Dash app and apply Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = create_layout(app, data)

if __name__ == "__main__":
    app.run_server(debug=True)
