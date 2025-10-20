from PySide6 import QtWidgets, QtCore

class ProgressDialog(QtWidgets.QDialog):
  def __init__(self, parent=None, width=420, height=140, show_buttons=True):
    super().__init__(parent)

    self.setWindowTitle("Working...")
    self.resize(width, height)

    self.show_buttons = show_buttons

    # Set callbacks in the owner (E.g. MainWindow). Callbacks are for handling behavior only after
    # the buttons cancel/done have been invoked. Practical for modal based dialogs.
    self.on_cancel_callback = None
    self.on_done_callback = None

    self.overall_label = QtWidgets.QLabel("Working…", self)
    self.progress_bar = QtWidgets.QProgressBar(self)
    self.progress_bar.setRange(0, 100)
    self.progress_bar.setValue(0)

    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.overall_label)
    layout.addWidget(self.progress_bar)

    if self.show_buttons:
      self.setWindowModality(QtCore.Qt.WindowModal)
      self.done_button = QtWidgets.QPushButton("Done", self)
      self.done_button.setEnabled(False)
      self.done_button.clicked.connect(self.accept)
      self.cancel_button = QtWidgets.QPushButton("Cancel", self)
      self.cancel_button.clicked.connect(self.reject)

      buttons_layout = QtWidgets.QHBoxLayout()
      buttons_layout.addStretch(1)
      buttons_layout.addWidget(self.cancel_button)
      buttons_layout.addWidget(self.done_button)
      layout.addLayout(buttons_layout)

  def accept(self):
      try:
        if self.on_done_callback:
          self.on_done_callback()
      finally:
        super().accept()
        self.on_done_callback = None

  def reject(self):
      try:
        if self.on_cancel_callback:
          self.on_cancel_callback()
      finally:
        super().reject()
        self.on_cancel_callback = None

  def reset(self):
    self.progress_bar.setValue(0)
    self.overall_label.setText("Working…")
    if self.show_buttons:
      self.done_button.setEnabled(False)

  def set_progress(self, pct: int) -> None:
    # bounds check
    if pct < 0:
      pct = 0
    elif pct > 100:
      pct = 100
    self.progress_bar.setValue(pct)
    # When 100%
    if pct >= 100:
      self.overall_label.setText("Complete.")
      if self.show_buttons:
        self.done_button.setEnabled(True)
      # automatically close if no buttons are shown
      else:
        # small dwell so user sees completion
        QtCore.QTimer.singleShot(400, self.accept)
    else:
      self.overall_label.setText("Working…")
