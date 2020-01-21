FROM python:3.7
MAINTAINER shamshad alam "shams.alam.1996@gmail.com"

WORKDIR /app
COPY source_code/ /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
