from PyQt6.QtWidgets import QGridLayout, QCheckBox, QLabel, QComboBox, QPushButton, QLineEdit, QCompleter, QWidget
from PyQt6.QtCore import Qt

class Filter(QWidget):
    def __init__(self, builder=None, header=[], initial=0):
        super().__init__()
        grid_layout = QGridLayout()

        self.text_field1 = QLineEdit(self)
        completer = QCompleter(header, self.text_field1)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.text_field1.setCompleter(completer)
        if initial:
            grid_layout.addWidget(QLabel("Column:"), 0, 0)
        grid_layout.addWidget(self.text_field1, initial, 0)

        self.dropdown = QComboBox(self)
        self.dropdown.addItems([">", "<", ">=", "<=", "==", "!=", "Contains"])
        if initial:
            grid_layout.addWidget(QLabel("Operator:"), 0, 1)
        grid_layout.addWidget(self.dropdown, initial, 1)

        self.text_field2 = QLineEdit(self)
        if initial:
            grid_layout.addWidget(QLabel("Value:"), 0, 2)
        grid_layout.addWidget(self.text_field2, initial, 2)

        self.switch = QCheckBox("N/As", self)
        grid_layout.addWidget(self.switch, initial, 3)

        self.delete_button = QPushButton('X')
        self.delete_button.setFixedSize(20, 20)
        self.delete_button.clicked.connect(lambda: self.delete_filter(builder))
        grid_layout.addWidget(self.delete_button, initial, 4)
        if initial:
            self.delete_button.setEnabled(False)

        self.setLayout(grid_layout)

    def get_values(self):
        value1 = self.text_field1.text()
        operator = self.dropdown.currentText()
        value2 = self.text_field2.text()
        nas = self.switch.isChecked()
        return [value1, operator, value2, nas]

    def delete_filter(self, builder):
        self.deleteLater()
        builder.filters.remove(self)