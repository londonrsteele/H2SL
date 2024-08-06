import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from input_widget import CAR_Input_Widget, EOM_Input_Widget
from dashboard_widget import Dashboard_Widget

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # Qt widgets (QWidgets)
    CAR_input_widget = CAR_Input_Widget()
    EOM_input_widget = EOM_Input_Widget()
    dashboard_widget = Dashboard_Widget()

    # QMainWindow using QWidget as central widget
    window = MainWindow(CAR_input_widget, EOM_input_widget, dashboard_widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())