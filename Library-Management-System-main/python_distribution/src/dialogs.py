
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QTextEdit, QComboBox, QPushButton, 
                             QFormLayout, QMessageBox, QDoubleSpinBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class BaseDialog(QDialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
            }
            QLabel {
                font-weight: 600;
                color: #2c3e50;
            }
            QLineEdit, QTextEdit, QComboBox, QDoubleSpinBox {
                padding: 8px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                background-color: #f9f9f9;
            }
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
                border: 1px solid #3498db;
                background-color: #ffffff;
            }
            QPushButton {
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: 600;
            }
        """)
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.form_layout.setSpacing(15)
        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)

    def add_buttons(self, save_callback):
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.setStyleSheet("background-color: #27ae60; color: white; border: none;")
        save_btn.clicked.connect(save_callback)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setStyleSheet("background-color: #e74c3c; color: white; border: none;")
        cancel_btn.clicked.connect(self.reject)
        
        btn_layout.addStretch()
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(save_btn)
        self.layout.addLayout(btn_layout)

class BookDialog(BaseDialog):
    def __init__(self, parent=None, categories=[], authors=[], publishers=[], book_data=None):
        title = "Edit Book" if book_data else "Add New Book"
        super().__init__(title, parent)
        self.categories = categories
        self.authors = authors
        self.publishers = publishers
        self.book_data = book_data
        self.setup_ui()

    def setup_ui(self):
        self.title_input = QLineEdit()
        self.code_input = QLineEdit()
        self.category_input = QComboBox()
        self.category_input.addItems(self.categories)
        self.author_input = QComboBox()
        self.author_input.addItems(self.authors)
        self.publisher_input = QComboBox()
        self.publisher_input.addItems(self.publishers)
        self.price_input = QDoubleSpinBox()
        self.price_input.setMaximum(100000)
        self.desc_input = QTextEdit()
        self.desc_input.setMaximumHeight(100)

        self.form_layout.addRow("Book Title:", self.title_input)
        self.form_layout.addRow("Book Code:", self.code_input)
        self.form_layout.addRow("Category:", self.category_input)
        self.form_layout.addRow("Author:", self.author_input)
        self.form_layout.addRow("Publisher:", self.publisher_input)
        self.form_layout.addRow("Price:", self.price_input)
        self.form_layout.addRow("Description:", self.desc_input)

        if self.book_data:
            # Populate fields
            self.title_input.setText(self.book_data.get('name', ''))
            self.code_input.setText(self.book_data.get('code', ''))
            self.price_input.setValue(float(self.book_data.get('price', 0)))
            self.desc_input.setText(self.book_data.get('description', ''))
            
            # Set combos
            index = self.category_input.findText(self.book_data.get('category', ''))
            if index >= 0: self.category_input.setCurrentIndex(index)
            
            index = self.author_input.findText(self.book_data.get('author', ''))
            if index >= 0: self.author_input.setCurrentIndex(index)
            
            index = self.publisher_input.findText(self.book_data.get('publisher', ''))
            if index >= 0: self.publisher_input.setCurrentIndex(index)

        self.add_buttons(self.validate_and_accept)

    def validate_and_accept(self):
        if not self.title_input.text() or not self.code_input.text():
            QMessageBox.warning(self, "Validation Error", "Title and Code are required.")
            return
        self.accept()

    def get_data(self):
        return {
            'name': self.title_input.text(),
            'code': self.code_input.text(),
            'category': self.category_input.currentText(),
            'author': self.author_input.currentText(),
            'publisher': self.publisher_input.currentText(),
            'price': self.price_input.value(),
            'description': self.desc_input.toPlainText()
        }

class UserDialog(BaseDialog):
    def __init__(self, parent=None, user_data=None):
        title = "Edit User" if user_data else "Add New User"
        super().__init__(title, parent)
        self.user_data = user_data
        self.setup_ui()
    
    def setup_ui(self):
        self.username_input = QLineEdit()
        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.confirm_pass_input = QLineEdit()
        self.confirm_pass_input.setEchoMode(QLineEdit.Password)
        
        self.form_layout.addRow("Username:", self.username_input)
        self.form_layout.addRow("Email:", self.email_input)
        self.form_layout.addRow("Password:", self.password_input)
        self.form_layout.addRow("Confirm Password:", self.confirm_pass_input)
        
        if self.user_data:
            self.username_input.setText(self.user_data.get('username', ''))
            self.email_input.setText(self.user_data.get('email', ''))
            # Don't pre-fill password for security, or maybe allow changing it
            self.password_input.setPlaceholderText("Leave blank to keep current")
            self.confirm_pass_input.setPlaceholderText("Leave blank to keep current")
            
        self.add_buttons(self.validate_and_accept)
        
    def validate_and_accept(self):
        if not self.username_input.text() or not self.email_input.text():
             QMessageBox.warning(self, "Validation Error", "Username and Email are required.")
             return
             
        if not self.user_data and not self.password_input.text():
             QMessageBox.warning(self, "Validation Error", "Password is required for new users.")
             return
             
        if self.password_input.text() != self.confirm_pass_input.text():
            QMessageBox.warning(self, "Validation Error", "Passwords do not match.")
            return
            
        self.accept()
        
    def get_data(self):
        return {
            'username': self.username_input.text(),
            'email': self.email_input.text(),
            'password': self.password_input.text()
        }

class ClientDialog(BaseDialog):
    def __init__(self, parent=None, client_data=None):
        title = "Edit Client" if client_data else "Add New Client"
        super().__init__(title, parent)
        self.client_data = client_data
        self.setup_ui()
        
    def setup_ui(self):
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.nid_input = QLineEdit()
        
        self.form_layout.addRow("Client Name:", self.name_input)
        self.form_layout.addRow("Email:", self.email_input)
        self.form_layout.addRow("National ID:", self.nid_input)
        
        if self.client_data:
            self.name_input.setText(self.client_data.get('name', ''))
            self.email_input.setText(self.client_data.get('email', ''))
            self.nid_input.setText(self.client_data.get('nid', ''))
            
        self.add_buttons(self.validate_and_accept)
        
    def validate_and_accept(self):
        if not self.name_input.text() or not self.nid_input.text():
            QMessageBox.warning(self, "Validation Error", "Name and ID are required.")
            return
        self.accept()
        
    def get_data(self):
        return {
            'name': self.name_input.text(),
            'email': self.email_input.text(),
            'nid': self.nid_input.text()
        }
