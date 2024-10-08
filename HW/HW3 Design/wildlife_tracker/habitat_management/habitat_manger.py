from typing import Optional, List, Dict
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:
    def __init__(self) -> None:
        self.habitats: Dict[int, Habitat] = {}

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        new_habitat = Habitat(habitat_id, geographic_area, size, environment_type)
        self.habitats[habitat_id] = new_habitat
        return new_habitat

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        return self.habitats.get(habitat_id)

    def get_habitat_details(self, habitat_id: int) -> Optional[Dict]:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            return {
                'habitat_id': habitat.habitat_id,
                'geographic_area': habitat.geographic_area,
                'size': habitat.size,
                'environment_type': habitat.environment_type,
                'animals': [animal.species for animal in habitat.get_animals_in_habitat()]
            }
        return None

    def get_habitats_by_geographic_area(self, geographic_area: str) -> List[Habitat]:
        return [habitat for habitat in self.habitats.values() if habitat.geographic_area == geographic_area]

    def assign_animals_to_habitat(self, habitat_id: int, animals: List[Animal]) -> None:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            habitat.assign_animals_to_habitat(animals)
        else:
            raise ValueError(f"Habitat with ID {habitat_id} not found.")
