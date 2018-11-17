import dash # importing the dash framework
import dash_core_components as dcc # importing the core components from dash
import dash_html_components as html # importing the html components from dash
from flask import Flask


app = dash.Dash()

app.layout = html.Div("Hello World")


if __name__ == '__main__':
    app.run_server(debug=True)
