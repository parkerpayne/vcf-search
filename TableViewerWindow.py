from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QFileDialog


class TableViewerWindow(QMainWindow):
    def __init__(self, rows, columns, data):
        super().__init__()
        self.init_ui(rows, columns, data)

    def init_ui(self, rows, columns, data):
        self.filter_builder = None
        # Create main layout
        main_layout = QVBoxLayout()

        new_file_btn = QPushButton('New File')
        new_file_btn.clicked.connect(self.show_file_browser)
        download_btn = QPushButton('Save')
        download_btn.clicked.connect(self.save)

        # Create table widget
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(rows)
        self.table_widget.setColumnCount(columns)

        # Populate the table with file contents
        for row, row_data in enumerate(data):
            for col, item_data in enumerate(row_data):
                item = QTableWidgetItem(item_data)
                self.table_widget.setItem(row, col, item)

        # Add widgets to the main layout
        main_layout.addWidget(new_file_btn)
        main_layout.addWidget(self.table_widget)
        main_layout.addWidget(download_btn)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

        # Set window properties
        self.setWindowTitle('Table Viewer')
        self.setGeometry(100, 100, 600, 400)

    def show_file_browser(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File')
        if file_path:
            print(f'Selected file: {file_path}')
            for line in open(file_path):
                header = line.strip().split('\t')
                break
            from FilterBuilder import FilterBuilder
            self.filter_builder = FilterBuilder(header, file_path)
            self.filter_builder.show()
            self.hide()
        
    
    def save(self):
        options = QFileDialog()
        file_path, _ = options.getSaveFileName(self, "Save As", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'w') as file:
                for line in open('temp'):
                    file.write(line)