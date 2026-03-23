from pyspark.sql import DataFrame

def analyze(df: DataFrame) -> DataFrame:
    """
    Simple analysis step (row count).
    """
    return df.groupBy().count()