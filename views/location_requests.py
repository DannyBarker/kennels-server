LOCATIONS = [
    {
        "id": 1,
        "name": "ABC Building",
        "address": "123 Street"
    },
    {
        "id": 2,
        "name": "Johnny's House",
        "address": "450 Apple Blvd"
    },
    {
        "id": 3,
        "name": "NSS Building",
        "address": "2022 NSS Way"
    }
]


def get_all_locations() -> list[dict[str, any]]:
    '''
    Returns all locations
    '''
    return LOCATIONS

def get_single_location(id: int) -> dict[str, any]:
    '''
    Returns single location based off ID passed
    '''
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location) -> dict[str, any]:
    '''
    Creates a location obj and appends to locations list based off location object passed
    '''
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location