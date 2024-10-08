from typing import Any, List, Optional, Dict
from wildlife_tracker.animal_management.animal import Animal

class Habitat:
    def __init__(self,
                 habitat_id: int,
                 geographic_area: str,
                 size: int,
                 environment_type: str,
                 animals: Optional[List[Animal]] = None) -> None:
        self.habitat_id = habitat_id
        self.geographic_area = geographic_area
        self.size = size
        self.environment_type = environment_type
        self.animals: List[Animal] = animals or []

    def update_habitat_details(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def assign_animals_to_habitat(self, animals: List[Animal]) -> None:
        self.animals.extend(animals)

    def get_animals_in_habitat(self) -> List[Animal]:
        return self.animals

    def get_habitat_details(self) -> Dict:
        return {
            'habitat_id': self.habitat_id,
            'geographic_area': self.geographic_area,
            'size': self.size,
            'environment_type': self.environment_type,
            'animals': [animal.species for animal in self.animals]
        }
