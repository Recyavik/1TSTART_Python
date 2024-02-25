"""Initializie Dash app."""
# import sqlite3
from dash import Dash, html, dcc, Output, Input, dash_table
import plotly.express as px
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/'
                 'master/gapminder_unfiltered.csv')

# conn = sqlite3.connect('file.db')
# df = pd.read_sql_query("SELECT * FROM table_name", conn)

dash_app = Dash()

dash_app.layout = html.Div([
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    # Отрисовка графика, определяемого через ф-ию коллбэка.
    # Сама функция создана ниже.
    dcc.Graph(id='graph-content'),
    # Отрисовка обычной таблицы с данными
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # Отрисовка гистограммы
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
    # Отрисовка круговой диаграммы
    dcc.Graph(figure=px.pie(df, values='pop', names='continent', title='Population of European continent', height=500)),
], style={'backgound-color': '#fff'})


@dash_app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop')


if __name__ == '__main__':
    dash_app.run()
