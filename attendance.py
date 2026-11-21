import json
import os
from datetime import datetime

FILE_NAME = "attendance.txt"
employees = []


# 1. Load saved data
def load_data():
    global employees

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                employees = json.load(file)
        except (json.JSONDecodeError, OSError):
            employees = []
    else:
        employees = []


# 2. Save data
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


# 3. Find an employee by ID
def find_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return None


# 4. Add a new employee
def add_employee():
    name = input("Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    # Find the highest existing employee number (IDs start from E101)
    highest_id = 100
    for emp in employees:
        try:
            number = int(emp["id"][1:])
            highest_id = max(highest_id, number)
        except (ValueError, TypeError, KeyError):
            continue

    emp_id = "E" + str(highest_id + 1)

    employees.append({"id": emp_id, "name": name, "records": {}})
    save_data()

    print(f"Employee added: {emp_id} | {name}")


# 5. Mark employee attendance
def mark_attendance():
    # Read ALL inputs first so the input sequence never gets out of sync
    emp_id = input("Employee ID: ").strip().upper()
    date = input("Date (YYYY-MM-DD): ").strip()
    status = input("Status (P/A/L): ").strip().upper()

    # Validate in order: employee -> date -> status -> duplicate
    employee = find_employee(emp_id)
    if employee is None:
        print(f"Employee {emp_id} not found.")
        return

    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        if parsed_date.strftime("%Y-%m-%d") != date:
            raise ValueError
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    if status not in ["P", "A", "L"]:
        print("Invalid status. Enter P, A or L.")
        return

    if date in employee["records"]:
        print(f"Attendance for {date} is already marked.")
        return

    employee["records"][date] = status
    save_data()

    print(f"Attendance marked: {emp_id} | {date} | {status}")


# 6. Show attendance report
def show_report():
    emp_id = input("Employee ID: ").strip().upper()

    employee = find_employee(emp_id)
    if employee is None:
        print(f"Employee {emp_id} not found.")
        return

    records = list(employee["records"].values())
    present = records.count("P")
    absent = records.count("A")
    leave = records.count("L")
    total = len(records)

    # Format must match the expected output: "Aman: Present 2 | Absent 1 | Leave 1"
    print(f"{employee['name']}: Present {present} | Absent {absent} | Leave {leave}")

    if total == 0:
        print("Attendance: 0.00% (no records)")
    else:
        percentage = (present / total) * 100
        print(f"Attendance: {percentage:.2f}%")


# 7. Main menu
def main():
    load_data()

    while True:
        print("\n===== EMPLOYEE ATTENDANCE SYSTEM =====")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. View Attendance Report")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            show_report()
        elif choice == "4":
            save_data()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
