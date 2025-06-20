class ShipComponent:
    def __init__(self, name, type, mass, volume, crew_required, tech_tier, description, tags):
        self.name = name
        self.type = type
        self.mass = mass
        self.volume = volume
        self.crew_required = crew_required
        self.tech_tier = tech_tier
        self.description = description
        self.tags = tags

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"