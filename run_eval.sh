#!/usr/bin/env bash

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# [Not needed:] Generate spacy config.cfg
# python3 -m spacy init fill-config base_config.cfg config.cfg

# Run evaluation
python3 -m spacy evaluate ./gernermed_pipeline ./data/ner_medical.test.spacy
