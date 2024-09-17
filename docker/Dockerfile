# Python tasviridan foydalanamiz
FROM python:3.10.4-slim as python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# Ilova katalogini yaratamiz
# RUN mkdir /web
WORKDIR /web

#
# Install dependencies
COPY requirements.txt /web/requirements.txt

RUN pip install -r /web/requirements.txt

# Copy the rest of the application code
COPY . /web

# Copy scripts (ensure the path is correct)
COPY scripts/ /scripts/
# RUN chmod +x /entrypoint.sh
# RUN chmod +x /start.sh


# Django serverini ishga tushirish uchun
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8014"]


RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh && \
    sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh