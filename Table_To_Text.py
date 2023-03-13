from transformers import pipeline

input_file = 'table_output/data_0.json_table_0.txt'
output_file = 'output1.txt'

summarizer = pipeline('summarization')

with open(input_file, 'r') as f:
    text = f.read()
    summary = summarizer(text, max_length=1024)[0]['summary_text']
    lines = summary.split('\n')
    if lines:
        headers = lines[0].strip().split('\t')
        if len(lines) > 1:
            values = lines[1].strip().split('\t')
            with open(output_file, 'w') as f:
                for header, value in zip(headers, values):
                    f.write(f'{header}: {value}\n')