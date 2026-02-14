
import sys
import os
import logging
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from .database import get_db_connection
from .ui_login import ModernLoginUI

logger = logging.getLogger(__name__)

class LoginCls(ModernLoginUI):
    
    def __init__(self):
        super().__init__()
        logger.debug("Login window setup complete.")
        
        self.loginBtn.clicked.connect(self.handleLogin)
        self.mainWindow = None # Will be set to Library instance

    def handleLogin(self):
        try:
            self.db = get_db_connection(self)
            if not self.db:
                return # User cancelled or failed
                
            self.cur = self.db.cursor()
            
            loginUsername = self.loginUsername.text()
            loginUserPass = self.loginUserPass.text()
            
            if not loginUsername or not loginUserPass:
                self.loginError.setText('Please enter both username and password')
                return
            
            sql = "SELECT * FROM users WHERE username=? AND userspassword=?"
            self.cur.execute(sql, (loginUsername, loginUserPass))
            data = self.cur.fetchone()
            
            if data:
                # data is (id, username, email, password)
                from .main import Library 
                self.mainWindow = Library()
                self.close()
                self.mainWindow.show()
            else:
                self.loginError.setText('❌ Username or password is invalid')
            self.db.close()
            
        except sqlite3.Error as e:
            self.loginError.setText(f"Database Error: {e}")
        except Exception as e:
            self.loginError.setText(f"Error: {e}")
            import traceback
            traceback.print_exc()
