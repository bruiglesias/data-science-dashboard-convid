import plotly.express as px
import plotly.graph_objects as go
import json
import dash

from datasets.load import df_states

color_white = "#ede9f6"

brazil_states = json.load(open("geojson/brazil_geo.json", "r"))

def update_map_callback(date):
    df_data_on_states = df_states[df_states["data"] == date]

    fig = px.choropleth_mapbox(df_data_on_states, locations="estado", geojson=brazil_states, 
        center={"lat": -14.95, "lon": -55.78},
        zoom=2.7, color="casosAcumulado", color_continuous_scale="Redor", opacity=0.55,
        hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": True}
        )

    fig.update_layout(
        paper_bgcolor=color_white,
        autosize=True,
        margin=go.layout.Margin(l=0,r=0,t=0,b=0),
        showlegend=False,
        mapbox_style="open-street-map"
    )

    return fig

def update_location_callback(click_data, n_clicks):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if click_data is not None and changed_id != "location-button.n_clicks":
        state = click_data["points"][0]["location"]
        return "{}".format(state)
    
    else:
        return "Brasil"