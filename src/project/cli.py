from __future__ import annotations

import argparse
from pathlib import Path

from project.config import load_config
from project.spark_session import create_spark
from project.pipelines import ingest, transform, analyze


def main() -> int:
    parser = argparse.ArgumentParser(description="MSBX 5420 Final Project Runner")
    parser.add_argument("--config", default="configs/local.yaml", help="Path to YAML config")
    args = parser.parse_args()

    cfg = load_config(args.config)
    spark = create_spark(cfg)

    try:
        raw_path = cfg.paths.raw
        out_tables = Path(cfg.paths.outputs_tables)
        out_tables.mkdir(parents=True, exist_ok=True)

        df_raw = ingest(spark, raw_path)
        df_clean = transform(df_raw)
        df_result = analyze(df_clean)

        # Write a tiny artifact so your pipeline always produces something
        out_path = (out_tables / "analysis_counts.parquet").as_posix()
        df_result.write.mode("overwrite").parquet(out_path)

        df_result.show(truncate=False)
        print(f"\nWrote results to: {out_path}\n")
        return 0
    finally:
        spark.stop()


if __name__ == "__main__":
    raise SystemExit(main())