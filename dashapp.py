import pandas as pd
import plotly.graph_objects as pgo
import dash
from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import webbrowser
from flask import request
import sys

# Create Dash app
dashapp = Dash()

# Get data from sys.argv[1]
df = pd.read_csv(sys.argv[1])
print(df.head())
# dff = pd.DataFrame([["Shots Fired", df["eom_shots_fired"][0]], ["Shots Hit", df["eom_shots_hit"][0]]], columns=["Stat", "Value"])

dashapp.layout = [html.Div(children="Hello")]


# Set up functions to close Dash app on "X" click
def shutdown():
    func = request.environ.get("wekzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Wekzeug Server")
    func()

@dashapp.callback([dash.dependencies.Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/kill":
        shutdown()


# Run Dash app
if __name__ == "__main__":
    dashapp.run(debug=True,port=8050)