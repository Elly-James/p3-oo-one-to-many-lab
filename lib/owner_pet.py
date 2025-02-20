class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Default to None; will be set if a valid Owner is passed

        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            self.owner = owner
            owner.add_pet(self)  # Automatically add the pet to the owner's list

        Pet.all.append(self)  # Add this Pet instance to the class variable `all`

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Private attribute to store owned pets

    def pets(self):
        """Returns a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's list of pets."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of the Pet class.")
        pet.owner = self  # Assign this owner to the pet
        if pet not in self._pets:  # Avoid duplicates
            self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)

# Example usage
owner = Owner("Ben")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)

# Ensure pets are associated with the owner
assert owner.pets() == [pet1, pet2]
