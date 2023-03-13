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

#  open each JSON file in a folder, extract a table from the file and save it as a text file
import json
import os
from bs4 import BeautifulSoup

def extract_tables(json_folder, output_folder):
    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            with open(os.path.join(json_folder, filename), 'r') as f:
                data = json.load(f)
                html = data['html']
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find('table')
                output_file = os.path.join(output_folder, f'{filename}.txt')
                with open(output_file, 'w') as f:
                    for row in table.find_all('tr'):
                        f.write('\t'.join(cell.text for cell in row.find_all(['td', 'th'])) + '\n')

save_jsonl('/Users/rui/Documents/Georgetown/Hao/HTML_Table_to_TXT/tables.jsonl','/Users/rui/Documents/Georgetown/Hao/HTML_Table_to_TXT/json_dataset')

extract_tables('/Users/rui/Documents/Georgetown/Hao/HTML_Table_to_TXT/json_dataset','/Users/rui/Documents/Georgetown/Hao/HTML_Table_to_TXT/table_output')