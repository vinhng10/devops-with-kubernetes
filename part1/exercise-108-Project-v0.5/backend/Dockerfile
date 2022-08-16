FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirements.txt /code
RUN pip3 install --no-cache-dir -r requirements.txt 
COPY ./app /code/app
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0" ]