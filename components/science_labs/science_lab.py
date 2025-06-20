import json
from components.base_component import ShipComponent

class ScienceLab(ShipComponent):
    def __init__(self, power_draw, research_output, analysis_speed, **kwargs):
        super().__init__(**kwargs)
        self.power_draw = power_draw
        self.research_output = research_output
        self.analysis_speed = analysis_speed

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_draw=data["power_draw"],
            research_output=data["research_output"],
            analysis_speed=data["analysis_speed"],
            **{k: v for k, v in data.items() if k not in ["power_draw", "research_output", "analysis_speed"]}
        )

# Loader utility
def load_science_labs_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [ScienceLab.from_dict(entry) for entry in data] 