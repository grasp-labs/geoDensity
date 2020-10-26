# Pull base image
FROM python:3.7

# setting folder
# RUN cd / src
# set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /code

# install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# copy project and start script
COPY . /code/
COPY ./docker/start.sh /start.sh

# run start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh
