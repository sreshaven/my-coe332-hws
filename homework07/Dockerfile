FROM python:3.8.10

ENV REDIS_IP redis-db

RUN pip install Flask==2.2.0 
RUN pip install redis==4.5.1 
RUN pip install requests==2.22.0

ADD ./auto_trends_data.csv /auto_trends_data.csv
ADD ./auto_trends_api.py /auto_trends_api.py

CMD ["python", "/auto_trends_api.py"]
