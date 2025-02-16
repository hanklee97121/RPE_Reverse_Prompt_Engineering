# Reverse Prompt Engineering (RPE) Implementation

This repository contains an implementation of [Reverse Prompt Engineering](https://arxiv.org/abs/2411.06729) (RPE) that infers the underlying prompt based on outputs from large language models (LLMs).


## Repository Structure

- **RPE_ga.py**:  
  Contains the main functions for reverse prompt engineering. This module implements the core algorithm that deduces the hidden prompt from given LLM outputs.

- **RPE_GA_experiment.py**:  
  Provides a script with example experiments demonstrating how to use the reverse prompt engineering functions.

- **RPE_GA_experiment.ipynb**:  
  A Jupyter Notebook with interactive examples.

- **Dataset/**:  
  Contains the datasets used in the experiments. Ensure that this folder is properly populated with the required data files before running the experiments.

- **result/**:  
  Stores the results generated from experiments. This folder will be updated with new outputs each time you run the experiments.

## Requirements

You can install the necessary packages using:

```bash
pip install -r requirements.txt
```

## License
**This repository is released under MIT license.**
