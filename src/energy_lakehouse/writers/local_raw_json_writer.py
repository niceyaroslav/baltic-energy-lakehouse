import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class RawJsonWriter:
    def __init__(self, base_path: str | Path):
        self.base_path = Path(base_path)

    def write(self, dataset: str, data: dict[str, Any]) -> Path:
        metadata = data.get("metadata", {})
        source = metadata.get("source", "unknown")

        ingested_at = datetime.now(timezone.utc)
        request_id = str(uuid.uuid4())

        partition = {
            "source": source,
            "ingestion_date": ingested_at.date().isoformat(),
        }

        target_dir = self._build_partition_path(dataset, partition)
        target_dir.mkdir(parents=True, exist_ok=True)

        target_path = target_dir / f"{request_id}.json"

        record = {
            "metadata": {
                **metadata,
                "request_id": request_id,
                "ingested_at": ingested_at.isoformat(),
            },
            "payload": data.get("payload"),
        }

        with target_path.open("w", encoding="utf-8") as file:
            json.dump(record, file, ensure_ascii=False, indent=2, default=str)

        return target_path

    def _build_partition_path(self, dataset: str, partition: dict[str, str]) -> Path:
        path = self.base_path / dataset

        for key, value in partition.items():
            path = path / f"{key}={value}"

        return path