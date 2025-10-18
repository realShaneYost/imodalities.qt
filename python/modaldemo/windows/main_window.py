from PySide6 import QtWidgets, QtCore
from modaldemo.dialogs.progress_dialog import ProgressDialog

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    self.resize(520, 240)

    run_button = QtWidgets.QPushButton("Run Task")
    run_button.clicked.connect(self.start_task)

    central = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(central)
    layout.addStretch(1)
    layout.addWidget(run_button, alignment=QtCore.Qt.AlignCenter)
    layout.addStretch(1)
    self.setCentralWidget(central)

  def start_task(self):
    progress_dialog = ProgressDialog(parent=self)
    percent_complete = 0
    ticker = QtCore.QTimer(interval=15)

    # My little worker simulation
    def do_one_unit_of_work():
      nonlocal percent_complete
      if not progress_dialog:
        ticker.stop()
        return
      percent_complete +=1
      progress_dialog.set_progress(percent_complete)
      if percent_complete >= 100:
        ticker.stop()

    ticker.timeout.connect(do_one_unit_of_work)
    ticker.start()

    # Handlers to the signals that accept/reject emit
    def on_rejected():
      if ticker.isActive():
        ticker.stop()
      print(f"Task canceled")

    def on_accepted():
      print(f"Task complete")

    progress_dialog.rejected.connect(on_rejected)
    progress_dialog.accepted.connect(on_accepted)
    progress_dialog.show()
