
"""
Modern stylesheet for the Library Management System
Provides contemporary design with Dark Glassmorphism aesthetics
"""

MODERN_STYLESHEET = """
/* Global Styling - Dark Theme */
QMainWindow, QWidget {
    background-color: #1a1a2e;
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
}

QDialog {
    background-color: #1a1a2e;
}

/* Tab Widget */
QTabWidget::pane {
    border: 1px solid #16213e;
    background-color: #16213e;
    border-radius: 8px;
    margin-top: -1px; 
}

QTabBar::tab {
    background-color: #0f3460;
    color: #a0a0a0;
    padding: 10px 25px;
    margin-right: 4px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    font-weight: bold;
    font-size: 13px;
    border: 1px solid #16213e;
}

QTabBar::tab:selected {
    background-color: #e94560;
    color: #ffffff;
    border-bottom: 2px solid #e94560;
}

QTabBar::tab:hover {
    background-color: #1f4068;
    color: #ffffff;
}

/* Push Buttons - Gradient & Shadow */
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0f3460, stop:1 #16213e);
    color: #ffffff;
    border: 1px solid #0f3460;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: 600;
    font-size: 13px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1a1a2e, stop:1 #0f3460);
    border: 1px solid #e94560;
}

QPushButton:pressed {
    background-color: #0f3460;
    border: 1px solid #e94560;
}

/* Special Button Variants */
QPushButton[objectName$="_add_btn"] {
    background-color: #e94560;
    border: none;
}
QPushButton[objectName$="_add_btn"]:hover {
    background-color: #ff2e63;
}

QPushButton[objectName$="_export_btn"] {
    background-color: #0f3460;
    border: 1px solid #e94560;
}


/* Input Fields */
QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QComboBox {
    background-color: #16213e;
    color: #ffffff;
    border: 1px solid #0f3460;
    border-radius: 6px;
    padding: 8px;
    font-size: 13px;
    selection-background-color: #e94560;
}

QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
    border: 1px solid #e94560;
    background-color: #1a1a2e;
}

/* Combo Box */
QComboBox::drop-down {
    border: none;
    width: 20px;
}
QComboBox QAbstractItemView {
    background-color: #16213e;
    color: #ffffff;
    selection-background-color: #e94560;
}


/* Tables - Data Grid */
QTableWidget {
    background-color: #16213e;
    gridline-color: #0f3460;
    border: 1px solid #0f3460;
    border-radius: 8px;
    color: #e0e0e0;
    font-size: 13px;
    selection-background-color: #e94560;
    selection-color: #ffffff;
}

QHeaderView::section {
    background-color: #0f3460;
    color: #ffffff;
    padding: 12px;
    border: none;
    font-weight: bold;
    font-size: 13px;
}

QTableWidget::item {
    padding: 8px;
    border-bottom: 1px solid #0f3460;
}

QTableWidget::item:selected {
    background-color: #e94560;
    color: #ffffff;
}

/* Sidebar Specifics */
QFrame#sidebar {
    background-color: #16213e; /* Dark Blue */
    border-right: 1px solid #0f3460;
}

QLabel#header_logo {
    color: #e94560; /* Accent Red/Pink */
    font-size: 18px;
    font-weight: bold;
    padding: 20px;
    border-bottom: 2px solid #0f3460;
}

/* Scroll Bars */
QScrollBar:vertical {
    background-color: #1a1a2e;
    width: 10px;
    margin: 0px; 
}
QScrollBar::handle:vertical {
    background-color: #0f3460;
    border-radius: 5px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background-color: #e94560;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
}
"""

def apply_stylesheet(app):
    """
    Apply the modern stylesheet to the entire application.
    Args:
        app: QApplication instance
    """
    app.setStyle('Fusion')
    app.setStyleSheet(MODERN_STYLESHEET)


def apply_stylesheet_to_widget(widget):
    """
    Apply the modern stylesheet to a specific widget.
    Args:
        widget: QWidget or QMainWindow instance
    """
    widget.setStyleSheet(MODERN_STYLESHEET)
