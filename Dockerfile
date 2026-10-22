FROM python:3.12

WORKDIR /opt/flask_scorepredictor

COPY . .

RUN pip install -r requirements.txt

RUN python model.py

EXPOSE 5000

CMD ["python", "flaskapp.py"]
