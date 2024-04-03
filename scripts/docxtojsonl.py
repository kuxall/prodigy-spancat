# import json

# with open('/home/kushal/Dropbox/dolphindrive/Dataset/resumes/Batch#1Jsonl-250/_UI.jsonl', 'r') as f:
#     text_values = []
#     for line in f:
#         data = json.loads(line)
#         text = data['text']
#         if text:
#             text_values.append(text)

# output_data = {'text': ' '.join(text_values)}
# with open('_UI.json', 'w') as f:
#     json.dump(output_data, f)

# import json
# import glob
# import os

# folder_path = '/home/kushal/Dropbox/dolphindrive/Dataset/resumes/Batch#1Jsonl-250/'
# for filename in glob.glob(os.path.join(folder_path, '*.jsonl')):
#     with open(filename, 'r') as f:
#         text_values = []
#         for line in f:
#             data = json.loads(line)
#             text = data['text']
#             if text:
#                 text_values.append(text)
#         output_data = {'text': ' '.join(text_values)}
#         output_filename = os.path.splitext(filename)[0] + '.json'
#         with open(output_filename, 'w') as f:
#             json.dump(output_data, f)

import json
import glob
import os

input_folder_path = '/home/kushal/Dropbox/dolphindrive/Dataset/resumes/Batch#2Jsonl-500/'
output_folder_path = '/home/kushal/Documents/spancat/outfolder2/'

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

for filename in glob.glob(os.path.join(input_folder_path, '*.jsonl')):
    with open(filename, 'r') as f:
        text_values = []
        for line in f:
            data = json.loads(line)
            text = data['text']
            if text:
                text_values.append(text)
        output_data = {'text': ' '.join(text_values)}
        output_filename = os.path.join(output_folder_path, os.path.basename(filename).replace('.jsonl', '.json'))
        with open(output_filename, 'w') as f:
            json.dump(output_data, f)