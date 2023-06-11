from typing import List, Dict

import csv


def write_results(output_path: str, data: List[Dict[str, str | float]]) -> None:
    with open(output_path, "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def read_results(file_path: str) -> List[Dict[str, str | float]]:
    results = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            results.append(row)
    return results
