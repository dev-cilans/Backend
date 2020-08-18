FROM tiangolo/uvicorn-gunicorn-fastapi
COPY src/ /app
RUN mkdir /app/tests/
COPY tests/ /app/tests/
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
