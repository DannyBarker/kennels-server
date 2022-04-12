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
    return LOCATIONS

# Function with a single parameter
def get_single_location(id: int) -> dict[str, any]:
    requested_location = None
    
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location