# Spancat

`model` folder represents the model from ```prodigy train ./model --spancat democheckspancat --eval-split 0.5```

`corpus` folder represents the model from ```python3 -m prodigy data-to-spacy ./corpus --spancat democheckspancat --eval split 0.5```

# spans.manual

 python -m prodigy
 spans.manual 
 demoprofilespancat 
 blank:en 
 /home/kushal/Documents/spancat/annotate/corpus.jsonl 
 --label PROFILE_NAME,PROFILE_EMAIL,PROFILE_ADDRESS,PROFILE_PHONE


# spans.correct

prodigy
spans.correct
dataset
spacy_model
source
--loader
--label
--update
--exclude
--component

# Short info

The model and binary spacy files are generated from the annotated documents i.e 172 resumes, model are prepared after that and inferencing is here: 
 ```
./inferencing.txt
``` 
We think we will take dummy labels for almost additional 120 documents and again we check how the scores are obtained from the training. And we will move forward for real labels.