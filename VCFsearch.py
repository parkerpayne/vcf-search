import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QScrollArea, QHBoxLayout, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QCompleter, QWidget, QFileDialog
from PyQt6.QtCore import QTimer, Qt
from FilterBuilder import FilterBuilder

class MyApp(QApplication):
    def __init__(self, *args):
        super().__init__(*args)
        self.filter_builder = None  # Initialize filter_builder as an instance variable

def open_file_dialog(app):
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(None, 'Open File')  # Pass None as the parent
    if file_path:
        print(f'Selected file: {file_path}')
        for line in open(file_path):
            header = line.strip().split('\t')
            break
        app.filter_builder = FilterBuilder(header, file_path)
        app.filter_builder.show()


if __name__ == '__main__':
    app = MyApp(sys.argv)
    
    # Use a QTimer to execute the open_file_dialog function after starting the event loop
    QTimer.singleShot(0, lambda: open_file_dialog(app))

    sys.exit(app.exec())

        # Read the contents of the selected file
        # with open(file_path, 'r') as file:
        #     file_contents = file.read()
        # uglyrows = file_contents.split('\n')
        # rows = [row.split('\t') for row in uglyrows if row]
        # # Show the main window with the file contents
        # table_viewer = TableViewerWindow(rows=len(rows), columns=len(rows[0]), data=rows)
        # table_viewer.file_contents = file_contents
        # table_viewer.show()