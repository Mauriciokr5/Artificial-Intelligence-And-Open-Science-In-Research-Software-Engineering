FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "iaop", "/bin/bash", "-c"]

# Demonstrate the environment is activated:
# RUN echo "Make sure wordcloud is installed:"
# RUN python -c "import wordcloud"

# The code to run when container is started:
COPY getInfoTEI.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "iaop", "python", "getInfoTEI.py"]