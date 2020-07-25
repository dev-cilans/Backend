FROM tiangolo/uvicorn-gunicorn-fastapi
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
