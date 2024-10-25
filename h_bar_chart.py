import plotly.express as px
from dash import html, dcc

def render(app, data, x="marketcap", y="country", title="H - Bar Chart of Marketcap", orientation="h", chart_id="h_age_chart"):
    fig = px.bar(
        data,
        x=x,
        y=y,
        orientation=orientation,
        title=title,
        color=y,  # Adding color by category for a nicer look
        text=x  # Display values on bars for readability
    )
    
    # Update layout for better readability and styling
    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
        title_font_size=20,
        template="plotly_white",  # Use a clean, white theme
        height=600  # Increase height for better visibility
    )
    
    # Customize bar appearance
    fig.update_traces(
        texttemplate='%{text:.2s}',  # Shorten the text display on bars
        textposition="outside",      # Place text outside bars for clarity
        marker=dict(line=dict(width=1, color="DarkSlateGrey"))  # Add a border for contrast
    )
    
    return html.Div(dcc.Graph(figure=fig), id=chart_id)