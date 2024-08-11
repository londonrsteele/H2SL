import sys
import os
import signal
import subprocess
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtWebEngineWidgets import QWebEngineView
################################################################
# 
# Browser_mw class
#
################################################################
class BrowserMW(QMainWindow):
    ################################################################
    # Browser_mw initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl("http://127.0.0.1:8050/")
        self.setCentralWidget(self.browser)
        self.show()

    ################################################################
    # Browser_me member function: set_Pid
    ################################################################
    def set_Pid(self, pid):
        print("Dash running on pid " + str(pid))
        self.pid = pid

    ################################################################
    # Browser_mw (overloaded) member function: closeEvent 
    ################################################################
    def closeEvent(self, event):
        print("Killing Dash...")
        try:
            os.kill(self.pid, signal.SIGTERM)
            print(f"Sent SIGTERM signal to process {self.pid}")
        except OSError:
            print(f"Failed to send SIGTERM signal to process {self.pid}")
        event.accept()


################################################################
################################################################
# Execution: browser_mw.py __main__
################################################################
################################################################
if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # QMainWindow using QWidget as central widget
    window = BrowserMW()
    window.showMaximized()
    window.setWindowTitle("Helldivers 2 Stats Logger Dashboard")
    window.show()

    # From Load_data_widget, sys.argv[1] == "EOM"/"CAR"/"BOTH"
    #   If == "EOM", sys.argv[3] == "ERROR"
    #   If == "CAR", sys.argv[2] == "ERROR"
    if sys.argv[1] == "EOM":
        dashapp = "EOM_dashapp.py"
    elif sys.argv[1] == "CAR":
        dashapp = "CAR_dashapp.py"
    elif sys.argv[1] == "BOTH":
        dashapp = "dashapp.py"
    else:
        raise RuntimeError("ERROR: Cannot Start Dash")
    
    # Open appropriate Dash script and save pid
    dash_process = subprocess.Popen(["python", dashapp, sys.argv[2], sys.argv[3]])
    window.set_Pid(dash_process.pid)

    # Execute Qt application
    sys.exit(app.exec())