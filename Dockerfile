FROM python:3.10.1

WORKDIR /home/

RUN git clone https://github.com/minwoonggi/django_intj.git

WORKDIR /home/intj/

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-t54*8wogldcp@1it9l4r7^+u#52l^apv!9-#=k69y6+ncptm&@"> .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]