import sys
import platform
from PySide2.QtCore import QTimer, Qt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pandas as pd
from Sorting import Algorithms
from PySide2.QtGui import QKeyEvent

# Loading Screen
from ui_Loading import Ui_SplashScreen

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class LoadingScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.load_main_ui)
        self.timer.start(40)

    def load_main_ui(self):
        value = self.ui.progressBar.value() + 1
        if value > 100:
            self.timer.stop()
            self.main_ui = MainWindow()
            self.main_ui.show()
            self.close()
        else:
            self.ui.progressBar.setValue(value)

class SearchResultsPopup(QDialog):
    def __init__(self, results):
        super().__init__()
        self.results = results
        self.current_index = 0
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.updateLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.current_index = (self.current_index - 1) % len(self.results)
            self.updateLabel()
        elif event.key() == Qt.Key_Down:
            self.current_index = (self.current_index + 1) % len(self.results)
            self.updateLabel()

    def updateLabel(self):
        self.label.setText(f"Result {self.current_index+1} of {len(self.results)}: {self.results[self.current_index]}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.btn_start.clicked.connect(self.sorting_admin_condition)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(200, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(self.confirm_exit)

        # Load CSV Data
        self.load_csv_data("Product Data\\products.csv")
        # Make self.ui.tableWidget non-editable
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Make self.ui.tableWidget_admin editable
        self.ui.tableWidget_admin.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)

        # Connect the login function to the Login button
        self.ui.Login_btn.clicked.connect(self.login)

       # Connect the textChanged signal to the live search function
        self.ui.btn_search.textChanged.connect(self.live_search)
        self.ui.btn_search.textChanged.connect(self.live_search_admin)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    def load_csv_data(self, file_path):
        data = pd.read_csv(file_path, encoding='utf-8')
        headers = data.columns.tolist()
        num_rows, num_columns = data.shape

        # Set the number of rows and columns in the QTableWidgets
        self.ui.tableWidget.setRowCount(num_rows)
        self.ui.tableWidget.setColumnCount(num_columns)

        self.ui.tableWidget_admin.setRowCount(num_rows)
        self.ui.tableWidget_admin.setColumnCount(num_columns)

        # Populate the header row
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget_admin.setHorizontalHeaderLabels(headers)

        # Populate the QTableWidgets with data
        for row_idx, row_data in data.iterrows():
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))

                # Set the item for the user table
                self.ui.tableWidget.setItem(row_idx, col_idx, item)

                # Create a new item for the admin table (don't reuse the item)
                item_admin = QTableWidgetItem(str(cell_data))
                self.ui.tableWidget_admin.setItem(row_idx, col_idx, item_admin)


    def live_search(self):
        search_text = self.ui.btn_search.text().lower()  # Convert search text to lowercase
        search_count = 0  # Initialize search count

        if not search_text:
            # If search text is empty, reset background color for all items
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    if item is not None:
                        item.setBackground(QBrush(QColor("#00ffff")))  # Set background color to cyan
            self.ui.search_count.setText("")  # Clear search count label
            return

        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    item_text = item.text().lower()
                    if search_text in item_text:
                        item.setBackground(QBrush(QColor("#ffff00")))  # Set background color to yellow
                        search_count += 1
                    else:
                        item.setBackground(QBrush(QColor("#00ffff")))  # Set background color to cyan
        self.ui.search_count.setText(str(search_count))

    def live_search_admin(self):
        search_text = self.ui.btn_search.text().lower()  # Convert search text to lowercase
        search_count = 0  # Initialize search count

        if not search_text:
            # If search text is empty, reset background color for all items
            for row in range(self.ui.tableWidget_admin.rowCount()):
                for col in range(self.ui.tableWidget_admin.columnCount()):
                    item = self.ui.tableWidget_admin.item(row, col)
                    if item is not None:
                        item.setBackground(QBrush(QColor("#00ffff")))  # Set background color to cyan
            self.ui.search_count.setText("")  # Clear search count label
            return

        for row in range(self.ui.tableWidget_admin.rowCount()):
            for col in range(self.ui.tableWidget_admin.columnCount()):
                item = self.ui.tableWidget_admin.item(row, col)
                if item is not None:
                    item_text = item.text().lower()
                    if search_text in item_text:
                        item.setBackground(QBrush(QColor("#ffff00")))  # Set background color to yellow
                        search_count += 1
                    else:
                        item.setBackground(QBrush(QColor("#00ffff")))  # Set background color to cyan
        self.ui.search_count.setText(str(search_count))
    
    def sorting(self, sorted_indices=None):
        data = pd.read_csv("Product Data\\products.csv")
        selected_algorithm = self.ui.dropdown_menu.currentText()
        col, ok = QInputDialog.getInt(self, "Column Selection", "Enter Column Number:")
        if not ok:
            return
        if col < 0 or col >= self.ui.tableWidget.columnCount():
            QMessageBox.warning(self, 'Error', 'Invalid column number!', QMessageBox.Ok)
            return
        selected_column = data.columns[col]
        column_data = data[selected_column]
        print(column_data)
        if selected_algorithm == "Bucket Sort":
            try:
                arr, sorted_indices = Algorithms.bucketSort(column_data, self.ui)
                sorted_data = data.iloc[sorted_indices]
                for row_idx, (_, row) in enumerate(sorted_data.iterrows()):
                    for col_idx, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.ui.tableWidget.setItem(row_idx, col_idx, item)
            except Exception as e:
                print(f'Error: {e}')
        elif selected_algorithm == "Bubble Sort":
            arr, sorted_indices = Algorithms.bubbleSort(column_data.tolist(), self.ui)
            sorted_data = data.iloc[sorted_indices]
            for row_idx, (_, row) in enumerate(sorted_data.iterrows()):
                for col_idx, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(row_idx, col_idx, item)

    def sorting_admin_condition(self):
        # Check if the current page is 'page_3' and if the active table is 'tableWidget_admin'
        if self.ui.stackedWidget.currentWidget() == self.ui.page_3 and self.ui.stackedWidget.currentWidget() == self.ui.tableWidget_admin:
            self.ui.btn_start.clicked.connect(self.sorting_admin)
        else:
            self.ui.btn_start.clicked.connect(self.sorting)
                  
    def sorting_admin(self, sorted_indices=None):
        data = pd.read_csv("Product Data\\products.csv")
        selected_algorithm = self.ui.dropdown_menu.currentText()
        col, ok = QInputDialog.getInt(self, "Column Selection", "Enter Column Number:")
        if not ok:
            return
        if col < 0 or col >= self.ui.tableWidget_admin.columnCount():
            QMessageBox.warning(self, 'Error', 'Invalid column number!', QMessageBox.Ok)
            return
        selected_column = data.columns[col]
        column_data = data[selected_column]
        print(column_data)
        if selected_algorithm == "Bucket Sort":
            try:
                arr, sorted_indices = Algorithms.bucketSort(column_data, self.ui)
                sorted_data = data.iloc[sorted_indices]
                for row_idx, (_, row) in enumerate(sorted_data.iterrows()):
                    for col_idx, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.ui.tableWidget_admin.setItem(row_idx, col_idx, item)
            except Exception as e:
                print(f'Error: {e}')
        elif selected_algorithm == "Bubble Sort":
            arr, sorted_indices = Algorithms.bubbleSort(column_data.tolist(), self.ui)
            sorted_data = data.iloc[sorted_indices]
            for row_idx, (_, row) in enumerate(sorted_data.iterrows()):
                for col_idx, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.ui.tableWidget_admin.setItem(row_idx, col_idx, item)

    def confirm_exit(self):
        reply = QMessageBox.question(self, 'Exit Confirmation', 'Are you sure you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()

    def login(self):
        username = self.ui.admin_name.text().upper()  # Convert username to uppercase
        password = self.ui.admin_password.text().upper()

        # Check if username and password are correct
        if username == "NOFIL" and password == "1242":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            self.ui.admin_name.clear()  # Clear the input fields
            self.ui.admin_password.clear()
        else:
            # Show error message if login is unsuccessful
            QMessageBox.warning(self, 'Login Failed', 'Incorrect username or password. Please try again.',
                                QMessageBox.Ok)


            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loading_screen = LoadingScreen()
    loading_screen.show()
    sys.exit(app.exec_())
