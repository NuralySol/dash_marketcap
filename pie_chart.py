import plotly.express as px
from dash import html, dcc

def render(app, data):
    fig = px.pie(
        data,
        values="marketcap",
        names="country",
        title="Top 5 largest countries by capitalization",
        color_discrete_sequence=px.colors.sequential.RdBu,  
        hole=0.4,
    )
    
    fig.update_layout(
        title_font_size=20,
        title_x=0.5,  
        margin=dict(t=40, b=20, l=0, r=0),  
        legend_title_text="Best Sellers in order",  
        legend=dict(
            orientation="h", 
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
    )
    # inline styling for the Div component id="pie-chart" is important to make the chart responsive
    return html.Div(
        [
            html.H2("Pie Chart of Countries ", style={"textAlign": "center", "color": "#333", "marginBottom": "13px"}),
            dcc.Graph(figure=fig),  
        ],
        style={
            "padding": "30px",
            "backgroundColor": "#f9f9f9",  
            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",  
            "borderRadius": "10px",  
            "maxWidth": "1000px",
            "margin": "auto"  
        },
        id="pie-chart"
    )