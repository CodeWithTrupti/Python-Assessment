## 📋 Project Overview
This repository contains my solutions for the Python Developer Assessment, demonstrating skills in:
- Data processing with CSV files
- REST API integration
- Object-Oriented Programming
- SQL queries
- Debugging and problem-solving

## 📁 Project Structure
```
Python_Assessment/
├── data/
│   └── employees.csv          # Employee data
├── output/
│   └── employees_2023.csv     # Generated output
├── task1_data_processing.py   # CSV data analysis
├── task2_api_integration.py   # API integration with caching
├── task3_library_oops.py      # Library management system (OOP)
├── task4_sql_queries.sql      # SQL queries
├── task5_debug_fixed.py       # Debugging exercise (fixed)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/Python-Assessment.git
cd Python-Assessment
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Tasks

**Task 1: Employee Data Processing**
```bash
python task1_data_processing.py
```
- Analyzes employee data from CSV
- Calculates average salaries by department
- Finds highest-paid employees
- Filters employees who joined in 2023

**Task 2: REST API Integration**
```bash
python task2_api_integration.py
```
- Fetches posts from JSONPlaceholder API
- Implements caching mechanism
- Analyzes post data
- Creates new posts

**Task 3: Library Management System**
```bash
python task3_library_oops.py
```
- Demonstrates OOP concepts
- Manages book inventory
- Handles borrowing and returning
- Prevents duplicate entries

**Task 5: Debugging**
```bash
python task5_debug_fixed.py
```
- Fixed multiple bugs in employee analysis code
- Improved error handling
- Added proper file management

## 💡 Key Features

### Task 1: Data Processing
- CSV file reading and parsing
- Statistical calculations
- Date filtering
- Data export functionality

### Task 2: API Integration
- HTTP requests using `requests` library
- Simple caching implementation
- Error handling for API calls
- JSON data processing

### Task 3: OOP Implementation
- Class design (`Book` and `Library`)
- Encapsulation of data
- Method implementation
- State management

### Task 4: SQL Queries
- Employee data queries
- Aggregation functions
- Filtering and sorting
- Join operations

### Task 5: Debugging
- Identified and fixed type conversion issues
- Fixed file handling problems
- Corrected logic errors
- Added proper error handling

## 🛠️ Technologies Used
- Python 3.x
- requests library (for API calls)
- csv module (for data processing)
- datetime module (for date operations)
- SQL (for database queries)
