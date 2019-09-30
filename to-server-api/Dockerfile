FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt

RUN chmod +x /app/config.sh

RUN /app/config.sh

EXPOSE 5000