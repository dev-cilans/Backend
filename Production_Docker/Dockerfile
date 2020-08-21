FROM tiangolo/uvicorn-gunicorn-fastapi
COPY ../src/ /app
COPY ../requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en-core-web-lg
