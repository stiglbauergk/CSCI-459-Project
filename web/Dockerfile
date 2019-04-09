FROM django

ADD . /459-project

WORKDIR /459-project

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
