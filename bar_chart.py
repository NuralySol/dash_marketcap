import plotly.express as px
from dash import html, dcc

def render(app, data, x="country", y="marketcap", title="Bar Chart by Country Marketcap", chart_id="bar-chart"):
    fig = px.bar(
        data,
        x=x,
        y=y,
        color=x,
        title=title
    )
    
    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
    )
    
    return html.Div(dcc.Graph(figure=fig), id=chart_id)