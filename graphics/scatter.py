import plotly.graph_objects as go
from datasets.load import df_states

color_white = "#ede9f6"

df_states_ = df_states[df_states["data"] == "2022-01-01"]
df_data = df_states[df_states['estado']=="RJ"]


def create_scatter():

    fig = go.Figure()
    fig.add_trace(go.Scatter( x=df_data['data'], y=df_data['casosAcumulado']))

    fig.update_layout(
        paper_bgcolor=color_white,
        plot_bgcolor=color_white,
        autosize=True,
        margin=dict(l=0,r=0,t=0,b=0)
    )

    return fig