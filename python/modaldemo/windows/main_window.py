from PySide6 import QtWidgets, QtCore
from modaldemo.dialogs.progress_dialog import ProgressDialog

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    self.resize(520, 240)

    self.progress_dialog = ProgressDialog(parent=self)
    self.percent_complete = 0

    self.ticker = QtCore.QTimer(interval=15)
    self.ticker.timeout.connect(self.do_one_unit_of_work)

    run_button = QtWidgets.QPushButton("Run Task")
    run_button.clicked.connect(self.start_task)

    central = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(central)
    layout.addStretch(1)
    layout.addWidget(run_button, alignment=QtCore.Qt.AlignCenter)
    layout.addStretch(1)
    self.setCentralWidget(central)

  def start_task(self):
    # Set callbacks in the task itself to support new callbacks (if required)
    self.progress_dialog.on_cancel_callback = self.on_cancel_callback
    self.progress_dialog.on_done_callback = self.on_done_callback

    self.percent_complete = 0
    self.progress_dialog.reset()
    self.progress_dialog.show()
    self.ticker.start()

  def do_one_unit_of_work(self):
    self.percent_complete +=1
    self.progress_dialog.set_progress(self.percent_complete)
    if self.percent_complete >= 100:
      self.ticker.stop()

  def on_cancel_callback(self):
    if self.ticker.isActive():
      self.ticker.stop()
    print("Task canceled")

  def on_done_callback(self):
    print("Task complete")
