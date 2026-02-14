"""
Modern Application UI - Clean, stylish layout
"""

from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QTabWidget, QPushButton, QLabel, QFrame, QSplitter,
                             QTableWidget, QTableWidgetItem, QLineEdit, QComboBox,
                             QSpinBox, QMessageBox, QFileDialog, QDialog)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtSvg import QSvgWidget


class ModernAppUI(QMainWindow):
    """Modern, clean application interface"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize the main application UI"""
        self.setWindowTitle("Bookhub - Library Management System")
        self.setGeometry(100, 100, 1400, 900)
        self.setMinimumSize(1200, 800)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Main layout with sidebar and content
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # Main content area
        content = self.create_content_area()
        main_layout.addWidget(content, 1)
        
        main_widget.setLayout(main_layout)
        
        # Set window style
        self.setStyleSheet("background-color: #f5f7fa;")
    
    def create_sidebar(self):
        """Create the left sidebar with navigation"""
        sidebar = QFrame()
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border: none;
            }
        """)
        sidebar.setFixedWidth(220)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Logo/Header
        header = QLabel("BOOKHUB")
        header_font = QFont()
        header_font.setPointSize(14)
        header_font.setBold(True)
        header.setFont(header_font)
        header.setStyleSheet("""
            QLabel {
                color: #ffffff;
                padding: 20px;
                border-bottom: 2px solid #34495e;
            }
        """)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Navigation buttons
        buttons_data = [
            ("📅 Day Operations", "dayOperationBtn"),
            ("📚 Books", "booksBtn"),
            ("👤 Users", "userBtn"),
            ("👥 Clients", "clientBtn"),
            ("⚙️ Settings", "settingsBtn"),
        ]
        
        for label, name in buttons_data:
            btn = QPushButton(label)
            btn.setObjectName(name)
            btn.setMinimumHeight(50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #bdc3c7;
                    border: none;
                    border-left: 4px solid transparent;
                    text-align: left;
                    padding-left: 20px;
                    font-size: 12px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: #34495e;
                    color: #3498db;
                    border-left: 4px solid #3498db;
                }
                QPushButton:pressed {
                    background-color: #1a252f;
                    color: #ffffff;
                }
            """)
            layout.addWidget(btn)
            setattr(self, name, btn)

        
        layout.addStretch()
        
        # Footer
        footer = QLabel("v1.0.0")
        footer.setStyleSheet("""
            QLabel {
                color: #7f8c8d;
                padding: 15px;
                text-align: center;
                border-top: 1px solid #34495e;
                font-size: 10px;
            }
        """)
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer)
        
        sidebar.setLayout(layout)
        return sidebar
    
    def create_content_area(self):
        """Create the main content area"""
        content = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Top bar with title and search
        top_bar = self.create_top_bar()
        layout.addWidget(top_bar)
        
        # Tab widget for different sections
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #e1e8ed;
                background-color: #ffffff;
            }
        """)
        
        # Create tab pages
        self.day_operations_tab = self.create_tab_content("Day Operations", "day_ops")
        self.books_tab = self.create_tab_content("Books Management", "books")
        self.users_tab = self.create_tab_content("User Management", "users")
        self.clients_tab = self.create_tab_content("Client Management", "clients")
        self.settings_tab = self.create_tab_content("Settings", "settings")
        
        self.tabWidget.addTab(self.day_operations_tab, "📅 Day Operations")
        self.tabWidget.addTab(self.books_tab, "📚 Books")
        self.tabWidget.addTab(self.users_tab, "👤 Users")
        self.tabWidget.addTab(self.clients_tab, "👥 Clients")
        self.tabWidget.addTab(self.settings_tab, "⚙️ Settings")
        
        layout.addWidget(self.tabWidget)
        content.setLayout(layout)
        
        return content
    
    def create_top_bar(self):
        """Create the top bar with filters and options"""
        bar = QFrame()
        bar.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 1px solid #ecf0f1;
                border-radius: 8px;
            }
        """)
        bar.setFixedHeight(60)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(15)
        
        # Title label
        title = QLabel("Welcome to Bookhub Library Management System")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #2c3e50;")
        
        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search...")
        self.search_box.setMaximumWidth(200)
        self.search_box.setStyleSheet("""
            QLineEdit {
                background-color: #f5f7fa;
                color: #2c3e50;
                border: 1px solid #ecf0f1;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        
        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(self.search_box)
        
        bar.setLayout(layout)
        return bar
    
    def create_tab_content(self, title, name_prefix):
        """Create a clean tab content area"""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Tab header
        header = QFrame()
        header.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border: 1px solid #ecf0f1;
                border-radius: 8px;
            }
        """)
        header.setFixedHeight(70)
        
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(20, 15, 20, 15)
        
        tab_title = QLabel(title)
        tab_title_font = QFont()
        tab_title_font.setPointSize(14)
        tab_title_font.setBold(True)
        tab_title.setFont(tab_title_font)
        tab_title.setStyleSheet("color: #2c3e50; border: none;")
        
        # Action buttons
        add_btn = QPushButton("➕ Add New")
        add_btn.setObjectName(f"{name_prefix}_add_btn")
        add_btn.setMinimumWidth(120)
        add_btn.setCursor(Qt.PointingHandCursor)
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 600;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #219150;
            }
        """)
        
        export_btn = QPushButton("📊 Export")
        export_btn.setObjectName(f"{name_prefix}_export_btn")
        export_btn.setMinimumWidth(100)
        export_btn.setCursor(Qt.PointingHandCursor)
        export_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 600;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #5dade2;
            }
            QPushButton:pressed {
                background-color: #2980b9;
            }
        """)
        
        header_layout.addWidget(tab_title)
        header_layout.addStretch()
        header_layout.addWidget(add_btn)
        header_layout.addWidget(export_btn)
        header.setLayout(header_layout)
        
        layout.addWidget(header)
        
        # Table area
        table = QTableWidget()
        table.setObjectName(f"{name_prefix}_table")
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["ID", "Name", "Description", "Category", "Action"])
        table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                gridline-color: #ecf0f1;
                border: 1px solid #ecf0f1;
                border-radius: 8px;
                selection-background-color: #d6eaf8;
                selection-color: #2c3e50;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: #ffffff;
                padding: 10px;
                border: none;
                font-weight: 600;
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        
        layout.addWidget(table)
        tab.setLayout(layout)
        
        # Store references for controller access
        setattr(self, f"{name_prefix}_add_btn", add_btn)
        setattr(self, f"{name_prefix}_export_btn", export_btn)
        setattr(self, f"{name_prefix}_table", table)
        
        return tab
    
    def setup_navigation(self):
        """Setup navigation button connections"""
        # These will be connected in the main.py file
        pass
