import json
from components.base_component import ShipComponent

class SensorArray(ShipComponent):
    def __init__(self, power_draw, scan_range, resolution, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.scan_range = scan_range
        self.resolution = resolution

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            scan_range=data["scan_range"],
            resolution=data["resolution"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "scan_range", "resolution"]}
        )

# Loader utility
def load_sensor_arrays_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [SensorArray.from_dict(entry) for entry in data] 