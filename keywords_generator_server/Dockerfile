FROM python:3.6-slim
ADD . /keywords_generator_server
WORKDIR /keywords_generator_server
RUN pip install -r requirements.txt
EXPOSE 9999
CMD ["python", "manage.py", "runserver", "9999"]
