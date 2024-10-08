from typing import Optional, Dict
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self,
                 path_id: int,
                 species: str,
                 start_location: Habitat,
                 destination: Habitat,
                 duration: Optional[int] = None) -> None:
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

    def update_migration_path_details(self, **kwargs) -> None:
        """
        Update the details of the migration path using keyword arguments.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_migration_path_details(self) -> Dict:
        """
        Retrieve the details of the migration path as a dictionary.
        """
        return {
            'path_id': self.path_id,
            'species': self.species,
            'start_location': self.start_location.geographic_area,
            'destination': self.destination.geographic_area,
            'duration': self.duration
        }
