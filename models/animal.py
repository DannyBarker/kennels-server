class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, species, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.species = species
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
        
    def get_animal_name(self):
        print(self.name)
        
    def create_animal(self) -> dict[str, any]:
        return {
            "id": self.id,
            "species": self.species,
            "name": self.name,
            "locationId": self.location_id,
            "customerId": self.customer_id,
            "status": self.status
            }