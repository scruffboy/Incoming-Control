# Incoming Control

Automatic reporting on incoming inspections. Data is received from an Excel file, read, processed, and finally output as an Excel spreadsheet. Additionally, the data is written to a database.

## Workflow

**Import**: Data is read from an Excel file in table format: date, document number, supplier, warehouse.
**Analysis**: Incoming data is analyzed and converted into raw data objects.
**Creation**: Creation of ready-made objects for output to a file and writing to a database. Internal logic: selection of product group and temperature.
**Output**: The processed data is saved in a table: date, document number, supplier, product group, temperature, packaging condition, accompanying documents, driver's medical record, availability, and markings.
**Database**: The data is written to the database.

## Technology Stack

- **Program Language**: Python 3.13
- **Data Processing**: Pandas
- **Excel Engine**: Openpyxl
- **Database & ORM**: SQLAlchemy
- **Testing**: Pytest

## Local Setup & Run

- **Clone the repository**

```bash
git clone 'link'
cd Incoming-Control
```

- **Create, activate virtual environment**

```bash
# For windows powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# For Linux/macOS or Git Bash
source .venv/bin/activate
```

- **Install requirements**

```bash
pip install -r requirements.txt
```

- **Run**

```bash
python main.py
```
