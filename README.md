+---------------------+
|   BattleController  |
+---------------------+
| - battle_state      |
+---------------------+
| + start_battle()    |
| + run_turn()        |
| + apply_turn_effects() |
| + check_win_condition() |
| + end_battle()      |
+---------------------+
          |
          ▼
+---------------------+
|     BattleState     |
+---------------------+
| - trainer1          |
| - trainer2          |
| - active_pokemon    |
| - turn_count        |
| - weather           |
| - field_effects     |
+---------------------+
| + get_opponent()    |
| + get_active()      |
| + is_battle_over()  |
+---------------------+
          |
          ▼
+------------------------+
|   PokemonInBattle      |
+------------------------+
| - base_pokemon         |
| - current_hp           |
| - status_condition     |
| - stat_boosts          |
| - volatile_status      |
| - disabled_moves       |
| - protect_counter      |
+------------------------+
| + is_fainted()         |
| + apply_damage()       |
| + heal()               |
| + reset_boosts()       |
| + get_modified_stat()  |
| + can_move()           |
| + select_move()        |
| + decrement_pp()       |
| + has_type()           |
+------------------------+
          |
          ▼
+------------------------+
|       Pokemon          |
+------------------------+
| - name                |
| - level               |
| - types               |
| - nature              |
| - base_stats          |
| - ivs                 |
| - evs                 |
| - moves [4]           |
+------------------------+
| + calculate_stats()   |
| + get_stat()          |
| + get_move()          |
+------------------------+
          |
          ▼
+------------------------+
|        Move            |
+------------------------+
| - name                |
| - type_               |
| - category            |
| - power               |
| - accuracy            |
| - max_pp              |
| - current_pp          |
| - priority            |
| - target              |
| - effects             |
| - contact             |
+------------------------+
| + use_pp()            |
| + reset_pp()          |
| + can_be_used()       |
| + triggers_effects()  |
+------------------------+

+------------------------+
|        Stats           |
+------------------------+
| - hp, atk, def_, spa,  |
|   spd, spe             |
+------------------------+
| + as_dict()           |
| + total()             |
| + apply_modifier()    |
| + copy()              |
| + __getitem__()       |
+------------------------+

+------------------------+
|        Trainer         |
+------------------------+
| - name                |
| - team [list]         |
| - active_index        |
| - is_ai               |
+------------------------+
| + choose_action()     |
| + get_active_pokemon()|
| + has_usable_pokemon()|
| + switch_pokemon()    |
+------------------------+


# GENERIC DISTRIBUTION OF THE PROJECT
poke_battle_project/
│
├── main.py
├── README.md
├── .gitignore
│
├── test_data/
│   └── trainer_data.json
│
├── core/                  # Lógica principal del juego (núcleo)
│   ├── trainer.py         # Clase Trainer
│   ├── pokemon.py         # Clase Pokemon
│   ├── stats.py           # Clase Stats
│   └── move.py            # Clase Move
│
├── battle/                # Todo lo relacionado con combates
│   ├── battle_controller.py   # BattleController
│   ├── battle_state.py        # BattleState
│   ├── pokemon_in_battle.py   # PokemonInBattle
│   └── mechanics/             # Submódulo para lógica específica
│       ├── damage_calc.py     # (futura lógica de daño)
│       ├── status_effects.py  # (futura lógica de estados)
│       └── move_resolution.py # (resolver turnos, pr
ioridades, etc.)
│
├── data/                 # Datos reutilizables o constantes
│   ├── types.py           # Tipos, ventajas y desventajas
│   └── moves_data.json    # Datos de movimientos (opcional)
│
└── utils/                # Utilidades generales
    ├── loader.py         # Cargar desde JSON, validación
    └── logger.py         # Debug/logging personalizado
