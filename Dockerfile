FROM mcr.microsoft.com/devcontainers/python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements/dev-requirements.txt ./

# RUN apt-get update \
#   && apt-get install -y \
#   libcairo2 \
#   libgdk-pixbuf2.0-0 \
#   liblcms2-2 \
#   libopenjp2-7 \
#   libpango-1.0-0 \
#   libpangocairo-1.0-0 \
#   libssl3 \
#   libtiff6 \
#   libwebp7 \
#   libxml2 \
#   libpq5 \
#   shared-mime-info \
#   mime-support

RUN pip install --no-cache-dir -r dev-requirements.txt

# RUN apt-get remove -y \
#       gcc \
#       pkg-config && \
#     rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000