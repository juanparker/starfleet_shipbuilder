import json
import os

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

from ship_classes.ship_class import load_ship_classes
from ships.ships import Ship

DATA_DIR = os.path.join(os.path.dirname(__file__), "components")
SHIP_SAVE_PATH = os.path.join("ships", "built_ships.json")


def choose(options, label):
    print(f"\nSelect {label}:")
    for idx, item in enumerate(options, 1):
        print(f" {idx}. {item.name}")
    while True:
        choice = input("Enter number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid selection. Try again.")


def maybe_choose(options, label):
    print(f"\nSelect {label} (or press Enter to skip):")
    for idx, item in enumerate(options, 1):
        print(f" {idx}. {item.name}")
    choice = input("Enter number or press Enter to skip: ")
    if not choice:
        return None
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return options[int(choice) - 1]
    print("Invalid selection. Skipping.")
    return None


def load_all_components():
    base = os.path.join(os.path.dirname(__file__), "components")
    return {
        "warp_cores": load_warp_cores_from_json(os.path.join(base, "warp_cores", "warp_cores.json")),
        "warp_drives": load_warp_drives_from_json(os.path.join(base, "warp_drives", "warp_drives.json")),
        "life_support": load_life_support_from_json(os.path.join(base, "life_support", "life_support.json")),
        "deflectors": load_deflectors_from_json(os.path.join(base, "deflectors", "deflectors.json")),
        "impulse_drives": load_impulse_engines_from_json(os.path.join(base, "impulse_drives", "impulse_drives.json")),
        "shield_generators": load_shield_generators_from_json(os.path.join(base, "shield_generators", "shield_generators.json")),
        "computer_cores": load_computer_cores_from_json(os.path.join(base, "computer_cores", "computer_cores.json")),
        "science_labs": load_science_labs_from_json(os.path.join(base, "science_labs", "science_labs.json")),
        "sensor_arrays": load_sensor_arrays_from_json(os.path.join(base, "sensor_arrays", "sensor_arrays.json")),
        "transporters": load_transporters_from_json(os.path.join(base, "transporters", "transporters.json")),
        "phaser_banks": load_phaser_banks_from_json(os.path.join(base, "phaser_banks", "phaser_banks.json")),
        "photon_torpedoes": load_photon_torpedoes_from_json(os.path.join(base, "photon_torpedoes", "photon_torpedoes.json")),
    }


def save_ship_record(record):
    if os.path.exists(SHIP_SAVE_PATH):
        with open(SHIP_SAVE_PATH, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(record)
    with open(SHIP_SAVE_PATH, "w") as f:
        json.dump(data, f, indent=2)


def build_ship():
    components = load_all_components()
    ship_classes = load_ship_classes(os.path.join("ship_classes", "ship_classes.json"))

    ship_class = choose(ship_classes, "ship class")
    ship_name = input("Enter ship name: ") or "Unnamed Vessel"

    selected_components = []
    selected_components.append(choose(components["warp_cores"], "warp core"))
    selected_components.append(choose(components["warp_drives"], "warp drive"))
    selected_components.append(choose(components["life_support"], "life support"))
    selected_components.append(choose(components["deflectors"], "deflector"))
    selected_components.append(choose(components["impulse_drives"], "impulse drive"))
    selected_components.append(choose(components["shield_generators"], "shield generator"))
    selected_components.append(choose(components["computer_cores"], "computer core"))

    # Optional science labs
    while True:
        lab = maybe_choose(components["science_labs"], "science lab")
        if lab:
            selected_components.append(lab)
            if input("Add another science lab? (y/N): ").lower() != "y":
                break
        else:
            break

    selected_components.append(choose(components["sensor_arrays"], "sensor array"))
    transporter = maybe_choose(components["transporters"], "transporter")
    if transporter:
        selected_components.append(transporter)

    # Weapon mounts determined by ship class
    phaser_mounts = [m for m in ship_class.mount_points if m["type"] == "phaser_bank"]
    torpedo_mounts = [m for m in ship_class.mount_points if m["type"] == "photon_torpedo"]

    for mount in phaser_mounts:
        label = f"phaser bank for {mount['location']} mount"
        selected_components.append(choose(components["phaser_banks"], label))

    for mount in torpedo_mounts:
        label = f"photon torpedo launcher for {mount['location']} mount"
        selected_components.append(choose(components["photon_torpedoes"], label))

    ship = Ship(ship_class, selected_components)
    errors = ship.validate()
    if errors:
        print("\nShip validation failed:")
        for e in errors:
            print(" -", e)
        return

    record = {
        "name": ship_name,
        "class": ship_class.name,
        "components": [vars(c) for c in selected_components],
    }
    save_ship_record(record)
    print(f"\nShip '{ship_name}' saved successfully.")


if __name__ == "__main__":
    build_ship()
