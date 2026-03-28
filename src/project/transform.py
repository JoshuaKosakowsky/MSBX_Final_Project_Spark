from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean_transactions(df: DataFrame) -> DataFrame:
    """
    Basic cleanup and normalization for transaction data.
    Assumes the schema has already applied the main data types.
    """
    return (
        df
        .withColumn("merchant", F.trim(F.col("merchant")))
        .withColumn("category", F.trim(F.col("category")))
        .withColumn("first", F.trim(F.col("first")))
        .withColumn("last", F.trim(F.col("last")))
        .withColumn("city", F.trim(F.col("city")))
        .withColumn("state", F.upper(F.trim(F.col("state"))))
        .withColumn("zip", F.trim(F.col("zip")))
        .withColumn("merch_zipcode", F.trim(F.col("merch_zipcode")))
    )


def add_time_features(df: DataFrame) -> DataFrame:
    """
    Add time-based analytical features from transaction timestamp.
    Assumes trans_date_trans_time is already TimestampType.
    """
    return (
        df
        .withColumn("event_date", F.to_date(F.col("trans_date_trans_time")))
        .withColumn("event_hour", F.hour(F.col("trans_date_trans_time")))
        .withColumn("event_month", F.month(F.col("trans_date_trans_time")))
        .withColumn("event_dayofweek", F.dayofweek(F.col("trans_date_trans_time")))
        .withColumn("event_weekofyear", F.weekofyear(F.col("trans_date_trans_time")))
    )


def add_customer_features(df: DataFrame) -> DataFrame:
    """
    Add customer-derived features such as age and full name.
    Assumes dob is already DateType.
    """
    return (
        df
        .withColumn(
            "age",
            F.floor(F.datediff(F.current_date(), F.col("dob")) / F.lit(365.25))
        )
        .withColumn(
            "customer_name",
            F.concat_ws(" ", F.col("first"), F.col("last"))
        )
    )


def add_amount_features(df: DataFrame) -> DataFrame:
    """
    Add amount-related derived fields.
    Assumes amt is numeric.
    """
    return (
        df
        .withColumn("amt_log", F.log1p(F.col("amt")))
    )


def prepare_transactions(df: DataFrame) -> DataFrame:
    """
    One-stop transformation pipeline for analysis and streaming.
    """
    return (
        df.transform(clean_transactions)
          .transform(add_time_features)
          .transform(add_customer_features)
          .transform(add_amount_features)
    )