from __future__ import annotations

from pyspark.sql import SparkSession
from project.config import AppConfig


def create_spark(cfg: AppConfig) -> SparkSession:
    builder = SparkSession.builder.appName(cfg.app_name)

    # Local dev uses an explicit master; clusters usually provide it.
    if cfg.spark.master:
        builder = builder.master(cfg.spark.master)

    spark = builder.getOrCreate()

    # A common tuning knob you'll reference in class
    spark.conf.set("spark.sql.shuffle.partitions", str(cfg.spark.shuffle_partitions))

    return spark