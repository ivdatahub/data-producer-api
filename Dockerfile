FROM python:3.9.6

WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install
CMD ["poetry", "run", "python", "src/run.py"]