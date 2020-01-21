FROM python:3.7
MAINTAINER shamshad alam "shams.alam.1996@gmail.com"
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
