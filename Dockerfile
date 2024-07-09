FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

# Copie apenas os arquivos necessários para instalar as dependências
COPY pyproject.toml poetry.lock ./

# Instale as dependências usando Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copie o restante dos arquivos para o diretório de trabalho
COPY . .

# Instale o Flask
RUN pip install flask

# Configure o Flask
ENV FLASK_APP=./src/app.py

# Exponha a porta que o Flask está utilizando
EXPOSE 8080

# Comando para iniciar o Flask quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
