import json
from components.base_component import ShipComponent

class WarpDrive(ShipComponent):
    def __init__(self, power_draw, max_warp_factor, efficiency_rating, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.max_warp_factor = max_warp_factor
        self.efficiency_rating = efficiency_rating

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            max_warp_factor=data["max_warp_factor"],
            efficiency_rating=data["efficiency_rating"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "max_warp_factor", "efficiency_rating"]}
        )

# Loader utility
def load_warp_drives_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [WarpDrive.from_dict(entry) for entry in data] 