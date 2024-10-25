import plotly.express as px
from dash import html, dcc

def render(app, data, x="country", y="marketcap", size="marketcap", title="Scatter of the Marketcap", chart_id="scatter-chart"):
    fig = px.scatter(
        data,
        x=x,
        y=y,
        size=size,
        title=title,
        hover_name=x,  # Use x-axis column name in hover
        hover_data={y: True, size: True},  # Show y and size values on hover
    )
    
    # Customize layout for readability
    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
        title_font_size=20,
    )
    
    return html.Div(dcc.Graph(figure=fig), id=chart_id)