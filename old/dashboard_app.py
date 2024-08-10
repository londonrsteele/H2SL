import sys
import pandas as pd
import plotly.graph_objects as pltgo
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtWebEngineWidgets import QWebEngineView

class DashboardApp(QMainWindow):
    def __init__(self, df):
        super().__init__()
        self.setWindowTitle("Helldivers 2 Stats Logger Dashboard")
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.data = df

    def show_figure(self, figure):
        self.browser.setHtml(figure.to_html(include_plotlyjs="cdn"))

    def EOM_shots(self):
        # EOM Accuracy = x%
        # EOM Shots Fired = y
        # EOM Shots Hit = z
        shots_data = {
            "x" : [0, 0],
            "Shots" : [self.data["eom_shots_fired"], self.data["eom_shots_hit"]],
            "labels" : ["Shots Fired", "Shots Hit"],
            "Accuracy": str("Accuracy = " + str(self.data["eom_accuracy"][0]) + "%")
        }
        
        fig = pltgo.Figure(
            data=[
                pltgo.Bar(
                    name="Shots Fired",
                    x=shots_data["x"],
                    y=shots_data["Shots"][0],
                    offsetgroup=0,
                    marker_color="#024a70",
                    text=shots_data["Shots"][0]
                ),
                pltgo.Bar(
                    name="Shots Hit",
                    x=shots_data["x"],
                    y=shots_data["Shots"][1],
                    offsetgroup=0,
                    marker_color="#051c2c",
                    text=shots_data["Shots"][1]
                )
            ],
            layout=pltgo.Layout(
                title="Shots Accuracy",
                yaxis_title = "Shots"
            ),
        )
        fig.add_annotation(xref="paper", yref="paper", 
                           x=0.75, y=(self.data["eom_accuracy"][0]/100),
                           text=shots_data["Accuracy"],
                           arrowhead=1, arrowsize=1, arrowwidth=2,
                           font=dict(
                               size=18,
                               color="White"
                           ),
                           arrowcolor="White"
                           )
        fig.update_xaxes(showticklabels=False)
        fig.update_traces(textposition="inside")
        self.show_figure(fig)


    def EOM_dashboard(self):
        print("Showing EOM Dashboard")
        self.EOM_shots()
        # self.update_html("Showing EOM Dashboard")
        
if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # sys.argv argv1 is filepath for df
    df = pd.read_csv(sys.argv[1])
    print(df.head())

    # QMainWindow using QWebEngineView as central widget
    window = DashboardApp(df)
    window.resize(800, 600)
    window.show()

    # sys.argv argv2 is code for which dashboard to display
    if(sys.argv[2] == "EOM"):
        window.EOM_dashboard()

    # Execute Qt application
    sys.exit(app.exec())