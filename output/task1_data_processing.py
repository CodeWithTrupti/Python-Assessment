import csv
from datetime import datetime


input_file = 'data/employees.csv'
output_file = 'output/employees_2023.csv'

def load_employees(file):
    
    employees = []
    
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['salary'] = float(row['salary'])
            row['join_date'] = datetime.strptime(row['join_date'], '%Y-%m-%d')
            employees.append(row)
    
    return employees


def get_total_employees(employees):
    #total_employees
    return len(employees)


def get_avg_salary_by_dept(employees):
    #avg_salary
    dept_salaries = {}
    
    for emp in employees:
        dept = emp['department']
        if dept not in dept_salaries:
            dept_salaries[dept] = []
        dept_salaries[dept].append(emp['salary'])
    
    
    avg_salaries = {}
    for dept, salaries in dept_salaries.items():
        avg_salaries[dept] = sum(salaries) / len(salaries)
    
    return avg_salaries


def get_highest_dept(avg_salaries):
    #highest avg salary
    highest = None
    highest_avg = 0
    
    for dept, avg in avg_salaries.items():
        if avg > highest_avg:
            highest_avg = avg
            highest = dept
    
    return highest


def get_highest_paid(employees):
    #employee with highest salary
    max_salary = 0
    for emp in employees:
        if emp['salary'] > max_salary:
            max_salary = emp['salary']
    
    highest_paid = []
    for emp in employees:
        if emp['salary'] == max_salary:
            highest_paid.append(emp)
    
    return highest_paid


def get_2023_employees(employees):
    
    employees_2023 = []
    for emp in employees:
        if emp['join_date'].year == 2023:
            employees_2023.append(emp)
    return employees_2023


def save_to_csv(employees, filename):
    
    if len(employees) == 0:
        print("No employees to save")
        return
    
    with open(filename, 'w', newline='') as f:
        fieldnames = employees[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for emp in employees:
            row = emp.copy()
            row['join_date'] = row['join_date'].strftime('%Y-%m-%d')
            writer.writerow(row)


def main():
    
    print("Loading employees...")
    employees = load_employees(input_file)
    
    # Total employees
    total = get_total_employees(employees)
    print(f"Total Employees: {total}")
    
    # Average salary 
    avg_salaries = get_avg_salary_by_dept(employees)
    print("\nAverage Salary by Department:")
    for dept, avg in avg_salaries.items():
        print(f"  {dept}: ${avg:.2f}")
    
    # Highest average department
    highest_dept = get_highest_dept(avg_salaries)
    print(f"\nDepartment with Highest Avg Salary: {highest_dept}")
    
    # Highest paid employees
    highest_paid = get_highest_paid(employees)
    print("\nHighest Paid Employee(s):")
    for emp in highest_paid:
        print(f"  {emp['name']} - ${emp['salary']}")
    
    # 2023 employees
    emp_2023 = get_2023_employees(employees)
    print(f"\nEmployees who joined in 2023: {len(emp_2023)}")
    
    
    save_to_csv(emp_2023, output_file)
    print(f"Saved 2023 employees to {output_file}")


if __name__ == "__main__":
    main()