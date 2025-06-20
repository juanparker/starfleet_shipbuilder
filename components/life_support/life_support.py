import json
from components.base_component import ShipComponent

class LifeSupport(ShipComponent):
    def __init__(self, power_draw, crew_supported, redundancy_rating, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.crew_supported = crew_supported
        self.redundancy_rating = redundancy_rating

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            crew_supported=data["crew_supported"],
            redundancy_rating=data["redundancy_rating"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "crew_supported", "redundancy_rating"]}
        )

# Loader utility
def load_life_support_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [LifeSupport.from_dict(entry) for entry in data] 