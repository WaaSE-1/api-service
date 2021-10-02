FROM python:3.8

ADD src /app/src
ADD requirements.txt /app
ADD main.py /app

WORKDIR /app

ENV DB_HOSTNAME={DB_HOSTNAME}
ENV DB_USERNAME={DB_USERNAME}
ENV DB_PASSWORD={DB_PASSWORD}
ENV DB_DATABASE={DB_DATABASE}
ENV JWT_SECRET={JWT_SECRET}

RUN pip install --upgrade pip && \
pip install -r ./requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]