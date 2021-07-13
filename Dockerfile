FROM tiangolo/uvicorn-gunicorn-fastapi
COPY ./src/ /app
COPY ./requirements.txt /app
COPY ./.env /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn","main:app"]