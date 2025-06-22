import json
import os

from ship_classes.ship_class import load_ship_classes
from components.warp_cores.warp_core import load_warp_cores_from_json
from components.warp_drives.warp_drive import load_warp_drives_from_json
from components.life_support.life_support import load_life_support_from_json
from components.deflectors.deflector import load_deflectors_from_json
from components.impulse_drives.impulse_drive import load_impulse_engines_from_json
from components.shield_generators.shield_generator import load_shield_generators_from_json
from components.computer_cores.computer_core import load_computer_cores_from_json
from components.science_labs.science_lab import load_science_labs_from_json
from components.sensor_arrays.sensor_array import load_sensor_arrays_from_json
from components.transporters.transporter import load_transporters_from_json
from components.phaser_banks.phaser_bank import load_phaser_banks_from_json
from components.photon_torpedoes.photon_torpedo import load_photon_torpedoes_from_json
from ships.ships import Ship

DATA_DIR = os.path.join(os.path.dirname(__file__), "components")
SAVE_PATH = os.path.join("ships", "saved_ships.json")


def _load_or_empty(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


def _save_ship(data, path):
    ships = _load_or_empty(path)
    ships.append(data)
    with open(path, "w") as f:
        json.dump(ships, f, indent=2)


def _select_component(options, label):
    print(f"\nSelect {label}:")
    for idx, comp in enumerate(options, 1):
        print(f"  {idx}. {comp.name}")
    choice = int(input("Enter choice number: ")) - 1
    return options[choice]


def build_ship():
    classes = load_ship_classes(os.path.join("ship_classes", "ship_classes.json"))
    print("Available ship classes:")
    for idx, cls in enumerate(classes, 1):
        print(f"  {idx}. {cls.name} - {cls.description}")
    cls_idx = int(input("Select ship class number: ")) - 1
    ship_class = classes[cls_idx]

    name = input("Enter ship name: ")

    components = []

    warp_cores = load_warp_cores_from_json(os.path.join(DATA_DIR, "warp_cores", "warp_cores.json"))
    components.append(_select_component(warp_cores, "warp core"))

    warp_drives = load_warp_drives_from_json(os.path.join(DATA_DIR, "warp_drives", "warp_drives.json"))
    components.append(_select_component(warp_drives, "warp drive"))

    life_supports = load_life_support_from_json(os.path.join(DATA_DIR, "life_support", "life_support.json"))
    components.append(_select_component(life_supports, "life support"))

    deflectors = load_deflectors_from_json(os.path.join(DATA_DIR, "deflectors", "deflectors.json"))
    components.append(_select_component(deflectors, "deflector"))

    impulses = load_impulse_engines_from_json(os.path.join(DATA_DIR, "impulse_drives", "impulse_drives.json"))
    components.append(_select_component(impulses, "impulse drive"))

    shields = load_shield_generators_from_json(os.path.join(DATA_DIR, "shield_generators", "shield_generators.json"))
    components.append(_select_component(shields, "shield generator"))

    computers = load_computer_cores_from_json(os.path.join(DATA_DIR, "computer_cores", "computer_cores.json"))
    components.append(_select_component(computers, "computer core"))

    sensors = load_sensor_arrays_from_json(os.path.join(DATA_DIR, "sensor_arrays", "sensor_arrays.json"))
    components.append(_select_component(sensors, "sensor array"))

    if input("Add science lab? [y/N]: ").lower().startswith("y"):
        labs = load_science_labs_from_json(os.path.join(DATA_DIR, "science_labs", "science_labs.json"))
        components.append(_select_component(labs, "science lab"))

    if input("Add transporter? [y/N]: ").lower().startswith("y"):
        transporters = load_transporters_from_json(os.path.join(DATA_DIR, "transporters", "transporters.json"))
        components.append(_select_component(transporters, "transporter"))

    # Weapon mounts
    mount_points = ship_class.mount_points
    phaser_slots = len([m for m in mount_points if m["type"] == "phaser_bank"])
    if phaser_slots:
        phasers = load_phaser_banks_from_json(os.path.join(DATA_DIR, "phaser_banks", "phaser_banks.json"))
        count = int(input(f"Number of phaser banks (0-{phaser_slots}): "))
        for i in range(min(count, phaser_slots)):
            components.append(_select_component(phasers, f"phaser bank {i + 1}"))

    torpedo_slots = len([m for m in mount_points if m["type"] == "photon_torpedo"])
    if torpedo_slots:
        torpedoes = load_photon_torpedoes_from_json(os.path.join(DATA_DIR, "photon_torpedoes", "photon_torpedoes.json"))
        count = int(input(f"Number of photon torpedo launchers (0-{torpedo_slots}): "))
        for i in range(min(count, torpedo_slots)):
            components.append(_select_component(torpedoes, f"photon torpedo {i + 1}"))

    ship = Ship(ship_class, components)
    errors = ship.validate()
    if errors:
        print("\nShip validation failed:")
        for e in errors:
            print(f"- {e}")
        return

    ship_data = {
        "name": name,
        "class": ship_class.name,
        "components": [c.name for c in components],
    }
    _save_ship(ship_data, SAVE_PATH)
    print(f"\n{name} saved to {SAVE_PATH}")


if __name__ == "__main__":
    build_ship()
