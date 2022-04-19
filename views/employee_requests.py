EMPLOYEES = [
    {
        "id": 1,
        "name": "Casey",
        "age": 25
    },
    {
        "id": 2,
        "name": "Johnny",
        "age": 31
    },
    {
        "id": 3,
        "name": "Stacey",
        "age": 23
    }
]


def get_all_employees() -> list[dict[str, any]]:
    '''
    Returns all employees
    '''
    return EMPLOYEES

def get_single_employee(id: int) -> dict[str, any]:
    '''
    Returns single employee based off ID passed
    '''
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee) -> dict[str, any]:
    '''
    Creates a employee obj and appends to employees list based off employee object passed
    '''
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee