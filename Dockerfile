FROM ubuntu
USER root
RUN apt-get update
RUN apt-get install -y python3 \
        && apt-get install -y python3-pip \
        && apt-get install -y wget \
        && apt-get install -y gettext
RUN wget https://telegrafreleases.blob.core.windows.net/linux/telegraf
RUN chmod +rwx telegraf
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY telegraf_postgres.conf .
COPY dockerexec.sh .
COPY app.py .
CMD ["sh","dockerexec.sh"]