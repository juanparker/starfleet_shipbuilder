import json
from components.base_component import ShipComponent

class Transporter(ShipComponent):
    def __init__(self, power_draw, range, cycle_time, simultaneous_capacity, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.range = range
        self.cycle_time = cycle_time
        self.simultaneous_capacity = simultaneous_capacity

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            range=data["range"],
            cycle_time=data["cycle_time"],
            simultaneous_capacity=data["simultaneous_capacity"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "range", "cycle_time", "simultaneous_capacity"]}
        )

# Loader utility
def load_transporters_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [Transporter.from_dict(entry) for entry in data] 