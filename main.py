from utils.loader_data import load_trainer_data_from_json


if __name__ == '__main__':
    pathFile = r"C:\Users\Usuario\Desktop\proyectos\pokemon_game\test_data\trainer_data.json"
    trainer1 = load_trainer_data_from_json (pathFile)
    
    trainer1.print_information_trainer ()
    
    