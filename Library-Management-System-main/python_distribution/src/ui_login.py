"""
Modern Login UI - Built with clean PyQt5 layouts
"""

from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QFrame)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor
from PyQt5.QtCore import QPropertyAnimation, QRect


class ModernLoginUI(QMainWindow):
    """Modern, clean login interface"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Initialize the login UI"""
        self.setWindowTitle("Bookhub - Library Management System")
        self.setGeometry(100, 100, 500, 600)
        self.setMinimumSize(500, 600)
        self.setMaximumSize(600, 700)
        
        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Header section
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Content section
        content = self.create_content()
        main_layout.addWidget(content)
        
        central_widget.setLayout(main_layout)
    
    def create_header(self):
        """Create the header section with logo and title"""
        header = QFrame()
        header.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0f3460, stop:1 #16213e);
                border: none;
                border-bottom: 2px solid #e94560;
            }
        """)
        header.setFixedHeight(200)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 40, 20, 40)
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignCenter)
        
        # Title
        title = QLabel("BOOKHUB")
        title_font = QFont()
        title_font.setPointSize(32)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #e94560; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        
        # Subtitle
        subtitle = QLabel("Library Management System")
        subtitle_font = QFont()
        subtitle_font.setPointSize(12)
        subtitle.setFont(subtitle_font)
        subtitle.setStyleSheet("color: #e0e0e0;")
        subtitle.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(title)
        layout.addWidget(subtitle)
        header.setLayout(layout)
        
        return header
    
    def create_content(self):
        """Create the login form content"""
        content = QFrame()
        content.setStyleSheet("""
            QFrame {
                background: #1a1a2e;
                border: none;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        
        # Username label and input
        username_label = QLabel("Username")
        username_label.setStyleSheet("""
            color: #e0e0e0;
            font-weight: 600;
            font-size: 13px;
        """)
        
        self.loginUsername = QLineEdit()
        self.loginUsername.setPlaceholderText("Enter your username")
        self.loginUsername.setMinimumHeight(45)
        self.loginUsername.setStyleSheet("""
            QLineEdit {
                background-color: #16213e;
                color: #ffffff;
                border: 1px solid #0f3460;
                border-radius: 8px;
                padding: 12px 15px;
                font-size: 13px;
                selection-background-color: #e94560;
            }
            QLineEdit:focus {
                border: 1px solid #e94560;
                background-color: #1a1a2e;
            }
        """)
        
        # Password label and input
        password_label = QLabel("Password")
        password_label.setStyleSheet("""
            color: #e0e0e0;
            font-weight: 600;
            font-size: 13px;
        """)
        
        self.loginUserPass = QLineEdit()
        self.loginUserPass.setPlaceholderText("Enter your password")
        self.loginUserPass.setEchoMode(QLineEdit.Password)
        self.loginUserPass.setMinimumHeight(45)
        self.loginUserPass.setStyleSheet("""
            QLineEdit {
                background-color: #16213e;
                color: #ffffff;
                border: 1px solid #0f3460;
                border-radius: 8px;
                padding: 12px 15px;
                font-size: 13px;
                selection-background-color: #e94560;
            }
            QLineEdit:focus {
                border: 1px solid #e94560;
                background-color: #1a1a2e;
            }
        """)
        
        # Error message
        self.loginError = QLabel()
        self.loginError.setStyleSheet("""
            color: #e74c3c;
            font-size: 12px;
            font-weight: 600;
        """)
        self.loginError.setAlignment(Qt.AlignCenter)
        
        # Login button
        self.loginBtn = QPushButton("LOGIN")
        self.loginBtn.setMinimumHeight(50)
        self.loginBtn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.loginBtn.setCursor(Qt.PointingHandCursor)
        self.loginBtn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0f3460, stop:1 #16213e);
                color: #ffffff;
                border: 1px solid #e94560;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1a1a2e, stop:1 #0f3460);
                background-color: #e94560;
                border: 2px solid #e94560;
            }
            QPushButton:pressed {
                background-color: #0f3460;
            }
        """)
        
        # Add widgets to layout
        layout.addWidget(username_label)
        layout.addWidget(self.loginUsername)
        layout.addSpacing(10)
        layout.addWidget(password_label)
        layout.addWidget(self.loginUserPass)
        layout.addWidget(self.loginError)
        layout.addSpacing(20)
        layout.addWidget(self.loginBtn)
        layout.addStretch()
        
        content.setLayout(layout)
        return content
