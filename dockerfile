FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "iaop", "/bin/bash", "-c"]

COPY getInfoTEI.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "iaop", "python", "getInfoTEI.py"]