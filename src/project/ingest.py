from pyspark.sql import SparkSession, DataFrame
from pathlib import Path

def ingest(spark: SparkSession, path: str) -> DataFrame:
    """
    Load raw data into a Spark DataFrame.

    If no data exists, returns a small sample DataFrame
    so the pipeline can still run.
    """
    p = Path(path)

    if p.exists() and list(p.glob("*.csv")):
        return spark.read.option("header", True).csv(str(p / "*.csv"))

    # Fallback sample data
    return spark.createDataFrame(
        [(1, "sample"), (2, "data")],
        ["id", "value"]
    )