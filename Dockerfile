FROM python:3.10

# RUN mkdir /data
# VOLUME /data

# ENV AIApplicationAnalysis /usr/bin/src/webapp/AIApplicationAnalysis
COPY AIApplicationAnalysis/* /usr/bin/src/webapp/AIApplicationAnalysis/
# WORKDIR ${AIApplicationAnalysis}
WORKDIR /usr/bin/src/webapp/AIApplicationAnalysis
# ADD server.py server.py

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["python3", “server.py”]