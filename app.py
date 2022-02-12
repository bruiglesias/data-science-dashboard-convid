import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from callbacks.display_status import display_status_callback
from callbacks.pie_graph import pie_graph_callback
from callbacks.line_graph import plot_line_graph_callback
from callbacks.update_map import update_map_callback, update_location_callback

from dashboard import layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.PULSE])

app.layout = layout


@app.callback(
    [
        Output("casos-recuperados-text", "children"),
        Output("em-acompanhamento-text", "children"),
        Output("casos-confirmados-text", "children"),
        Output("novos-casos-text", "children"),
        Output("obitos-text", "children"),
        Output("obitos-na-data-text", "children"),
    ], [Input("date-picker", "date"), Input("location-button", "children")]
)
def display_status(date, location):
    return display_status_callback(date, location)

@app.callback(Output('pizza', 'figure'),
    [
        Input("date-picker", "date"), 
        Input("location-button", "children")
    ]
)
def pie_graph(date, location):
    return pie_graph_callback(date, location)

@app.callback(Output('line-graph', 'figure'),[
    Input("location-dropdown", "value"),
    Input("location-button", "children"),
    ])
def plot_line_graph(plot_type, location):
    return plot_line_graph_callback(plot_type, location)

@app.callback(
    Output("choropleth-map", "figure"), 
    [Input("date-picker", "date")]
)
def update_map(date):
    return update_map_callback(date)

@app.callback(
    Output("location-button", "children"),
    [Input("choropleth-map", "clickData"), Input("location-button", "n_clicks")]
)
def update_location(click_data, n_clicks):
    return update_location_callback(click_data, n_clicks)

if __name__ == "__main__":
    app.run_server(port=8051,debug=True)


