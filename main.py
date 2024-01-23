from json import load
from src.show_operations_data import show_operations_data

with open("data/operations.json", encoding="utf8") as f:
    data = load(f)

print(show_operations_data(data))
