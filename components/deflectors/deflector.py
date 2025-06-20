import json
from components.base_component import ShipComponent

class Deflector(ShipComponent):
    def __init__(self, power_draw, deflection_rating, sensor_boost, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.deflection_rating = deflection_rating
        self.sensor_boost = sensor_boost

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            deflection_rating=data["deflection_rating"],
            sensor_boost=data["sensor_boost"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "deflection_rating", "sensor_boost"]}
        )

# Loader utility
def load_deflectors_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [Deflector.from_dict(entry) for entry in data] 