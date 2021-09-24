FROM python:3.8

ADD src /app/src
ADD requirements.txt /app
ADD main.py /app

WORKDIR /app

RUN pip install --upgrade pip && \
pip install -r ./requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]