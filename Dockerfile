FROM python:3.8-slim
LABEL Maintainer "MikeTeddyOmondi <mike_omondi@outlook.com>"

ENV PYTHONUNBUFFERED 1

RUN apt-get update && python -m pip install --upgrade pip && rm -rf /var/lib/apt/lists/*

RUN mkdir /src
WORKDIR /src

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh

#COPY ./migrations.sh /src/migrations.sh
#RUN sed -i 's/\r//' /src/migrations.sh
#RUN chmod +x /src/migrations.sh
#RUN chown user /src/migrations.sh

#RUN adduser -D user
#USER user

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "manage.py",  "runserver", "0.0.0.0:8000"]