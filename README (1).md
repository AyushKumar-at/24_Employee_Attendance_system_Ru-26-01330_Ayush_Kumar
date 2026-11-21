# Employee Attendance System

**PS No. 24** | Rungta International Skills University
School of Computer Science and Engineering | B.Tech Computer Science and Engineering, First Semester

## Overview

A console application written in Python 3 that lets you add employees, mark their daily attendance as Present, Absent or Leave, and view an attendance report for each employee. All data is saved to a file (`attendance.txt`) and loaded again when the program starts.

**Concepts used:** Dictionaries, Lists, Conditions, File Handling

## Features

- Add an employee with an auto-generated ID (starting from `E101`)
- Mark attendance for many dates in one session
- Validate the employee ID, the date format (`YYYY-MM-DD`) and the status
- Block duplicate attendance for the same date
- View a report with Present, Absent and Leave counts and the attendance percentage
- Save data to `attendance.txt` after every change and load it at start-up

## Files

| File | Purpose |
|---|---|
| `attendance_system.py` | The main program |
| `run_tests.py` | Runs the 4 test cases automatically |
| `attendance.txt` | Data file, created automatically (JSON format) |

## How to Run

Requires Python 3.

```
python attendance_system.py
```

## Menu

```
1. Add Employee
2. Mark Attendance
3. View Attendance Report
4. Exit
```

### 1. Add Employee
Asks for a name and creates the next employee ID (E101, E102, ...).

### 2. Mark Attendance
1. Enter the Employee ID once.
2. Enter a date (`YYYY-MM-DD`) and then a status for each entry.
3. Press **Enter on a blank date** to finish and return to the menu.

Status codes: `P` = Present, `A` = Absent, `L` = Leave.

### 3. View Attendance Report
Enter the Employee ID to see the counts and the attendance percentage.

Attendance % = Present days / Marked days x 100

## Data Structure

Each employee is a dictionary stored inside a list. The `records` dictionary maps each date to a status.

```python
employees = [
    {
        "id": "E101",
        "name": "Aman",
        "records": {
            "2026-08-01": "P",
            "2026-08-02": "P",
            "2026-08-03": "A",
            "2026-08-04": "L"
        }
    }
]
```

## Messages

| Situation | Message |
|---|---|
| Employee added | `Employee added: E101 \| Aman` |
| Unknown employee ID | `Employee E999 not found.` |
| Wrong date format | `Invalid date. Use YYYY-MM-DD.` |
| Wrong status | `Invalid status. Enter P, A or L.` |
| Date already marked | `Attendance for 2026-08-02 is already marked.` |
| Employee with no records | `Attendance: 0.00% (no records)` |

## Test Cases

### Test Case 1: Normal Input
- Menu option 1, Name: `Aman`
- Output: `Employee added: E101 | Aman`

### Test Case 2: Boundary / Minimum Input
- Employee E101 has no attendance records, menu option 3 for `E101`
- Output: `Aman: Present 0 | Absent 0 | Leave 0` and `Attendance: 0.00% (no records)`

### Test Case 3: Invalid Input
- (a) Mark `E999` gives `Employee E999 not found.`
- (b) Mark `E101`, date `2026-13-45` gives `Invalid date. Use YYYY-MM-DD.`
- (c) Mark `E101`, date `2026-08-01`, status `X` gives `Invalid status. Enter P, A or L.`

### Test Case 4: Different Valid Scenario
Input for Employee E101 (Aman):

```
2
E101
2026-08-01   P
2026-08-02   P
2026-08-03   A
2026-08-04   L
2026-08-02   P
(press Enter)
3
E101
```

Output:

```
Attendance for 2026-08-02 is already marked.
Aman: Present 2 | Absent 1 | Leave 1
Attendance: 50.00%
```

### Running the test cases automatically

```
python run_tests.py
```

The script overwrites `attendance.txt` before each test case, types the inputs, and prints PASS or FAIL for every expected line. **It erases the existing data in `attendance.txt`, so run it in a test folder.**

## Notes

- Delete `attendance.txt` before testing by hand. If it already contains E101, a new employee will get the ID E102.
- Employee IDs and status codes are not case-sensitive (`e101` and `p` are accepted).
- Dates are checked against the real calendar, so `2026-02-30` is rejected.
