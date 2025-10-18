import sys
from PySide6 import QtWidgets
from modaldemo.windows.main_window import MainWindow

def main():
  app = QtWidgets.QApplication(sys.argv)
  win = MainWindow()
  win.show()
  sys.exit(app.exec())
