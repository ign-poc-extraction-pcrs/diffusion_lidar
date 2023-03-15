FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN mkdir -p /api
WORKDIR /api/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
