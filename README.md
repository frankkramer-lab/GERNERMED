# GERNERMED - An Open German Medical NER Model

## About
The is the project repository for **GERNERMED**, a named entity recognition (NER) model in the context of German medical natural language processing (NLP).  
In particular, **GERNERMED** is the first open neural NER model for medical entities designed for German data.

**Our follow-up work, GERNERMED++, is available here:** http://github.com/frankkramer-lab/GERNERMED-pp

**Published papers:**\
See our short, software-related paper at: https://doi.org/10.1016/j.simpa.2021.100212 \
Or see our long paper at: https://doi.org/10.2196/39077

**NER entities:**
The following entities are supported:
- Drug
- Strength
- Route
- Form
- Dosage
- Frequency
- Duration

The evaluation scores on the test set are as follows:  

| NER Tag   | Precision | Recall | F1-Score |
|-----------|-----------|--------|----------|
| Drug      |     67.33 |  66.17 |    66.74 |
| Strength  |     92.34 |  90.99 |    91.66 |
| Route     |     89.93 |  90.14 |    90.04 |
| Form      |     91.94 |  89.24 |    90.57 |
| Dosage    |     87.83 |  87.57 |    87.70 |
| Frequency |     79.14 |  76.92 |    78.01 |
| Duration  |     67.86 |  52.78 |    59.37 |
| total     |     82.31 |  80.79 |    81.54 |

### NER Demonstration
<kbd><img src="./data/demo.png" alt="NER example demo" width="600"/></kbd>
                                                              
## Setup and Usage

For a quick test, run `python3 example.py` to run the NER model pipeline.

The package NER pipeline is available in `/data/de_GERNERMED-1.0.0.tar.gz` and can be installed by:  
```bash
# From local fs
python3 -m pip install ./data/de_GERNERMED-1.0.0.tar.gz

# From GitHub
python3 -m pip install https://github.com/frankkramer-lab/GERNERMED/blob/main/data/de_GERNERMED-1.0.0.tar.gz?raw=true
```  
The pipeline can be used in Python:  
```python
import spacy

nlp = spacy.load("de_GERNERMED")
doc = nlp("Dem Patienten wurde die Einnahme von Paracetamol (500 mg, zwei Tabletten täglich, 8 Wochen lang) zur Behandlung empfohlen.")

# Show entities
print(doc.ents)
```

## Reproducibility

The evaluation scores on the testset can be obtained by `./run_eval.sh`.  
The custom German dataset is stored in `/data/GERNERMED_dataset.json`.

## Citation

Long-form JMIR Formative Research paper (https://doi.org/10.2196/39077):
```
﻿@article{info:doi/10.2196/39077,
  author="Frei, Johann and Kramer, Frank",
  title="German Medical Named Entity Recognition Model and Data Set Creation Using Machine Translation and Word Alignment: Algorithm Development and Validation",
  journal="JMIR Form Res",
  year="2023",
  month="Feb",
  day="28",
  volume="7",
  pages="e39077",
  keywords="natural language processing; named entity recognition; information extraction",
  issn="2561-326X",
  doi="10.2196/39077",
  url="https://formative.jmir.org/2023/1/e39077",
  url="https://doi.org/10.2196/39077",
  url="http://www.ncbi.nlm.nih.gov/pubmed/36853741"
}
```

Short, software-focused paper at Software Impacts (https://doi.org/10.1016/j.simpa.2021.100212):
```
@article{frei_gernermed_2022,
  title = {{GERNERMED}: An open German medical {NER} model},
  volume = {11},
  issn = {2665-9638},
  url = {https://www.sciencedirect.com/science/article/pii/S2665963821000944},
  doi = {10.1016/j.simpa.2021.100212},
  pages = {100212},
  journaltitle = {Software Impacts},
  shortjournal = {Software Impacts},
  author = {Frei, Johann and Kramer, Frank},
  urldate = {2022-02-21},
  date = {2022-02-01},
  langid = {english},
  keywords = {Machine learning, Natural language processing, Clinical text mining, Named entity recognition},
}
```

The ArXiv pre-print paper from http://arxiv.org/abs/2109.12104

```
@misc{frei2021gernermed,
  title={GERNERMED -- An Open German Medical NER Model}, 
  author={Johann Frei and Frank Kramer},
  year={2021},
  eprint={2109.12104},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```
