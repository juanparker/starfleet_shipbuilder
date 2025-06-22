import json
from ship_classes.ship_class import load_ship_classes
from ships.ships import Ship
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


def _progress_bar(current, maximum, bar_len=20):
    if maximum == 0:
        ratio = 0
    else:
        ratio = min(current / maximum, 1)
    filled = int(ratio * bar_len)
    bar = "#" * filled + "-" * (bar_len - filled)
    return f"[{bar}] {current}/{maximum}"


class ShipBuilder:
    def __init__(self):
        self.ship_classes = load_ship_classes('ship_classes/ship_classes.json')
        self.warp_cores = load_warp_cores_from_json('components/warp_cores/warp_cores.json')
        self.warp_drives = load_warp_drives_from_json('components/warp_drives/warp_drives.json')
        self.life_support = load_life_support_from_json('components/life_support/life_support.json')
        self.deflectors = load_deflectors_from_json('components/deflectors/deflectors.json')
        self.impulse_engines = load_impulse_engines_from_json('components/impulse_drives/impulse_drives.json')
        self.shield_generators = load_shield_generators_from_json('components/shield_generators/shield_generators.json')
        self.computer_cores = load_computer_cores_from_json('components/computer_cores/computer_cores.json')
        self.science_labs = load_science_labs_from_json('components/science_labs/science_labs.json')
        self.sensor_arrays = load_sensor_arrays_from_json('components/sensor_arrays/sensor_arrays.json')
        self.transporters = load_transporters_from_json('components/transporters/transporters.json')
        self.phaser_banks = load_phaser_banks_from_json('components/phaser_banks/phaser_banks.json')
        self.photon_torpedoes = load_photon_torpedoes_from_json('components/photon_torpedoes/photon_torpedoes.json')

    def _print_progress(self, ship_class, components):
        total_mass = sum(c.mass for c in components)
        total_volume = sum(c.volume for c in components)
        total_power_draw = sum(getattr(c, 'power_draw', 0) for c in components)
        total_crew = sum(c.crew_required for c in components)

        warp_core = next((c for c in components if c.type == "warp_core"), None)
        power_output = warp_core.power_output if warp_core else 0

        print("\nCurrent stats:")
        print("Mass       ", _progress_bar(total_mass, ship_class.hull_mass_limit))
        print("Volume     ", _progress_bar(total_volume, ship_class.volume_capacity))
        print("Crew       ", _progress_bar(total_crew, ship_class.crew_capacity))
        print("Power Draw ", _progress_bar(total_power_draw, ship_class.power_handling_cap))
        if warp_core:
            print("Power Gen  ", _progress_bar(power_output, total_power_draw if total_power_draw > 0 else power_output))

    def _select(self, options, prompt):
        print(prompt)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option.name}")
        idx = int(input('Enter choice number: ')) - 1
        return options[idx]

    def build(self):
        ship_class = self._select(self.ship_classes, '\nSelect ship class:')
        name = input('Enter ship name: ')

        components = []
        components.append(self._select(self.warp_cores, '\nSelect warp core:'))
        self._print_progress(ship_class, components)
        components.append(self._select(self.warp_drives, '\nSelect warp drive:'))
        self._print_progress(ship_class, components)
        components.append(self._select(self.life_support, '\nSelect life support system:'))
        self._print_progress(ship_class, components)
        components.append(self._select(self.deflectors, '\nSelect deflector:'))
        self._print_progress(ship_class, components)
        components.append(self._select(self.impulse_engines, '\nSelect impulse drive:'))
        self._print_progress(ship_class, components)
        components.append(self._select(self.shield_generators, '\nSelect shield generator:'))
        self._print_progress(ship_class, components)
        components.append(self._select(self.computer_cores, '\nSelect computer core:'))
        self._print_progress(ship_class, components)
        components.append(self._select(self.sensor_arrays, '\nSelect sensor array:'))
        self._print_progress(ship_class, components)

        # Optional components
        if input('Add science lab? (y/n): ').lower().startswith('y'):
            components.append(self._select(self.science_labs, '\nSelect science lab:'))
            self._print_progress(ship_class, components)
        if input('Add transporter? (y/n): ').lower().startswith('y'):
            components.append(self._select(self.transporters, '\nSelect transporter:'))
            self._print_progress(ship_class, components)

        phaser_slots = sum(1 for mp in ship_class.mount_points if mp['type'] == 'phaser_bank')
        torpedo_slots = sum(1 for mp in ship_class.mount_points if mp['type'] == 'photon_torpedo')

        print(f"\nShip class allows up to {phaser_slots} phaser banks.")
        for _ in range(phaser_slots):
            if input('Add phaser bank? (y/n): ').lower().startswith('y'):
                components.append(self._select(self.phaser_banks, 'Select phaser bank:'))
                self._print_progress(ship_class, components)
            else:
                break

        print(f"\nShip class allows up to {torpedo_slots} photon torpedo launchers.")
        for _ in range(torpedo_slots):
            if input('Add photon torpedo launcher? (y/n): ').lower().startswith('y'):
                components.append(self._select(self.photon_torpedoes, 'Select torpedo launcher:'))
                self._print_progress(ship_class, components)
            else:
                break

        ship = Ship(ship_class, components)
        errors = ship.validate()
        if errors:
            print('\nShip failed validation:')
            for e in errors:
                print('-', e)
        else:
            print('\nShip successfully built!')
        self._print_progress(ship_class, components)

        data = {
            'name': name,
            'ship_class': ship_class.name,
            'components': [c.name for c in components]
        }
        with open(f'ships/{name}.json', 'w') as f:
            json.dump(data, f, indent=2)
        print(f'Ship saved to ships/{name}.json')


if __name__ == '__main__':
    builder = ShipBuilder()
    builder.build()
