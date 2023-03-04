# PDF-Analyzer
**A project for the subject of artificial intelligence and open science in research software engineering.**

[![DOI](https://zenodo.org/badge/597722448.svg)](https://zenodo.org/badge/latestdoi/597722448)

**Author:** Roberto Mauricio Beltrán Vargas

The aim of PDF-Analyzer is to help automatically extract metadata and text from scientific papers in PDF format to get key words, links and compare the number of figures in each paper. 


## Features
Given a set of 10 (or less) PDF file, PDF-Analyzer will do the following tasks:

- **Keyword cloud**: Draw a keyword cloud for each file based on the abstract information
- **Count figures**: Create a visualization showing the number of figures per article.
- **List links**: Create a list of the links found in each paper.

## Used Technologies and Standards

### GROBID
[GROBID](https://grobid.readthedocs.io/en/latest/)  (GeneRation Of BIbliographic Data) is an open-source machine learning tool for extracting and parsing bibliographic information from scholarly articles in PDF format. It is designed to extract various types of metadata from research articles, including title, abstract, authors, affiliations, references, and other bibliographic information.

### TEI XML
TEI XML stands for Text Encoding Initiative Extensible Markup Language. It is a markup language used for the digital representation of texts in the humanities and social sciences. 

### Beautiful Soup
[Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)  is a Python library used for web scraping purposes to extract data from HTML and XML documents. It provides a simple way to navigate and search the HTML tree structure, allowing the user to extract specific data from the document based on tags, attributes, and other HTML elements.

### Matplotlib
[Matplotlib](https://matplotlib.org/) is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

### WordCloud
[WordCloud](https://pypi.org/project/wordcloud/) is a library that provides a simple way to generate word clouds from text data. The library takes a text file or a string of text as input and produces a wordcloud image as output.




