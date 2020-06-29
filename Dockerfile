FROM python:3
MAINTAINER Roman Speranskii

#Need to download from GIT https://github.com/romsper/telegram-reminder-bot/archive/master.zip

WORKDIR telegram-reminder-bot
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./bot.py"]