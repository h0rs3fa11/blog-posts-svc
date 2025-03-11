FROM python:3.13

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install --no-root

COPY flaskblog /app/flaskblog
COPY instance /app/instance
COPY run.py /app/run.py

EXPOSE 5000

CMD ["poetry", "run", "python", "run.py"]