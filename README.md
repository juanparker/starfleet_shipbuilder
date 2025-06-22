# starfleet_shipbuilder

## Warp Core Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the warp core model (e.g. "Class-7 Warp Core"). |
| `type`              | string         | Identifies the component type; always `"warp_core"` for these entries. |
| `mass`              | int            | How much the warp core weighs; contributes to the ship's total hull mass. |
| `power_output`      | int            | Maximum amount of power (in arbitrary units) the core can generate continuously. |
| `stability_rating`  | float (0.0–1.0)| Indicates reliability. Higher means fewer chances of overload or failure under high draw. |
| `volume`            | int            | Physical space the core occupies inside the ship. Useful for ship volume capacity limits. |
| `crew_required`     | int            | Number of crew needed to operate and maintain the warp core. |
| `tech_tier`         | int            | Technology level required to manufacture or install this core. Helps gate progression. |
| `description`       | string         | Flavor/lore text describing the core's function or context. |
| `tags`              | list of string | Categorizations for filtering and mission logic (e.g. `["power", "standard", "mid-range"]`). |


## Warp Drive Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the warp drive (e.g. "Type-6 Warp Drive"). |
| `type`              | string         | Identifies the component type; always `"warp_drive"` for these entries. |
| `mass`              | int            | The physical mass of the drive, contributing to total ship mass. |
| `power_draw`        | int            | The amount of power the warp drive consumes when active. |
| `max_warp_factor`   | float          | The maximum warp factor the drive can achieve. |
| `efficiency_rating` | float (0.0–1.0)| Indicates how efficiently the drive converts power to velocity; affects power cost and performance. |
| `volume`            | int            | Space the drive occupies within the ship frame. |
| `crew_required`     | int            | Number of crew members needed to operate the warp drive. |
| `tech_tier`         | int            | Technology level needed to build or install the drive. |
| `description`       | string         | Flavored text or technical summary of the component. |
| `tags`              | list of string | Keywords used for filtering, categorization, and mission logic (e.g. `["propulsion", "standard"]`). |

Each warp drive:
- Draws power from a Warp Core.
- Has a `max_warp_factor` (representing top speed).
- Uses `efficiency_rating` to potentially affect fuel/power usage scaling or mission speed multipliers.
- Has a distinct `tech_tier` and flavor based on gameplay role.


## Impulse Drive Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the impulse drive (e.g. "Standard Impulse Engine"). |
| `type`              | string         | Identifies the component type; always `"impulse_engine"` for these entries. |
| `mass`              | int            | How much the engine weighs; contributes to the ship's total hull mass. |
| `power_draw`        | int            | The amount of power the impulse engine consumes while in use. |
| `sublight_speed`    | float          | The maximum sublight velocity, normalized (e.g. 0.25 = 25% speed of light). |
| `maneuverability`   | float (0.0–1.0)| Reflects agility and responsiveness; higher values improve evasion and handling. |
| `volume`            | int            | How much internal ship space this engine takes up. |
| `crew_required`     | int            | The number of crew needed to monitor and maintain the system. |
| `tech_tier`         | int            | Technology level required to build or install the engine. |
| `description`       | string         | Text flavor or summary of the engine's role or use. |
| `tags`              | list of string | Used for filtering, categorization, or system logic (e.g. `["propulsion", "combat"]`). |

Each impulse drive:
- Determines sublight speed and agility of the ship.
- Uses `maneuverability` to affect turns, dodging, docking, and tactical positioning.
- Is affected by total ship mass and available power.


## Deflector Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the deflector unit (e.g. "Quantum Phase Deflector"). |
| `type`              | string         | Identifies the component type; always `"deflector"` for these entries. |
| `mass`              | int            | The weight of the deflector, contributing to total hull mass. |
| `power_draw`        | int            | Power consumed while the deflector is operational. |
| `deflection_rating` | int            | Strength of the deflector field — affects protection against debris and energy impacts. |
| `sensor_boost`      | float          | Multiplier or bonus to the ship’s sensor range or resolution. |
| `volume`            | int            | Physical space the deflector occupies in the ship. |
| `crew_required`     | int            | Number of crew needed to maintain the deflector system. |
| `tech_tier`         | int            | Technology level required to build or support this deflector. |
| `description`       | string         | Lore or usage explanation for the component. |
| `tags`              | list of string | Keywords used for filtering or mission logic (e.g. `["navigation", "sensor-boost"]`). |

Each deflector:
- Protects the ship at warp and impulse speeds.
- May enhance scanning capabilities depending on the `sensor_boost`.
- Could be expanded in future with `interference_resistance` or `signal_focus`.


