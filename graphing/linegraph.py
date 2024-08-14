import pandas as pd
import plotly.graph_objects as pltgo
import plotly.express as pltxp
from graphing import metadata

def Create_LineGraph(stats_last10):
    x_list = []
    for i in range(-len(stats_last10)+1,0):
        x_list.append(str(i))
    x_list.append("Last Mission")
    df = pd.DataFrame(list(zip(x_list,stats_last10)), columns=["X","Y"])

    fig = pltxp.line(df, x="X", y="Y", text="Y", markers=True)
    fig.update_traces(textposition="top center")
    return fig