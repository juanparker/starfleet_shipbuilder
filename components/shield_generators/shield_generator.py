import json
from components.base_component import ShipComponent

class ShieldGenerator(ShipComponent):
    def __init__(self, power_draw, shield_strength, recharge_rate, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.shield_strength = shield_strength
        self.recharge_rate = recharge_rate

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            shield_strength=data["shield_strength"],
            recharge_rate=data["recharge_rate"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "shield_strength", "recharge_rate"]}
        )

# Loader utility
def load_shield_generators_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [ShieldGenerator.from_dict(entry) for entry in data] 