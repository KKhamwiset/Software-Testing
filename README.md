# Selenium Web Automation Project

This project provides a structured framework for web automation testing using Selenium and Microsoft Edge.
## Important: 
Microsoft Edge is required to be version `145.0.3800.82`

## Prerequisites

- **Python 3.8+**
- **Microsoft Edge Browser**
- **Edge WebDriver** (The project is configured to look for the driver in `automation/resources/edgedriver_win64/msedgedriver.exe`)

## Initial Setup

1. **Clone the repository** and navigate to the project root.
2. **Create a virtual environment**:
   ```powershell
   python -m venv env_selenium
   ```
3. **Activate the virtual environment**:
   - Windows: `.\env_selenium\Scripts\activate`
   - Linux/Mac: `source env_selenium/bin/activate`
4. **Install the project in editable mode**:
   ```powershell
   pip install -e .
   ```
   *Note: This command installs all required dependencies (Selenium, python-dotenv) and registers the `automation` package.*

## Configuration

Create a `.env` file in the project root with the following variables:

```env
url=https://your-testing-site.com/
admin_username=your_username
admin_password=your_password
```

## Running Tests

Execute all tests from the root directory using the main runner:

```powershell
python main.py
```

## Project Structure

- `main.py`: The entry point for executing test cases.
- `automation/`: The core package containing resources and test logic.
  - `resources/`: Contains driver initialization logic and driver binaries.
  - `testers/`: Contains individual test functions (e.g., `fr1_test.py`, `fr2_test.py`).
- `setup.py`: Configuration for package installation.
