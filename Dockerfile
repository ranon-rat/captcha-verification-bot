FROM python:alpine
WORKDIR /
COPY . ./captcha-bot
WORKDIR /captcha-bot/
RUN apk update && apk upgrade && apk add build-base
RUN apk add sqlite && pip3 install -r requirements.txt
#RUN cat app/sql/init.sql | sqlite3 app/sql/database.db
CMD ["bash"]
#CMD ["python3","main.py"]