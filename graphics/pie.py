import plotly.express as px


def create_pie():

    labels = ['recuperados ou em recuperação', 'óbitos']

    values = [70.0, 30.0]

    fig = px.pie(labels, values = values, hole = 0.4,
                names = labels, color = labels,
                title = 'Percentual de recuperados e óbitos',
                color_discrete_map = {'recuperados ou em recuperação':'blue', 'óbitos': 'red'})

    fig.update_traces(
                    title_font = dict(size=25,family='Verdana', color='darkred'),
                    hoverinfo='label+percent',
                    textinfo='percent', textfont_size=20)
    
    return fig