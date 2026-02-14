
import sys
import os
import datetime
import logging
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QApplication, QHeaderView
import sqlite3
from xlsxwriter import Workbook
from .database import get_db_connection
from .ui_main import ModernAppUI
from .dialogs import BookDialog, ClientDialog, UserDialog

logger = logging.getLogger(__name__)

class Library(ModernAppUI):
    
    def __init__(self):
        super().__init__()
        logger.debug("Library window setup complete.")
        
        # Connect Tab Buttons
        self.connect_signals()
        
        # Initialize UI with data
        try:
             self.refresh_all_data()
        except Exception as e:
            logger.error(f"Initialization error (non-fatal): {e}")

    def connect_signals(self):
        """Connect all button signals to their slots"""
        # Books
        self.books_add_btn.clicked.connect(self.open_add_book_dialog)
        self.books_export_btn.clicked.connect(self.export_books)
        
        # Clients
        self.clients_add_btn.clicked.connect(self.open_add_client_dialog)
        self.clients_export_btn.clicked.connect(self.export_clients)
        
        # Users
        self.users_add_btn.clicked.connect(self.open_add_user_dialog)
        # self.users_export_btn.clicked.connect(self.export_users) # If implemented
        
        # Day Operations
        self.day_ops_add_btn.clicked.connect(self.open_add_operation_dialog)
        self.day_ops_export_btn.clicked.connect(self.export_day_operations)
        
        # Sidebar Navigation
        self.dayOperationBtn.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.booksBtn.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.userBtn.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.clientBtn.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        self.settingsBtn.clicked.connect(lambda: self.tabWidget.setCurrentIndex(4))

    def refresh_all_data(self):
        self.show_books()
        self.show_clients()
        self.show_users()
        self.show_day_operations()

    # ==========================
    # Books Management
    # ==========================
    def open_add_book_dialog(self):
        # Fetch categories, authors, publishers for dropdowns
        categories = self.fetch_single_column("category", "category_name")
        authors = self.fetch_single_column("author", "author_name")
        publishers = self.fetch_single_column("publisher", "publisher_name")
        
        dialog = BookDialog(self, categories, authors, publishers)
        if dialog.exec_():
            data = dialog.get_data()
            self.add_book_to_db(data)

    def add_book_to_db(self, data):
        try:
            conn = get_db_connection(self)
            if not conn: return
            cur = conn.cursor()
            cur.execute('''
                INSERT INTO book(book_name, book_description, book_code, book_category, book_author, book_publisher, book_price) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (data['name'], data['description'], data['code'], data['category'], data['author'], data['publisher'], data['price']))
            conn.commit()
            conn.close()
            self.statusBar().showMessage('New book added successfully!')
            self.show_books()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Could not add book: {e}")

    def show_books(self):
        try:
            conn = get_db_connection(self)
            if not conn: return
            cur = conn.cursor()
            cur.execute("SELECT book_code, book_name, book_description, book_category, book_author FROM book")
            data = cur.fetchall()
            
            self.update_table(self.books_table, data, ["Code", "Name", "Description", "Category", "Author"])
            conn.close()
        except sqlite3.Error as e:
            logger.error(f"Error fetching books: {e}")

    # ==========================
    # Client Management
    # ==========================
    def open_add_client_dialog(self):
        dialog = ClientDialog(self)
        if dialog.exec_():
            data = dialog.get_data()
            self.add_client_to_db(data)
            
    def add_client_to_db(self, data):
        try:
            conn = get_db_connection(self)
            if not conn: return
            cur = conn.cursor()
            cur.execute("INSERT INTO client(clientName, clientEmail, clientNid) VALUES(?, ?, ?)", 
                       (data['name'], data['email'], data['nid']))
            conn.commit()
            conn.close()
            self.statusBar().showMessage('New client added successfully!')
            self.show_clients()
        except sqlite3.Error as e:
             QMessageBox.critical(self, "Database Error", f"Could not add client: {e}")

    def show_clients(self):
        try:
             conn = get_db_connection(self)
             if not conn: return
             cur = conn.cursor()
             cur.execute("SELECT clientNid, clientName, clientEmail FROM client")
             data = cur.fetchall()
             self.update_table(self.clients_table, data, ["ID", "Name", "Email"])
             conn.close()
        except sqlite3.Error as e:
             logger.error(f"Error fetching clients: {e}")

    # ==========================
    # User Management
    # ==========================
    def open_add_user_dialog(self):
        dialog = UserDialog(self)
        if dialog.exec_():
            data = dialog.get_data()
            self.add_user_to_db(data)
            
    def add_user_to_db(self, data):
        try:
            conn = get_db_connection(self)
            if not conn: return
            cur = conn.cursor()
            # Note: In production, hash passwords!
            cur.execute("INSERT INTO users(username, useremail, userspassword) VALUES(?, ?, ?)", 
                       (data['username'], data['email'], data['password']))
            conn.commit()
            conn.close()
            self.statusBar().showMessage('New user added successfully!')
            self.show_users()
        except sqlite3.Error as e:
             QMessageBox.critical(self, "Database Error", f"Could not add user: {e}")

    def show_users(self):
        try:
             conn = get_db_connection(self)
             if not conn: return
             cur = conn.cursor()
             cur.execute("SELECT id_users, username, useremail FROM users")
             data = cur.fetchall()
             self.update_table(self.users_table, data, ["ID", "Username", "Email"])
             conn.close()
        except sqlite3.Error as e:
             logger.error(f"Error fetching users: {e}")

    # ==========================
    # Day Operations (TODO: Full Implementation)
    # ==========================
    def open_add_operation_dialog(self):
        QMessageBox.information(self, "Info", "Day Operation Dialog implementation pending refactor.")
        
    def show_day_operations(self):
        try:
             conn = get_db_connection(self)
             if not conn: return
             cur = conn.cursor()
             cur.execute("SELECT bookname, clientName, type, fromDate, toDate FROM dayoperations")
             data = cur.fetchall()
             self.update_table(self.day_ops_table, data, ["Book", "Client", "Type", "From", "To"])
             conn.close()
        except sqlite3.Error as e:
             logger.error(f"Error fetching operations: {e}")

    # ==========================
    # Helpers
    # ==========================
    def fetch_single_column(self, table, column):
        try:
            conn = get_db_connection(self)
            if not conn: return []
            cur = conn.cursor()
            cur.execute(f"SELECT {column} FROM {table}")
            data = [item[0] for item in cur.fetchall()]
            conn.close()
            return data
        except sqlite3.Error:
            return []

    def update_table(self, table_widget, data, headers=None):
        table_widget.setRowCount(0)
        table_widget.setColumnCount(len(headers) if headers else 0)
        if headers:
            table_widget.setHorizontalHeaderLabels(headers)
            table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        if not data: return
        
        # If no headers provided, assume data length determines columns
        if not headers and len(data) > 0:
             table_widget.setColumnCount(len(data[0]))
        
        for row_idx, row_data in enumerate(data):
            table_widget.insertRow(row_idx)
            for col_idx, item in enumerate(row_data):
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

    # ==========================
    # Exports
    # ==========================
    def export_books(self):
        self._export_table("book", "allBooks.xlsx")
        
    def export_clients(self):
        self._export_table("client", "allClients.xlsx")
        
    def export_day_operations(self):
        self._export_table("dayoperations", "day_operations.xlsx")

    def _export_table(self, table_name, filename):
        try:
            conn = get_db_connection(self)
            if not conn: return
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table_name}")
            data = cur.fetchall()
            
            # Get column names
            names = [description[0] for description in cur.description]
            
            wb = Workbook(filename)
            sheet = wb.add_worksheet()
            
            for col, name in enumerate(names):
                sheet.write(0, col, name)
                
            for row_idx, row in enumerate(data):
                for col_idx, item in enumerate(row):
                    sheet.write(row_idx + 1, col_idx, str(item))
                    
            wb.close()
            conn.close()
            self.statusBar().showMessage(f'Data exported to {filename}')
            QMessageBox.information(self, "Export Successful", f"Data exported to {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to export: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Library()
    win.show()
    app.exec_()
