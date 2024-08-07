import sys
import subprocess
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtWebEngineWidgets import QWebEngineView
import graphing


class BrowserMW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl("http:/127.0.0.1:8050/")
        self.setCentralWidget(self.browser)
        self.show()
    
    def closeEvent(self, event):
        self.browser.setUrl("http:/127.0.0.1:8050/kill")
        event.accept()

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # QMainWindow using QWidget as central widget
    window = BrowserMW()
    window.resize(800, 600)
    window.show()

    # sys.argv argv1 is filepath for graphing df
    subprocess.Popen("python graphing.py " + str(sys.argv[1]))

    # Execute Qt application
    sys.exit(app.exec())