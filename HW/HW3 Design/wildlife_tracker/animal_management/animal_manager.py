from typing import Optional, Dict, Any
from wildlife_tracker.animal_management.animal import Animal

class AnimalManager:
    def __init__(self) -> None:
        self.animals: Dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        return self.animals.get(animal_id)

    def register_animal(self, animal: Animal) -> None:
        new_id = len(self.animals) + 1
        self.animals[new_id] = animal

    def remove_animal(self, animal_id: int) -> None:
        if animal_id in self.animals:
            del self.animals[animal_id]

    def get_animal_details(self, animal_id: int) -> Optional[Dict[str, Any]]:
        animal = self.get_animal_by_id(animal_id)
        if animal:
            return {
                'id': animal_id,
                'species': animal.species,
                'age': animal.age,
                'health_status': animal.health_status
            }
        return None

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        animal = self.get_animal_by_id(animal_id)
        if animal:
            for key, value in kwargs.items():
                if hasattr(animal, key):
                    setattr(animal, key, value)
