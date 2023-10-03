FROM python:3.11.6-alpine3.18

WORKDIR /app

ARG URL=http://siem.yandex.ru/input
ARG FILE_PATH=/var/log/data.csv
RUN crontab -l | { cat; echo "00 * * * * python3 /app/sender.py ${FILE_PATH} ${URL}"; } | crontab -

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY sender.py .

CMD crond -f