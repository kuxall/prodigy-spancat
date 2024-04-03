
import spacy
nlp = spacy.load("/home/kushal/Documents/spancat/model/model-best/")
doc = nlp("Name: rajesh margaret E-Mail: rajesh.hamal@gmail.com Address: Kathmandu, Nepal Github: https://github.com/rajesh	 LinkedIn: https://linkedin.com/raja Phone No. 9866657042 ")
print(doc.spans)
# {'sc': [Septic shock, Septic shock, bacteremia, bacteremia]}
print([(span.text, span.label_) for span in doc.spans["sc"]])
# [('Septic shock', 'FACTOR'), ('Septic shock', 'CONDITION'), ('bacteremia', 'FACTOR'), ('bacteremia', 'CONDITION')]