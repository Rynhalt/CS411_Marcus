from typing import Optional

class Animal:
    def __init__(self, species: str, age: Optional[int] = None, health_status: Optional[str] = None) -> None:
        self.species = species
        self.age = age
        self.health_status = health_status
