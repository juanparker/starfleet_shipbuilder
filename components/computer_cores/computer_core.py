import json
from components.base_component import ShipComponent

class ComputerCore(ShipComponent):
    def __init__(self, power_draw, processing_power, ai_support, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.processing_power = processing_power
        self.ai_support = ai_support

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            processing_power=data["processing_power"],
            ai_support=data["ai_support"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "processing_power", "ai_support"]}
        )

# Loader utility
def load_computer_cores_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [ComputerCore.from_dict(entry) for entry in data] 