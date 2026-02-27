from __future__ import annotations

from pyspark.sql import DataFrame, functions as F


def ingest(spark, raw_path: str) -> DataFrame:
    # Placeholder: you'll replace this once you know the dataset format
    # Examples: spark.read.csv(...), spark.read.parquet(...), etc.
    return spark.read.option("header", True).csv(raw_path)


def transform(df: DataFrame) -> DataFrame:
    # Placeholder transforms: safe defaults
    # (You’ll replace with real cleaning/feature engineering)
    return (
        df
        .withColumn("_ingested_at", F.current_timestamp())
    )


def analyze(df: DataFrame) -> DataFrame:
    # Placeholder analysis: simple row count
    return df.groupBy().count()