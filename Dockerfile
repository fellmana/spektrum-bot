 
FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
    ffmpeg  && \ 
    useradd -m ruben

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD ./bot /opt/bot/

USER ruben
WORKDIR /opt/bot

CMD ["python", "bot.py"]