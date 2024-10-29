FROM python:3.11-bookworm

COPY . /pipeline
WORKDIR /pipeline

RUN pip install -r requirements.txt
    
ENTRYPOINT [ "python", "pipeline.py" ]