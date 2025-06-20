import json
from components.base_component import ShipComponent

class ImpulseEngine(ShipComponent):
    def __init__(self, power_draw, sublight_speed, maneuverability, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.sublight_speed = sublight_speed
        self.maneuverability = maneuverability

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            sublight_speed=data["sublight_speed"],
            maneuverability=data["maneuverability"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "sublight_speed", "maneuverability"]}
        )

# Loader utility
def load_impulse_engines_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [ImpulseEngine.from_dict(entry) for entry in data] 