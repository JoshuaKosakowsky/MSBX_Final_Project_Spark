from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp

def transform(df: DataFrame) -> DataFrame:
    """
    Basic transformation step.
    """
    return df.withColumn("processed_at", current_timestamp())