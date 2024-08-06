import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from input_widget import Input_Widget
from dashboard_widget import Dashboard_Widget

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # Qt widgets (QWidgets)
    input_widget = Input_Widget()
    dashboard_widget = Dashboard_Widget()

    # QMainWindow using QWidget as central widget
    window = MainWindow(input_widget, dashboard_widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())