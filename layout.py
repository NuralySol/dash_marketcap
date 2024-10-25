from dash import html
import dash_bootstrap_components as dbc
import bar_chart, pie_chart, scatter, h_bar_chart

def create_layout(app, data):
    heading = html.H1(
        "Countries by Market Cap Analysis",
        className="bg-primary text-white text-center p-3 mb-4 rounded",
        style={"font-weight": "bold"}
    )

    return dbc.Container(
        fluid=True,  # Make the container fluid to span full-width on large screens
        children=[
            heading,
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4(" Countries by marketcap ", className="text-center mt-3 mb-3"),
                            pie_chart.render(app, data)
                        ],
                        lg=6,
                        className="p-3"
                    ),
                    dbc.Col(
                        [
                            html.H4(" Bar Chart", className="text-center mt-3 mb-3"),
                            bar_chart.render(app, data)
                        ],
                        lg=6,
                        className="p-3"
                    ),
                ],
                className="mb-4"
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Scatter Plot", className="text-center mt-3 mb-3"),
                            scatter.render(app, data)
                        ],
                        lg=5,
                        className="p-3"
                    ),
                    dbc.Col(
                        [
                            html.H4("H Bar Chart in Trillions", className="text-center mt-3 mb-3"),
                            h_bar_chart.render(app, data)
                        ],
                        lg=7,
                        className="p-3"
                    ),
                ],
                className="mb-4"
            ),
        ],
        style={"max-width": "1200px", "margin": "auto"}  
    )