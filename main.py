from battle import Battle




if __name__ == '__main__':
    battle = Battle()
    battle.load_trainer_data_from_file("test_data/trainer_data.json")
    battle.battle ()