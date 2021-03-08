from library.common.random_generator import random_str
from pathlib import Path
import csv

csv_file = Path(__file__).parent.joinpath('sn.csv')

rows = [[random_str(16)] for i in range(1000)]

with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
