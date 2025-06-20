import json

class ShipClass:
    def __init__(self, name, frame_size, description, hull_mass_limit, power_handling_cap,
                 crew_capacity, component_hardpoints, volume_capacity, tech_tier,
                 build_cost, build_time, required_facilities, mission_bonus_tags, mount_points):
        self.name = name
        self.frame_size = frame_size
        self.description = description
        self.hull_mass_limit = hull_mass_limit
        self.power_handling_cap = power_handling_cap
        self.crew_capacity = crew_capacity
        self.component_hardpoints = component_hardpoints
        self.volume_capacity = volume_capacity
        self.tech_tier = tech_tier
        self.build_cost = build_cost
        self.build_time = build_time
        self.required_facilities = required_facilities
        self.mission_bonus_tags = mission_bonus_tags
        self.mount_points = mount_points

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

def load_ship_classes(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [ShipClass.from_dict(entry) for entry in data]