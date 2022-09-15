FROM python:3.10
RUN apt-get update 
RUN apt-get install -y ffmpeg ttf-wqy-microhei


RUN mkdir /VideoScaleChanger
WORKDIR /VideoScaleChanger

ADD requirements.txt /VideoScaleChanger
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /VideoScaleChanger


CMD ["python","manage.py","migrate"]
CMD ["celery","-A","VideoScaleChanger","worker","--loglevel=info"]
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]