## Shield Generator Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the shield generator (e.g. "Aegis Field Projector"). |
| `type`              | string         | Identifies the component type; always `"shield_generator"` for these entries. |
| `mass`              | int            | The weight of the shield system, affecting total ship mass. |
| `power_draw`        | int            | Power required to keep shields online. |
| `shield_strength`   | int            | Maximum shield capacity; how much damage the system can absorb. |
| `recharge_rate`     | int            | Amount of shield strength regenerated per time unit or tick. |
| `volume`            | int            | Physical space the generator occupies inside the ship. |
| `crew_required`     | int            | Number of crew members needed to operate and maintain the shields. |
| `tech_tier`         | int            | Technology level required to manufacture or install the system. |
| `description`       | string         | Flavored or technical description of the shield system. |
| `tags`              | list of string | Keywords for filtering, classification, or gameplay mechanics (e.g. `["defense", "combat"]`). |

Each shield generator:
- Adds a shield layer to the ship's defenses.
- Regenerates over time based on the `recharge_rate`.
- Can be overwhelmed if incoming damage exceeds strength or recovery.


## Sensor Array Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the sensor array (e.g. "Quantum Phase Detector Grid"). |
| `type`              | string         | Identifies the component type; always `"sensor_array"` for these entries. |
| `mass`              | int            | The weight of the array, adding to the ship’s hull mass. |
| `power_draw`        | int            | Power required to keep the sensor array operational. |
| `scan_range`        | int            | How far the sensors can scan, in abstract units (e.g. mission range, tactical grid). |
| `resolution`        | float (0.0–1.0)| Sensor clarity and data quality — affects detection accuracy and analysis depth. |
| `volume`            | int            | Space the array takes up inside the ship. |
| `crew_required`     | int            | Crew needed to operate and maintain the array. |
| `tech_tier`         | int            | Technology level required to manufacture or install. |
| `description`       | string         | Flavor or technical summary of the sensor package. |
| `tags`              | list of string | Classification or functional tags (e.g. `["sensor", "multi-spectrum", "navigation"]`). |

Each sensor array:
- Determines how far and how clearly the ship can scan.
- Uses `resolution` to affect anomaly detection, targeting, and mission insights.
- Can be extended later with features like stealth detection or frequency tuning.


## Computer Core Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the computer core (e.g. "Mk I Computer Core"). |
| `type`              | string         | Identifies the component type; always `"computer_core"` for these entries. |
| `mass`              | int            | The mass of the core, contributing to overall ship mass. |
| `power_draw`        | int            | Power required to operate the computer core. |
| `processing_power`  | int            | An abstract measure of system throughput; may affect sensor performance, tactical responsiveness, or scientific computation. |
| `ai_support`        | boolean        | Indicates whether the core supports advanced AI modules and behavior control. |
| `volume`            | int            | Space the computer core takes up inside the ship. |
| `crew_required`     | int            | Number of crew members required to operate and maintain the core. |
| `tech_tier`         | int            | Technology level required to build or install the system. |
| `description`       | string         | Narrative or technical summary of the core's capabilities. |
| `tags`              | list of string | Used for filtering, role assignment, or mission interaction logic (e.g. `["core", "ai", "command"]`). |

Each computer core:
- Acts as the ship's computational and command system.
- May unlock or improve automated systems when `ai_support` is enabled.
- Higher `processing_power` can boost performance in tactical, scientific, or mission operations.


## Life Support Component Attributes

| Attribute            | Type           | Description |
|----------------------|----------------|-------------|
| `name`               | string         | The display name of the life support system (e.g. "Basic Life Support Unit"). |
| `type`               | string         | Identifies the component type; always `"life_support"` for these entries. |
| `mass`               | int            | Physical weight of the unit, affecting total ship mass. |
| `power_draw`         | int            | Power consumed during normal operation. |
| `crew_supported`     | int            | Maximum number of crew the system can sustain under standard operating conditions. |
| `redundancy_rating`  | float (0.0–1.0)| Fault tolerance of the system. Higher values mean greater resilience to failures. |
| `volume`             | int            | Physical space occupied within the ship. |
| `crew_required`      | int            | Number of crew members needed to manage and maintain the system. |
| `tech_tier`          | int            | Technology level required to construct or use the system. |
| `description`        | string         | Technical or narrative description of the system. |
| `tags`               | list of string | Keywords for filtering, gameplay effects, or UI grouping (e.g. `["life_support", "basic"]`). |

Each life support system:
- Determines how many crew can be safely supported on a ship.
- Affects survivability and failure behavior through `redundancy_rating`.
- Can be critical for long-term missions or in emergencies.


## Science Lab Component Attributes

| Attribute           | Type           | Description |
|---------------------|----------------|-------------|
| `name`              | string         | The display name of the science lab (e.g. "Quantum Field Analysis Lab"). |
| `type`              | string         | Identifies the component type; always `"science_lab"` for these entries. |
| `mass`              | int            | The weight of the lab, contributing to total ship mass. |
| `power_draw`        | int            | The amount of power required to keep the lab operational. |
| `research_output`   | int            | Total scientific contribution — used in mission logic and discovery systems. |
| `analysis_speed`    | float (0.0–1.0)| Rate at which the lab processes data, affecting mission speed or success. |
| `volume`            | int            | Physical space the lab occupies inside the ship. |
| `crew_required`     | int            | Crew members needed to operate the lab. |
| `tech_tier`         | int            | Technology level required to construct or install the lab. |
| `description`       | string         | Narrative or technical summary of the lab’s function. |
| `tags`              | list of string | Tags used for filtering, mission scoring, or UI classification (e.g. `["science", "research"]`). |

