# PDF-Analyzer
**A project for the subject of artificial intelligence and open science in research software engineering.**

[![DOI](https://zenodo.org/badge/597722448.svg)](https://zenodo.org/badge/latestdoi/597722448)

**Author:** Roberto Mauricio Beltrán Vargas

The aim of PDF-Analyzer is to help automatically extract metadata and text from scientific papers in PDF format to get key words, links and compare the number of figures in each paper. 


### Features
Given a set of 10 (or less) PDF file, PDF-Analyzer will do the following tasks:

- **Keyword cloud**: Draw a keyword cloud for each file based on the abstract information
- **Count figures**: Create a visualization showing the number of figures per article.
- **List links**: Create a list of the links found in each paper.
***
##### Documentation: https://pdfanalyzer.readthedocs.io/en/latest/
***
## Installing PDF-Analyzer
### Requirements

- Docker-20.10.20 or higher 
or
- Miniconda 3 ([Instructions](https://pdfanalyzer.readthedocs.io/en/latest/install/#conda))


To install PDF-Analyzer just clone this GitHub repository:
```
git clone https://github.com/Mauriciokr5/PDF-Analyzer.git
```
This project is easier to use if you have Docker. If you don't have it, see the documentation [here](https://pdfanalyzer.readthedocs.io/en/latest/install/#conda) to prepare a **conda** environment to run it.

***
## Using PDF-Analyzer
Go to the path ```./Files/PDFs/``` and place the articles you want to analyze, only a maximum of 10 files can be analyzed.

With docker installed and running, go to the root path of the project and execute:
```
docker compose up
```
It is going to take some minutes to analyze all files. 

All output files are going to be store in ```./Files/output/```.

Once it finish, execute the command below to delete all the containers.
```
docker compose down
```
