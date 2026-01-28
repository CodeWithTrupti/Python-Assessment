import csv
from datetime import datetime
import os


INPUT_FILE = "data/employees.csv"


def read_employees(file_path):
    employees = []

    if not os.path.exists(file_path):
        print("Employee file not found.")
        return employees

    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row["salary"] = float(row["salary"])
                    employees.append(row)
                except ValueError:
                    print(f"Invalid salary for {row.get('name', 'Unknown')}")
    except Exception as e:
        print("Error while reading file:", e)

    return employees


def average_salary_by_department(employees):
    dept_salary = {}
    dept_count = {}

    for emp in employees:
        dept = emp["department"]

        if dept not in dept_salary:
            dept_salary[dept] = 0
            dept_count[dept] = 0

        dept_salary[dept] += emp["salary"]
        dept_count[dept] += 1

    avg_salary = {}
    for dept in dept_salary:
        if dept_count[dept] > 0:
            avg_salary[dept] = dept_salary[dept] / dept_count[dept]

    return avg_salary


def employees_joined_2023(employees):
    joined_2023 = []

    for emp in employees:
        try:
            join_date = datetime.strptime(emp["join_date"], "%Y-%m-%d")
            if join_date.year == 2023:
                joined_2023.append(emp)
        except ValueError:
            print(f"Invalid join date for {emp.get('name', 'Unknown')}")

    return joined_2023


def main():
    employees = read_employees(INPUT_FILE)

    if not employees:
        print("No employee data available.")
        return

    print("Total Employees:", len(employees))

    avg_salary = average_salary_by_department(employees)
    print("\nAverage Salary by Department:")
    for dept, salary in avg_salary.items():
        print(f"{dept}: {salary:.2f}")

    joined_2023 = employees_joined_2023(employees)
    print(f"\nEmployees joined in 2023: {len(joined_2023)}")

    for emp in joined_2023:
        print(f"- {emp['name']} ({emp['department']})")


if __name__ == "__main__":
    main()
