# FROM python:3.11

# ENV PYTHONUNBUFFERED=1  

# WORKDIR /code

# ENV PYTHONDONTWRITEBYTECODE=1

# COPY requirements.txt .

# RUN pip install --upgrade pip  

# RUN pip install -r requirements.txt 

# COPY . .

# EXPOSE 8000  

# CMD python3 manage.py runserver  
FROM python:3.11

ENV PYTHONUNBUFFERED=1
WORKDIR /code

# Create a non-root user
RUN adduser --disabled-password --gecos '' myuser

# Set permissions for the application folder
RUN chown -R myuser:myuser /code

USER myuser

ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
