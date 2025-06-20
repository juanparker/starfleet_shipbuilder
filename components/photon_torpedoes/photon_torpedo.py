import json
from components.base_component import ShipComponent

class PhotonTorpedo(ShipComponent):
    def __init__(self, power_draw, damage_output, reload_time, ammunition_capacity, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.damage_output = damage_output
        self.reload_time = reload_time
        self.ammunition_capacity = ammunition_capacity

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            damage_output=data["damage_output"],
            reload_time=data["reload_time"],
            ammunition_capacity=data["ammunition_capacity"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "damage_output", "reload_time", "ammunition_capacity"]}
        )

# Loader utility
def load_photon_torpedoes_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [PhotonTorpedo.from_dict(entry) for entry in data] 