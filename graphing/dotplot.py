import plotly
import plotly.graph_objects as pltgo
from graphing import metadata
from graphing import stat_scraper

def Create_EOM_Dotplot(minmaxed_stats):
    # mins will be at 0, maxes will be at 1
    # minmax will be between 0 and 1
    min = [0] * len(minmaxed_stats)
    max = [1] * len(minmaxed_stats)

    # Create the Figure
    fig = pltgo.Figure()
    fig.add_trace(pltgo.Scatter(
        x=minmaxed_stats,
        y=metadata.list_of_EOM_strats,
        marker=dict(
            color=minmaxed_stats, 
            cmax=1, cmin=0,
            colorscale=metadata.color_scale, 
            size=20,
            line=dict(
                width=2,
                color="black"
            ),
            colorbar=dict(
                title="Stat<br>Color<br>Scale<br>",
                len=0.5,
                lenmode="fraction",
                tickvals=[0, 0.25, 0.50, 0.75, 1],
                ticktext=["0%", "25%", "50%","75%", "100%"],
            )
        ),
        mode="markers",
        name="Stat (%)",
        hovertemplate="%{y}: %{x:.0%}<extra></extra>"
    ))
    fig.update_layout(
        title="<b>Stat Performance</b>",
        title_x=0.5,
        xaxis_title="<b>% of Best Performance<br></b>",
        yaxis_title="<b><br>Stat</b>",
        xaxis_tickformat=".0%",
        font=dict(
            family="sans-serif",
            size=18,
            color=metadata.dict_of_colors["white"]
        ),
        paper_bgcolor=metadata.dict_of_colors["black"],
        plot_bgcolor=metadata.dict_of_colors["light-black"],
        hovermode="closest",
        hoverlabel={
            "font_size":14
        }
    )
    fig.update_xaxes(
        ticks="outside",
        showline=True,
        linecolor=metadata.dict_of_colors["grey"], 
        gridcolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["grey"]
    )
    fig.update_yaxes(
        ticks="outside",
        showline=True,
        linecolor=metadata.dict_of_colors["grey"], 
        gridcolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["grey"]
    )
    return fig