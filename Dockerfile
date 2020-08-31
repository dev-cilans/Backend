FROM tiangolo/uvicorn-gunicorn-fastapi
COPY src/ /app
RUN mkdir /app/tests/
COPY tests/ /app/tests/
COPY tests/test-requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en-core-web-lg

