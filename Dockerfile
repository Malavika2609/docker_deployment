FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
RUN pip install --upgrade flask
RUN pip install --upgrade jinja2
RUN pip install --upgrade flasgger
CMD ["python", "flask_api.py"]