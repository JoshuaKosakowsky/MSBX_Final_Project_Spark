from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass(frozen=True)
class Paths:
    raw: str
    processed: str
    outputs_tables: str
    outputs_figures: str


@dataclass(frozen=True)
class SparkCfg:
    master: str | None
    shuffle_partitions: int


@dataclass(frozen=True)
class AppConfig:
    app_name: str
    env: str
    paths: Paths
    spark: SparkCfg


def load_config(path: str | Path) -> AppConfig:
    p = Path(path)
    data = yaml.safe_load(p.read_text(encoding="utf-8"))

    return AppConfig(
        app_name=data["app_name"],
        env=data["env"],
        paths=Paths(**data["paths"]),
        spark=SparkCfg(**data["spark"]),
    )