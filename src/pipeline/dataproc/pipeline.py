from pyspark.sql import SparkSession

spark_session = SparkSession.builder \
    .appName("PubSubToConsole") \
    .config("spark.jars.packages", "com.google.cloud:google-cloud-pubsub:1.131.0") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.port", "8888") \
    .config("spark.driver.extraJavaOptions", "-Djava.net.preferIPv4Stack=true") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "4") \
    .config("spark.executor.instances", "1") \
    .config("spark.logConf", "true") \
    .config("spark.log.level", "INFO") \
    .config("spark.sql.streaming.checkpointLocation", ".") \
    .config("spark.sql.streaming.schemaInference", "true") \
    .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true") \
    .config("spark.sql.streaming.minBatchesToRetain", "1") \
    .config("spark.sql.streaming.maxBatchesToRetain", "1") \
    .config("spark.sql.streaming.noDataMicroBatchesEnabled", "true") \
    .config("spark.sql.streaming.noDataMicroBatchesNum", "1") \
    .config("spark.sql.streaming.pollingDelay", "1") \
    .config("spark.sql.streaming.streamingQueryListeners", "org.apache.spark.sql.streaming.StreamingQueryListener") \
    .config("spark.sql.streaming.streamingQueryListeners.org.apache.spark.sql.streaming.StreamingQueryListener", "org.apache.spark.sql.streaming.StreamingQueryListener") \
    .getOrCreate()



project_id = "ivanildobarauna"
subscription = "projects/ivanildobarauna/subscriptions/gcp-streaming-pipeline-sub-bq"

# Lê dados do Pub/Sub
df = spark_session.readStream \
    .format("pubsub") \
    .option("project", project_id) \
    .option("subscription", f"projects/{project_id}/subscriptions/{subscription}") \
    .load()


messages = df.selectExpr("CAST(data AS STRING)")


query = messages.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()


query.awaitTermination()
