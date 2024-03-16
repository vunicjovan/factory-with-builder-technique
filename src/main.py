from src.models.base.vehicle import Vehicle
from src.utils.file_utils import CSV
from src.utils.randomizer import Randomizer

if __name__ == '__main__':
    VEHICLES_TO_BE_PRODUCED = 10000
    CSV_FILE_PATH = "random_vehicles.csv"
    CSV_HEADERS = ["brand", "model", "color", "gearshift_type", "fuel_source"]

    random_vehicles = Randomizer.produce_random_vehicles(VEHICLES_TO_BE_PRODUCED)
    random_vehicles_for_csv = list(map(Vehicle.__to_dict__, random_vehicles))
    CSV.save(CSV_FILE_PATH, CSV_HEADERS, random_vehicles_for_csv)

    loaded_vehicles = CSV.load(CSV_FILE_PATH)
    [print(vehicle) for vehicle in loaded_vehicles]
