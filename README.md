# Incoming Control

Automatic reporting on incoming inspections. Data is received from an Excel file, read, processed, and finally output as an Excel spreadsheet. Additionally, the data is written to a database.

## Project Structure

```
Incoming-Control/
├── main.py              # entry point
├── README.md            # project documentation
├── requirements.txt     # dependencies
├── LICENSE              # MIT license
├── data/                # data directory
│   ├── raw/             # input Excel files
│   ├── processed/       # output Excel files
│   ├── references/      # suppliers.json reference data
│   └── db/              # SQLite database
├── logs/                # log files
├── tests/               # test suite
│   ├── conftest.py      # pytest fixtures
│   └── integration/     # integration tests
│       ├── test_analyzer.py
│       ├── test_creator.py
│       ├── test_load_json.py
│       └── test_reader.py
└── src/
    ├── core/
    │   ├── reader.py    # Excel file reading
    │   ├── analyzer.py  # data validation & transformation
    │   ├── creator.py   # output object creation
    │   └── writer.py    # Excel export
    ├── db/
    │   ├── connection.py # database engine & session
    │   ├── db_models.py  # SQLAlchemy models
    │   └── repository.py # database operations
    ├── models/
    │   ├── load_data.py  # raw data dataclass
    │   └── output_data.py # processed data dataclass
    ├── tools/
    │   ├── bootstrap.py  # directory initialization
    │   ├── cli_handler.py # CLI argument parsing
    │   └── logger.py     # logging setup
    └── utils/
        ├── config.py     # configuration
        └── helper.py     # utility functions
```
        
## Workflow

- **Import**: Data is read from an Excel file in table format: date, document number, supplier, warehouse.
- **Analysis**: Incoming data is analyzed and converted into raw data objects.
- **Creation**: Creation of ready-made objects for output to a file and writing to a database. Internal logic: selection of product group and temperature.
- **Output**: The processed data is saved in a table: date, document number, supplier, product group, temperature, packaging condition, accompanying documents, driver's medical record, availability, and markings.
- **Database**: The data is written to the database.

## Technology Stack

- **Program Language**: Python 3.13
- **Data Processing**: Pandas
- **Excel Engine**: Openpyxl
- **Database & ORM**: SQLAlchemy
- **Testing**: Pytest

## Local Setup & Run

- **Clone the repository**

```bash
git clone https://github.com/scruffboy/Incoming-Control.git
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
python main.py path/to/your_file.xlsx
```

---

# Входящий контроль

Автоматическая отчетность по входящим проверкам. Данные поступают из файла Excel, считываются, обрабатываются и, наконец, выводятся в виде электронной таблицы Excel. Кроме того, данные записываются в базу данных.

## Структура проекта

```
Incoming-Control/
├── main.py # точка входа
├── README.md # документация проекта
├── requirements.txt # зависимости
├── LICENSE # лицензия MIT
├── data/ # каталог данных
│ ├── raw/ # входные файлы Excel
│ ├── processed/ # выходные файлы Excel
│ ├── references/ # справочные данные suppliers.json
│ └── db/ # база данных SQLite
├── logs/ # файлы журналов
├── tests/ # набор тестов
│ ├── conftest.py # pytest фикстуры
│ └── integration/ # интеграционные тесты
│ ├── test_analyzer.py
│ ├── test_creator.py
│ ├── test_load_json.py
│ └── test_reader.py
└── src/

├── core/
│ ├── reader.py # чтение файла Excel

│ ├── analyzer.py # проверка и преобразование данных

│ ├── creator.py # создание выходного объекта

│ └── writer.py # экспорт в Excel

├── db/

│ ├── connection.py # механизм базы данных и сессии

│ ├── db_models.py # модели SQLAlchemy

│ └── repository.py # операции с базой данных

├── models/

│ ├── load_data.py # класс данных необработанных данных

│ └── output_data.py # класс данных обработанных данных

├── tools/

│ ├── bootstrap.py # инициализация каталога

│ ├── cli_handler.py # разбор аргументов CLI

│ └── logger.py # настройка логирования

└── utils/

├── config.py # конфигурация
└── helper.py # вспомогательные функции
```

## Рабочий процесс

- **Импорт**: Данные считываются из файла Excel в табличном формате: дата, номер документа, поставщик, склад.

- **Анализ**: Входящие данные анализируются и преобразуются в объекты исходных данных.

- **Создание**: Создание готовых объектов для вывода в файл и записи в базу данных. Внутренняя логика: выбор группы товаров и температуры.

- **Вывод**: Обработанные данные сохраняются в таблице: дата, номер документа, поставщик, группа товаров, температура, состояние упаковки, сопроводительные документы, медицинская карта водителя, наличие и маркировка.

- **База данных**: Данные записываются в базу данных.

## Технологический стек

- **Язык программирования**: Python 3.13
- **Обработка данных**: Pandas
- **Движок Excel**: Openpyxl
- **База данных и ORM**: SQLAlchemy
- **Тестирование**: Pytest

## Локальная настройка и запуск

- **Клонируйте репозиторий**

```bash
git clone https://github.com/scruffboy/Incoming-Control.git
cd Incoming-Control
```

- **Создайте и активируйте виртуальное окружение**

```bash
# Для Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Для Linux/macOS или Git Bash
source .venv/bin/activate
```

- **Установите необходимые зависимости**

```bash
pip install -r requirements.txt
```

- **Запуск**

```bash
python main.py path/to/your_file.xlsx
```
