import json
from components.base_component import ShipComponent

class PhaserBank(ShipComponent):
    def __init__(self, power_draw, damage_output, firing_arc, cooldown_time, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.damage_output = damage_output
        self.firing_arc = firing_arc
        self.cooldown_time = cooldown_time

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            damage_output=data["damage_output"],
            firing_arc=data["firing_arc"],
            cooldown_time=data["cooldown_time"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "damage_output", "firing_arc", "cooldown_time"]}
        )

# Loader utility
def load_phaser_banks_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [PhaserBank.from_dict(entry) for entry in data] 