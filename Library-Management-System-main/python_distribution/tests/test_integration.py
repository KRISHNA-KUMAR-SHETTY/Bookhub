
import unittest
import sys
import os
from PyQt5.QtWidgets import QApplication

# Add python_distribution to the path (parent of tests)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.main import Library

# We need a QApplication instance to create widgets
app = QApplication(sys.argv)

class TestIntegration(unittest.TestCase):
    def test_library_window_creation(self):
        """Test that the main Library window can be created."""
        try:
            window = Library()
            self.assertIsNotNone(window)
            self.assertEqual(window.windowTitle(), "Bookhub - Library Management System")
            # Check if tabs are created
            self.assertEqual(window.tabWidget.count(), 5)
        except Exception as e:
            self.fail(f"Could not create Library window: {e}")

if __name__ == '__main__':
    unittest.main()
