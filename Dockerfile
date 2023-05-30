FROM python:3.10

WORKDIR /home/Carpoint/carpoint

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apt update
RUN apt install -y postgresql python3-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
# copy project
COPY . .


ENTRYPOINT ["/home/Carpoint/carpoint/entrypoint.sh"]
