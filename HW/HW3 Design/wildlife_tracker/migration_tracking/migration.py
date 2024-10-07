from typing import Any, Optional, Dict
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
    def __init__(self,
                 migration_id: int,
                 migration_path: MigrationPath,
                 start_date: str,
                 status: str = "Scheduled",
                 current_location: Optional[Habitat] = None) -> None:
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.start_date = start_date
        self.status = status
        self.current_location = current_location or migration_path.start_location

    def update_migration_details(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def cancel_migration(self) -> None:
        self.status = "Canceled"

    def get_migration_details(self) -> Dict[str, Any]:
        return {
            'migration_id': self.migration_id,
            'migration_path_id': self.migration_path.path_id,
            'start_date': self.start_date,
            'status': self.status,
            'current_location': self.current_location.geographic_area if self.current_location else None,
            'species': self.migration_path.species,
            'duration': self.migration_path.duration,
            'start_location': self.migration_path.start_location.geographic_area,
            'destination': self.migration_path.destination.geographic_area,
        }
