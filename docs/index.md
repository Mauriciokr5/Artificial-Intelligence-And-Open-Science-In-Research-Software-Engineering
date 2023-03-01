# Software Metadata Extraction Framework (SOMEF) 
**Authors:** Daniel Garijo, Allen Mao, Miguel Ángel García Delgado, Haripriya Dharmala, Vedant Diwanji, Jiaying Wang, Aidan Kelley and Jenifer Tabita Ciuciu-Kiss.

The aim of SOMEF is to help automatically extract metadata from scientific software from their readme files and GitHub repositories and make it available in a machine-readable manner. Thanks to SOMEF, we can populate knowedge graphs of scientific software metadata and relate different software together.

SOMEF has currently been tested with GitHub repositories, but it can extract metadata from any readme file written in mardown syntax.


## Features
Given a readme file (or a GitHub repository) SOMEF will extract the following categories (if present):

- **Name**: Name identifying a software component
- **Full name**: Name + owner (owner/name)