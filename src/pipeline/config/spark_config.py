from enum import Enum
from pyspark import SparkConf
from src.pipeline.config.common import EnvSetup


class SparkConfig:
    def __init__(self, env: EnvSetup):
        self.env = env

    def get_pipeline_options(self):
        if self.env == EnvSetup.PROD:
            conf = SparkConf() \
                .setAppName("PubSubToConsole") \
                .set("spark.jars.packages", "com.google.cloud:google-cloud-pubsub:1.99.0") \
                .setMaster("local[*]") \
                .set("spark.log.level", "INFO")
        else:
            conf = SparkConf() \
                .setAppName("PubSubToConsole") \
                .set("spark.jars.packages", "com.google.cloud:google-cloud-pubsub:1.99.0") \
                .setMaster("local[*]")

        return conf

