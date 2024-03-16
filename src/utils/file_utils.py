import csv
from typing import Union


class CSV:

    @staticmethod
    def save(file_path: str, columns: list[str], content: Union[list, dict]) -> None:
        with open(file_path, mode="w", newline="") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=columns)
            dict_writer.writeheader()
            dict_writer.writerows(content)

    @staticmethod
    def load(file_path: str) -> list:
        with open(file_path, mode="r") as input_file:
            reader = csv.reader(input_file, delimiter=",")
            return [line for line in reader]
