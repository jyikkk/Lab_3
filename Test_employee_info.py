import employee_info as ei

def get_employees_by_age_range():
    result = []
    correct_result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result = ei.get_employees_by_age_range(10, 30)
    assert(result == correct_result)


def calculate_average_salary():
    correct_result = 60166.666666666664
    assert(ei.calculate_average_salary == correct_result)


def get_employees_by_dept():
    correct_result = [
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert(ei.get_employees_by_dept("Engineering") == correct_result)