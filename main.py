import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)  

    # QMainWindow using QWidget as central widget
    window = MainWindow()
    window.resize(800, 600)
    window.show()

    # Execute Qt application
    sys.exit(app.exec())
