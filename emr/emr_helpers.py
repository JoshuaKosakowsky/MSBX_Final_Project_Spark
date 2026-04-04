from pyspark.sql import DataFrame, functions as F
from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, DoubleType, LongType,
    TimestampType, DateType
)

TRANSACTION_SCHEMA = StructType([
    StructField("Unnamed: 0", LongType(), True),
    StructField("trans_date_trans_time", TimestampType(), True),
    StructField("cc_num", StringType(), True),
    StructField("merchant", StringType(), True),
    StructField("category", StringType(), True),
    StructField("amt", DoubleType(), True),
    StructField("first", StringType(), True),
    StructField("last", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("street", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("zip", StringType(), True),
    StructField("lat", DoubleType(), True),
    StructField("long", DoubleType(), True),
    StructField("city_pop", IntegerType(), True),
    StructField("job", StringType(), True),
    StructField("dob", DateType(), True),
    StructField("trans_num", StringType(), True),
    StructField("unix_time", LongType(), True),
    StructField("merch_lat", DoubleType(), True),
    StructField("merch_long", DoubleType(), True),
    StructField("is_fraud", IntegerType(), True),
    StructField("merch_zipcode", StringType(), True),
])

def prepare_transactions(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("event_date", F.to_date("trans_date_trans_time"))
        .withColumn("event_hour", F.hour("trans_date_trans_time"))
        .withColumn("event_dayofweek", F.dayofweek("trans_date_trans_time"))
        .withColumn("age", F.floor(F.datediff(F.current_date(), F.col("dob")) / F.lit(365.25)))
        .withColumn("amt_log", F.log1p("amt"))
    )