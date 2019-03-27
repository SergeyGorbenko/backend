FROM python:3.6-slim
ADD . /rest_api_server
WORKDIR /rest_api_server
RUN pip install -r requirements.txt
EXPOSE 8000
RUN ["python", "manage.py", "runserver"]
