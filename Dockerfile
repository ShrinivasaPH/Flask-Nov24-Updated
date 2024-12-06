FROM python:3.12.7-bookworm
WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#Can rename the file name below
ENV FLASK_APP=loan_app.py 

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

