from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from datasets.load import df_brasil, df_states
import json

from graphics.mapbox import create_mapbox
from graphics.scatter import create_scatter
from graphics.pie import create_pie

df_states_ = df_states[df_states["data"] == "2022-01-01"]
brazil_states = json.load(open("geojson/brazil_geo.json", "r"))
df_data = df_states[df_states['estado']=="RJ"]

select_columns = {
    "casosAcumulado": "Casos Acumulados", 
    "casosNovos": "Novos Casos", 
    "obitosAcumulado": "Óbitos Totais",
    "obitosNovos": "Óbitos por dia"
    }

fig = create_mapbox()
fig2 = create_scatter()
fig3 = create_pie()

layout = dbc.Container(
    dbc.Row([
        dbc.Col([ 
            html.Div([
                html.H3("Evolução CONVID-19"),
                dbc.Button("Brasil", color="primary", id="location-button", size="lg")
            ], style={}),
            html.P("Informe a data na qual deseja obter informações", style={"marginTop": "40px"}),
            html.Div(
                children=[dcc.DatePickerSingle(
                    id="date-picker",
                    min_date_allowed=df_brasil["data"].min(),
                    max_date_allowed=df_brasil["data"].max(),
                    initial_visible_month = df_brasil["data"].min(),
                    date=df_brasil["data"].max(),
                    display_format="D MMMM YYYY",
                    style={"border": "0px solid black", 'width': '100%'},
                )] ,id="div-test", style={'width': '100%'}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Casos recuperados", style={"fontSize": "0.8rem"}),
                            html.H5(style={"color": "#adfc92"}, id="casos-recuperados-text"),
                            html.Span("Em acompanhamento", style={"fontSize": "0.8rem"}),
                            html.H5(id="em-acompanhamento-text")
                        ])
                    ], className="card border-primary", outline=True, style={
                        "marginTop": "10px",
                        "boxShadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)"
                        })
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Confirmados totais", style={"fontSize": "0.8rem"}),
                            html.H5(style={"color": "#389fd6"}, id="casos-confirmados-text"),
                            html.Span("Novos casos na data", style={"fontSize": "0.8rem"}),
                            html.H5(id="novos-casos-text")
                        ])
                    ], className="card border-primary", outline=True, style={
                        "marginTop": "10px",
                        "boxShadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)"
                        })
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Óbitos confirmados", style={"fontSize": "0.8rem"}),
                            html.H5(style={"color": "#df2935"}, id="obitos-text"),
                            html.Span("Óbitos na data", style={"fontSize": "0.8rem"}),
                            html.H5(id="obitos-na-data-text")
                        ])
                    ], className="card border-primary", outline=True, style={
                        "marginTop": "10px",
                        "boxShadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)"
                        })
                ], md=4)
            ]),
            html.Div([
                html.P("Selecione o tipo de dado que deseja visualizar", style={"marginTop": "25px"}),
                dcc.Dropdown(
                    id='location-dropdown',
                    options=[{"label": j, "value": i } for i, j in select_columns.items()],
                    value="casosNovos",
                    style={"marginTop": "10px", 'marginBottom': '10px'},
                    ),
                dcc.Graph(id="line-graph", figure=fig2)
            ], style={"marginTop":"20px","padding": "20px","boxShadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)"})
            
        ], md=6, style={"paddingTop": "25px", "paddingLeft": "25px"}),
        dbc.Col([ 
            dcc.Loading(
                id="loading-1",
                type="default",
                style={"color": "#593196", "backGroundColor": "#593196"},
                color="#593196",
                children =[
                    dcc.Graph(id="choropleth-map", figure=fig, style={
                        "height": "60vh", 
                        "paddingRight": "20px",
                        "marginLeft": "60px",
                        "marginRight": "20px",
                        "paddingBottom": "20px",
                        "paddingTop": "20px",
                        "paddingLeft": "20px",
                        "boxShadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)"
                        })
                ]
            ),
            dcc.Graph(id="pizza", figure=fig3, style={
                "paddingTop": "20px", 
                "marginLeft": "60px"
                })

            
            
            ], md=6, style={"paddingTop": "25px"})
    ], className="g-0"),
    fluid=True
)