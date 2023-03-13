import json
import os
# open jsonl file and save each line as a new json file
def save_jsonl(jsonl_file, output_dir):
    with open(jsonl_file, 'r') as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            output_file = os.path.join(output_dir, f'data_{i}.json')
            with open(output_file, 'w') as f:
                json.dump(data, f)

save_jsonl('tables.jsonl','json_dataset')

#  open each JSON file in a folder, extract a table from the file and save it as a text file
from bs4 import BeautifulSoup
import csv
input_folder = 'json_dataset'
output_folder = 'table_output'

for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file = os.path.join(input_folder, filename)
        with open(input_file, 'r') as f:
            data = json.load(f)
            if 'html' in data:
                soup = BeautifulSoup(data['html'], 'html.parser')
                tables = soup.find_all('table')
                for i, table in enumerate(tables):
                    output_file = f'{output_folder}/{filename}_table_{i}.csv'
                    with open(output_file, 'w', newline='') as f:
                        writer = csv.writer(f)
                        for row in table.find_all('tr'):
                            cells = row.find_all(['th', 'td'])
                            row_text = [cell.get_text(strip=True) for cell in cells]
                            writer.writerow(row_text)