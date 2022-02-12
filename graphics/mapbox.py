import plotly.express as px
import plotly.graph_objects as go
from datasets.load import df_states
import json

color_white = "#ede9f6"

df_states_ = df_states[df_states["data"] == "2022-01-01"]

brazil_states = json.load(open("geojson/brazil_geo.json", "r"))


def create_mapbox():

    fig = px.choropleth_mapbox(
        df_states_, 
        locations="estado", 
        color="casosNovos",
        center={"lat": -14.95, "lon": -55.78}, 
        zoom=3,
        geojson=brazil_states, 
        color_continuous_scale="Redor", 
        opacity=0.4,
        hover_data={
            "casosAcumulado": True, 
            "casosNovos": True, 
            "obitosNovos": True,
            "estado": True
            }
        )

    fig.update_layout(
        paper_bgcolor=color_white,
        autosize=True,
        margin=go.layout.Margin(l=0,r=0,t=0,b=0),
        showlegend=False,
        mapbox_style="open-street-map"
    )

    return fig