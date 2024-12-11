# Demo of tests for functions used in data analysis

This repository serves as a practice ground for learning how to setup
unit tests for functions that are used in a data analysis.
This is one step away from making a Python package.

The demo data analysis is shown here:
- `report/eda.qmd`

This literate code documents calls a function, `count_classes`, 
whose function specifications and documentation lives in `src/count_classes.py`
and which aims to calculate the number observations of each class of a data set.

We will need to write the tests for `count_classes`.
They should live in `tests/test-count_classes.py`.

Once built, the test suite can be run via:

```
pytest
```

## Dependencies:
A code editor, Python and the following packages:
- pandas
- pytest
- quarto

You can also use conda or Docker to run the environments included in this repo.

### Run using conda:

#### Set-up (first time only)

1. Clone this repo, and using the command line, 
navigate to the root of this project.

2. Run the following commands to create the conda environment:

```
conda-lock install --name count_classes conda-lock.yml
```

#### Run the analysis 

Activate the conda environment:

```
conda activate count_classes
```

In the terminal run the following command:

```
quarto render report/eda.qmd
```

### Run using Docker:

1. Clone this repo, and using the command line, 
navigate to the root of this project.

2. Run the following commands to launch the container:

```
docker compose up
```

3. In the terminal, look for a URL that starts with 
`http://127.0.0.1:8888/lab?token=`. 
Copy and paste that URL into your browser. 

#### Run the analysis 

In the termina, in the root of the project, run the following command:

```
quarto render report/eda.qmd
```
