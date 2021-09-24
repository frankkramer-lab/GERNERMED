import spacy
import os, sys

labels = {
    "Drug": "tan",
    "Route": "blue",
    "Strength": "yellow",
    "Frequency": "fuchsia",
    "Duration": "gray",
    "Form": "cyan",
    "Dosage": "orange"
}

dpath = os.path.abspath(os.path.dirname(__file__))
def example():
    global nlp

    nlp = spacy.load("gernermed_pipeline")
    global doc
    doc = nlp("Dem Patienten wurde die Einnahme von Paracetamol (500 mg, zwei Tabletten täglich, 8 Wochen lang) zur Behandlung empfohlen.")
    print(f"Satz: {doc.text}")
    for ent in doc.ents:
        print(f"{' '*2} {ent.label_} -> {repr(ent)}" )

    # displacy
    from spacy import displacy
    displacy.serve(doc, style="ent", options={ "ents": None, "colors": labels })

if __name__ == "__main__":
    example()
