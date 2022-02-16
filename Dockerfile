FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

ARG DJANGO_SECRET_KEY
ARG REDIS_URL

COPY poetry.lock pyproject.toml /app/

WORKDIR /app/

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # cleaning up unused files
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install poetry \
    && poetry config virtualenvs.create false

RUN poetry install $POETRY_INSTALL_ARGS

COPY . .

CMD python manage.py migrate --noinput \
    && python manage.py runserver 0.0.0.0:8000