Each science lab:
- Produces `research_output` for missions involving exploration, anomalies, or analysis.
- Uses `analysis_speed` to reduce mission time or increase effectiveness.
- Can vary by specialization or mission type compatibility.


## Transporter Component Attributes

| Attribute               | Type           | Description |
|-------------------------|----------------|-------------|
| `name`                  | string         | The display name of the transporter system (e.g. "Standard Personnel Transporter"). |
| `type`                  | string         | Identifies the component type; always `"transporter"` for these entries. |
| `mass`                  | int            | Physical mass of the transporter system. |
| `power_draw`            | int            | Power required to operate the transporter. |
| `range`                 | int            | Effective transport range in abstract or tactical units. |
| `cycle_time`            | int            | Time between transport cycles (in seconds or simulation ticks). |
| `simultaneous_capacity` | int            | Number of entities that can be transported per activation. |
| `volume`                | int            | Physical space the system occupies in the ship. |
| `crew_required`         | int            | Number of crew required to maintain and operate the system. |
| `tech_tier`             | int            | Technology level needed to install or build the system. |
| `description`           | string         | Lore or technical explanation of the system. |
| `tags`                  | list of string | Tags for categorization, filtering, and mission logic (e.g. `["transporter", "cargo"]`). |

Each transporter system:
- Moves personnel or cargo across space within its operational `range`.
- Uses `cycle_time` to determine the frequency of use.
- Supports multiple entity transport using `simultaneous_capacity`.


## Phaser Bank Component Attributes

| Attribute         | Type           | Description |
|-------------------|----------------|-------------|
| `name`            | string         | The display name of the phaser bank (e.g. "Type-X Phaser Bank"). |
| `type`            | string         | Identifies the component type; always `"phaser_bank"` for these entries. |
| `mass`            | int            | Physical weight of the weapon system. |
| `power_draw`      | int            | Power required per firing cycle. |
| `damage_output`   | int            | Base energy damage dealt per shot. |
| `firing_arc`      | string         | Firing direction or coverage area (e.g. `forward`, `aft`, `omnidirectional`). |
| `cooldown_time`   | int            | Time between consecutive shots (in simulation ticks or seconds). |
| `volume`          | int            | Space occupied by the weapon system inside the ship. |
| `crew_required`   | int            | Number of crew needed to operate and maintain the system. |
| `tech_tier`       | int            | Technology level required to build or install the system. |
| `description`     | string         | Narrative or technical description of the weapon. |
| `tags`            | list of string | Tags for filtering, tactical role, or classification (e.g. `["weapon", "phaser", "standard"]`). |

Each phaser bank:
- Delivers directed energy attacks against enemy targets.
- Has a `firing_arc` that determines its engagement orientation.
- Uses `cooldown_time` to define its firing rate and tactical pacing.


## Photon Torpedo Component Attributes

| Attribute             | Type           | Description |
|-----------------------|----------------|-------------|
| `name`                | string         | The display name of the torpedo launcher (e.g. "Mk I Torpedo Launcher"). |
| `type`                | string         | Identifies the component type; always `"photon_torpedo"` for these entries. |
| `mass`                | int            | Physical weight of the torpedo launcher. |
| `power_draw`          | int            | Power consumed per firing cycle. |
| `damage_output`       | int            | Base explosive or kinetic damage dealt per shot. |
| `reload_time`         | int            | Time between firings (in simulation ticks or seconds). |
| `ammunition_capacity` | int            | Total number of torpedoes the launcher can hold before resupply is required. |
| `volume`              | int            | Internal space required to mount the launcher. |
| `crew_required`       | int            | Number of crew needed to operate and maintain the launcher. |
| `tech_tier`           | int            | Technology level required to build or install the system. |
| `description`         | string         | Narrative or technical description of the torpedo system. |
| `tags`                | list of string | Tags for filtering, classification, or mission scoring (e.g. `["weapon", "torpedo", "mid-tier"]`). |

Each photon torpedo launcher:
- Provides heavy payload-based offensive capability.
- Uses `reload_time` to control rate of fire.
- Tracks onboard torpedoes using `ammunition_capacity`.

## Building Ships Interactively

Run `python ship_builder_cli.py` and follow the prompts to choose a ship class and install components. The finished configuration will be saved in the `ships/` directory as a JSON file.

As you select each component the CLI now shows progress bars reflecting current mass, volume, crew, and power usage compared to the limits of the chosen ship class. This helps avoid over-provisioning while building your ship.
