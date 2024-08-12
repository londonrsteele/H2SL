import plotly.graph_objects as pltgo
from graphing import metadata
from graphing import stat_scraper

def Create_EOM_Dotplot(minmaxed_stats):
    # mins will be at 0, maxes will be at 1
    # minmax will be between 0 and 1
    min = [0] * len(minmaxed_stats)
    max = [1] * len(minmaxed_stats)

    fig = pltgo.Figure()
    # Add 0's (mins)
    fig.add_trace(pltgo.Scatter(
        x=min,
        y=metadata.list_of_EOM_strats,
        marker=dict(color="black", size=12),
        mode="markers",
        name="Worst Performance (0%)",
    ))
    # Add 1's (max)
    fig.add_trace(pltgo.Scatter(
        x=max,
        y=metadata.list_of_EOM_strats,
        marker=dict(color="black", size=12),
        mode="markers",
        name="Best Performance (100%)",
    ))
    # Add x's (minmaxed_stats)
    fig.add_trace(pltgo.Scatter(
        x=minmaxed_stats,
        y=metadata.list_of_EOM_strats,
        marker=dict(color="red", size=12),
        mode="markers",
        name="Stat (%)",
        hovertemplate="%{x:%.0f}"
    ))
    fig.update_layout(title="Stat Performance",
                    xaxis_title="% of Best Performance",
                    yaxis_title="Stat",
                    xaxis_tickformat=".0%")

    return fig