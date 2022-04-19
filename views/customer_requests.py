CUSTOMERS = [
    {
        "id": 1,
        "name": "Jenny",
        "age": 46
    },
    {
        "id": 2,
        "name": "Squilliam",
        "age": 51
    },
    {
        "id": 3,
        "name": "JLo",
        "age": 18
    }
]


def get_all_customers() -> list[dict[str, any]]:
    '''
    Returns all customerss
    '''
    return CUSTOMERS

def get_single_customer(id: int) -> dict[str, any]:
    '''
    Returns single customers based off ID passed
    '''
    requested_customers = None

    for customers in CUSTOMERS:
        if customers["id"] == id:
            requested_customers = customers

    return requested_customers

def create_customer(customers) -> dict[str, any]:
    '''
    Creates a customers obj and appends to customerss list based off customers object passed
    '''
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1

    customers["id"] = new_id

    CUSTOMERS.append(customers)

    return customers