"""CLI entry points for the device prediction pipeline.

Supports both full pipeline runs and individual step execution.
"""

from __future__ import annotations

import argparse
import logging
import sys
import warnings
from pathlib import Path

# Suppress known non-critical warnings
warnings.filterwarnings("ignore", message=".*authenticated using end user credentials.*")
warnings.filterwarnings("ignore", message=".*BigQuery Storage module not found.*")

from device_prediction.config import load_config
from device_prediction.pipeline import (
    DEFAULT_DATA_DIR,
    run_device_enrichment,
    run_scoring_pipeline,
    run_training_pipeline,
    step_device_history,
    step_encode,
    step_extract,
    step_features,
    step_predict,
    step_statistics,
    step_target,
    step_train,
    step_write_scores,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="device-prediction",
        description="Device change prediction using survival analysis",
    )
    parser.add_argument(
        "--config", default=None,
        help="Path to YAML config file (default: config/default.yaml)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Enable debug logging",
    )
    parser.add_argument(
        "--data-dir", default=str(DEFAULT_DATA_DIR),
        help="Directory for intermediate parquet files (default: data/intermediate)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # ── Full pipeline commands ───────────────────────────────────────
    train_parser = subparsers.add_parser(
        "train", help="Run the FULL training pipeline (all steps)"
    )
    train_parser.add_argument("--model-path", default="models/latest")
    train_parser.add_argument("--skip-enrichment", action="store_true")

    score_parser = subparsers.add_parser(
        "score", help="Run the FULL scoring pipeline (all steps)"
    )
    score_parser.add_argument("--model-path", default="models/latest")

    subparsers.add_parser(
        "enrich-devices", help="Run device features enrichment only"
    )

    # ── Individual step commands ─────────────────────────────────────
    subparsers.add_parser(
        "step-enrich",
        help="Step 0: Enrich missing device features via LLM agent",
    )

    step_extract_p = subparsers.add_parser(
        "step-extract",
        help="Step 1: Extract subscription history from BigQuery",
    )
    step_extract_p.add_argument(
        "--mode", choices=["train", "score"], default="train",
    )

    step_history_p = subparsers.add_parser(
        "step-device-history",
        help="Step 2: Build cleaned device change history",
    )
    step_history_p.add_argument(
        "--mode", choices=["train", "score"], default="train",
    )

    step_stats_p = subparsers.add_parser(
        "step-statistics",
        help="Step 3: Compute subscriber/market/device-model statistics",
    )
    step_stats_p.add_argument(
        "--mode", choices=["train", "score"], default="train",
    )

    step_feat_p = subparsers.add_parser(
        "step-features",
        help="Step 4: Build feature matrix (joins all data sources)",
    )
    step_feat_p.add_argument(
        "--mode", choices=["train", "score"], default="train",
    )

    subparsers.add_parser(
        "step-target",
        help="Step 5: Construct survival target (train only)",
    )

    step_enc_p = subparsers.add_parser(
        "step-encode",
        help="Step 6: Run preprocessing/encoding pipeline",
    )
    step_enc_p.add_argument(
        "--mode", choices=["train", "score"], default="train",
    )
    step_enc_p.add_argument("--model-path", default="models/latest")

    step_train_p = subparsers.add_parser(
        "step-train",
        help="Step 7: Train and evaluate survival model",
    )
    step_train_p.add_argument("--model-path", default="models/latest")

    step_pred_p = subparsers.add_parser(
        "step-predict",
        help="Step 8: Predict survival curves",
    )
    step_pred_p.add_argument("--model-path", default="models/latest")

    subparsers.add_parser(
        "step-write-scores",
        help="Step 9: Write predictions to BigQuery",
    )

    args = parser.parse_args()

    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    cfg = load_config(args.config)
    data_dir = Path(args.data_dir)

    # ── Dispatch ─────────────────────────────────────────────────────
    if args.command == "train":
        metrics = run_training_pipeline(
            cfg, model_output_path=args.model_path,
            skip_enrichment=args.skip_enrichment, data_dir=data_dir,
        )
        print("\n=== Training Metrics ===")
        for k, v in metrics.items():
            print(f"  {k}: {v}")

    elif args.command == "score":
        output = run_scoring_pipeline(cfg, model_path=args.model_path, data_dir=data_dir)
        print(f"\nScoring complete: {len(output)} predictions generated")

    elif args.command in ("enrich-devices", "step-enrich"):
        result = run_device_enrichment(cfg)
        print(f"\nEnrichment complete: {len(result)} devices enriched")

    elif args.command == "step-extract":
        step_extract(cfg, mode=args.mode, data_dir=data_dir)

    elif args.command == "step-device-history":
        step_device_history(cfg, mode=args.mode, data_dir=data_dir)

    elif args.command == "step-statistics":
        step_statistics(cfg, mode=args.mode, data_dir=data_dir)

    elif args.command == "step-features":
        step_features(cfg, mode=args.mode, data_dir=data_dir)

    elif args.command == "step-target":
        step_target(cfg, data_dir=data_dir)

    elif args.command == "step-encode":
        step_encode(cfg, mode=args.mode, model_path=Path(args.model_path), data_dir=data_dir)

    elif args.command == "step-train":
        step_train(cfg, model_path=Path(args.model_path), data_dir=data_dir)

    elif args.command == "step-predict":
        step_predict(cfg, model_path=Path(args.model_path), data_dir=data_dir)

    elif args.command == "step-write-scores":
        step_write_scores(cfg, data_dir=data_dir)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
