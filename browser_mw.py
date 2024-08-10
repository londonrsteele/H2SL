import sys
import subprocess
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtWebEngineWidgets import QWebEngineView

class BrowserMW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl("http://127.0.0.1:8050/")
        self.setCentralWidget(self.browser)
        self.show()
    
    def closeEvent(self, event):
        self.browser.setUrl("http://127.0.0.1:8050/kill")
        event.accept()

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # QMainWindow using QWidget as central widget
    window = BrowserMW()
    window.showMaximized()
    window.setWindowTitle("Helldivers 2 Stats Logger Dashboard")
    window.show()

    # how many args are passed?
    if len(sys.argv) == 3:
        # sys.argv argv1 is EOM/CAR/BOTH, argv2 is datafile
        if sys.argv[1] == "EOM":
            subprocess.Popen("python EOM_dashapp.py " + str(sys.argv[2]))
        elif sys.argv[1] == "CAR":
            subprocess.Popen("python CAR_dashapp.py " + str(sys.argv[2]))
    elif len(sys.argv) == 4:
        # sys.argv argv1 is BOTH, argv2 is datafile, argv3 is datafile
        subprocess.Popen("python dashapp.py " + str(sys.argv[2]) + " " + str(sys.argv[3]))

    # Execute Qt application
    sys.exit(app.exec())