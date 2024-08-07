import pandas as pd
import plotly.graph_objects as pgo
import dash
from dash import Dash, html
import webbrowser
from flask import request

dashapp = Dash()
dashapp.layout = [html.Div(children="Hello World!")]

def shutdown():
    func = request.environ.get("wekzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Wekzeug Server")
    func()

@dashapp.callback([dash.dependencies.Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/kill":
        shutdown()

if __name__ == "__main__":
    dashapp.run(port=8050)