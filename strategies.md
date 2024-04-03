## Strategies - 1

### This is the strategy that should be used by an annotators and start annotating the spans only by selecting the starting and ending points for the given labels.

!python -m prodigy spans.manual segmentation blank:en ./annotate/corpus_27_03_2023.jsonl --label PROFILES,EXPERIENCES


## Strategies - 2

### This is the strategy that should be used by an annotators and start annotating the spans only by selecting the starting and ending points for the given labels but the inner labels that is mentioned below:

!python -m prodigy spans.manual inner_segmentation blank:en ./annotate/corpus_27_03_2023.jsonl --label PROFILES_NAME,PROFILES_EMAIL,PROFILES_ADDRESS,PROFILES_PHONE,EXPERIENCES_ORGANIZATION,EXPERIENCES_ADDRESS,EXPERIENCES_START,EXPERIENCES_END,EXPERIENCES_POSITION