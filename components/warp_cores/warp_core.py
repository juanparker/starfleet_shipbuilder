import json
from components.base_component import ShipComponent

class WarpCore(ShipComponent):
    def __init__(self, power_output, stability_rating, **kwargs):
        super().__init__(**kwargs)
        self.power_output = power_output
        self.stability_rating = stability_rating

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_output=data["power_output"],
            stability_rating=data["stability_rating"],
            **{k: v for k, v in data.items() if k not in ["power_output", "stability_rating"]}
        )

# Loader utility
def load_warp_cores_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [WarpCore.from_dict(entry) for entry in data]