from pyspark.sql import SparkSession

spark_session = SparkSession.builder \
    .appName("PubSubToConsole") \
    .config("spark.jars.packages", "com.google.cloud:google-cloud-pubsub:1.131.0") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .config("spark.driver.host", "127.0.0.1") \
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
