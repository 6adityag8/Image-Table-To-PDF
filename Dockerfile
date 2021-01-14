# Base Image
FROM python:3.6

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set port to '8888' to avoid conflict with the default port: '8000'
ENV PORT=8888

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        wkhtmltopdf \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Install project dependencies
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

# Run migrate and collect static commands
RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8888
CMD gunicorn image_table_to_pdf.wsgi:application --bind 0.0.0.0:$PORT