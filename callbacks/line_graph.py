import plotly.graph_objects as go
from datasets.load import df_states, df_brasil

color_white = "#ede9f6"

def plot_line_graph_callback(plot_type, location):
    if location == "Brasil":
        df_data_on_location = df_brasil.copy()
    else:
        df_data_on_location = df_states[df_states["estado"] == location]
    
    bar_plots = ['casosNovos', 'obitosNovos']

    fig = go.Figure()

    if plot_type in bar_plots:
        fig.add_trace(go.Bar(x=df_data_on_location['data'], y=df_data_on_location[plot_type]))
    else:
        fig.add_trace(go.Scatter(x=df_data_on_location['data'], y=df_data_on_location[plot_type]))

    fig.update_layout(
        paper_bgcolor=color_white,
        plot_bgcolor=color_white,
        autosize=True,
        margin=dict(l=0,r=0,t=0,b=0)
    )

    return fig