FROM tiangolo/uvicorn-gunicorn-fastapi
COPY src/ /app
RUN mkdir /app/test/
COPY tests/ /app/test/
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
