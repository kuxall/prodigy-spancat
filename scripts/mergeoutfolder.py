import pathlib
import srsly 
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")
full_dataset = [] 
for path in pathlib.Path(f"/home/kushal/Documents/spancat/outfolder2/").glob("*.json"):
    for ex in srsly.read_jsonl(path):
        full_dataset.append(ex)

srsly.write_jsonl(f"/home/kushal/Documents/spancat/annotate/corpus_25_03_2023.jsonl", full_dataset)