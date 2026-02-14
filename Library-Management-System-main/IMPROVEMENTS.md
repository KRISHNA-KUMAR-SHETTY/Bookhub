# Application Improvements & Usage Guide

## Summary of Changes
- **Backend**: Migrated from MySQL to **SQLite** for instant plug-and-play capability (no server setup required).
- **Security**: Fixed SQL Injection vulnerabilities in login authentication.
- **Frontend**: 
  - Redesigned with a **Modern Dark Glass Theme** (High contrast, vibrant accents).
  - Replaced legacy tab-based inputs with **Dialogs** (Add Book, Add User, etc.) for a cleaner interface.
  - Implemented responsive tables and efficient data loading.
- **Code Structure**: 
  - Refactored `src/main.py` into a proper Controller logic.
  - Created `src/dialogs.py` for modular form handling.
  - Removed dependency on `.ui` files, using pure Python UI generation for flexible styling.

## How to Run
1. Ensure you have Python installed.
2. Install dependencies (if not already):
   ```bash
   pip install PyQt5 xlsxwriter
   ```
3. Run the application:
   ```bash
   python python_distribution/run.py
   ```

## Default Login
- **Username**: `admin`
- **Password**: `admin`

## Testing
Run the included tests to verify stability:
```bash
python python_distribution/tests/test_backend.py
python python_distribution/tests/test_integration.py
```
