FROM python:3.9-slim

# Defina a variável de ambiente para não gerar bytecode compilado
ENV PYTHONDONTWRITEBYTECODE=1

# Defina a variável de ambiente para não armazenar buffer em stdout/stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instale as dependências do sistema e as ferramentas necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Instale pip, poetry e dependências
RUN pip install --upgrade pip \
    && pip install poetry

# Copie apenas os arquivos necessários para instalar as dependências
COPY pyproject.toml poetry.lock ./

# Instale as dependências usando Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copie o restante dos arquivos para o diretório de trabalho
COPY . .

# Configure o Flask
ENV FLASK_APP=src/app.py

# Exponha a porta que o Flask está utilizando
EXPOSE 8080

# Comando para iniciar o Flask quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
