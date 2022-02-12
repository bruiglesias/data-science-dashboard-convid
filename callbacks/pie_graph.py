import plotly.express as px
from datasets.load import df_states, df_brasil


def pie_graph_callback(date, location):
    if location == "Brasil":
        df_data_on_date = df_brasil[df_brasil["data"] == date]
    else:
        df_data_on_date = df_states[(df_states["estado"] == location) & (df_states["data"] == date)]

    casos_acumulados = 0 if df_data_on_date["casosAcumulado"].isna().values[0]  else int(df_data_on_date["casosAcumulado"].values[0]) 
    obitos_acumulado = 0 if df_data_on_date["obitosAcumulado"].isna().values[0]  else int(df_data_on_date["obitosAcumulado"].values[0])
    
    nao_obitos = casos_acumulados - obitos_acumulado
    nao_obitos_perc = nao_obitos / casos_acumulados * 100
    obitos_perc = obitos_acumulado / casos_acumulados * 100

    labels = ['recuperados ou em recuperação', 'óbitos']

    values = [nao_obitos_perc, obitos_perc]

    fig = px.pie(labels, values = values, hole = 0.4,
                names = labels, color = labels,
                title = 'Percentual de recuperados e óbitos',
                color_discrete_map = {'recuperados ou em recuperação':'blue', 'óbitos': 'red'})

    fig.update_traces(
                    title_font = dict(size=25,family='Verdana', color='darkred'),
                    hoverinfo='label+percent',
                    textinfo='percent', textfont_size=20)
    return fig
