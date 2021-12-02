import dash
from dash import dcc
from dash import html
import dash_daq as daq
from dash.dependencies import Input, Output
from flask import Flask, request
from flask_restful import Resource, Api

server = Flask('my_app')
app = dash.Dash(server=server)
api = Api(server)

current_temp = '1'

class UpdateTemp(Resource):
    def put(self):
        global current_temp
        current_temp = request.form['temp']


api.add_resource(UpdateTemp, '/api')

app.layout = html.Div([
    dcc.Interval(id='my_interval', disabled=False, n_intervals=0, interval=1000),
    
    html.H1(children='Dash example', style={
            'textAlign': 'center', 'color': 'white'}),

    html.Div(
        children=[
            daq.LEDDisplay(
                id="operator-led",
                value=current_temp,
                color="#92e0d3",
                backgroundColor="#1e2130",
                size=100,
            ),
        ],
        style={'textAlign': 'center'}
    )
])

@app.callback(
    Output('operator-led', 'value'),
    Input('my_interval', 'n_intervals')
)
def update_figure(v):
    return current_temp

if __name__ == '__main__':
    app.run_server(debug=True)
