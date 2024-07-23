# Use uma imagem base do Apache Spark
FROM spark

# Copie o arquivo Python do job Spark para dentro do container
COPY pipeline.py /opt/spark/jobs/

# Defina a variável de ambiente PYTHONPATH
ENV PYTHONPATH=/opt/spark/jobs

# Comando padrão a ser executado quando o container for iniciado
CMD ["/opt/spark/bin/spark-submit", "/opt/spark/jobs/pipeline.py"]
