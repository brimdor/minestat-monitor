FROM python:3

#prep folder structure
RUN mkdir -p /tmp
RUN mkdir -p /minestat
RUN mkdir -p /minestat-logs

#set working directory to app directory
WORKDIR /minestat

#install minestat
COPY . /minestat/
RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python3","minestat.py"]