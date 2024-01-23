from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QScrollArea, QProgressDialog, QPushButton, QWidget
from Filter import Filter
from FindDatatypes import find_datatypes
from Process import process

class FilterBuilder(QMainWindow):
    def __init__(self, header=[], file=None):
        super().__init__()
        self.table_viewer = None
        self.processing_view = None

        self.filepath = file

        self.main_layout = QVBoxLayout()

       
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        self.filters_layout = QVBoxLayout(scroll_widget)
        scroll_widget.setLayout(self.filters_layout)
        scroll_area.setWidget(scroll_widget)

        self.filters = []

        initial_filter = Filter(self, header, True)
        self.filters.append(initial_filter)
        self.add_param_button = QPushButton('New Parameter')
        self.add_param_button.clicked.connect(lambda: self.add_param_widget(header))
        self.filters_layout.addWidget(initial_filter)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit)

        self.main_layout.addWidget(scroll_area)
        self.main_layout.addWidget(self.add_param_button)
        self.main_layout.addWidget(self.submit_button)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('AutoComplete Text Field')
        self.setGeometry(100, 100, 420, 250)

    def add_param_widget(self, header):
        new_filter = Filter(self, header)
        self.filters.append(new_filter)
        self.filters_layout.addWidget(new_filter)

    def submit(self):
        self.submit_button.setEnabled(False)
        params = []
        for filter in self.filters:
            params.append(filter.get_values())
        
        progress_dialog = QProgressDialog(self)
        progress_dialog.setLabelText("Please wait...")
        progress_dialog.setRange(0, 0)
        progress_dialog.setWindowTitle("Processing")
        progress_dialog.show()
        
        columnIndex, columnType = find_datatypes(self.filepath, params)
        process(self.filepath, params, columnIndex, columnType)
        
        delim = '\t'
        if self.filepath.endswith('.csv'):
            delim = ','
        rows = []
        for index, row in enumerate(open('temp')):
            if index > 100:
                break
            rows.append(row.strip().split(delim))
        from TableViewerWindow import TableViewerWindow
        self.table_viewer = TableViewerWindow(rows=len(rows), columns=len(rows[0]), data=rows)
        progress_dialog.hide()
        self.table_viewer.show()
        self.hide()