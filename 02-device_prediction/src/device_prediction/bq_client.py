"""Thin wrapper around google.cloud.bigquery for centralized BQ I/O."""

from __future__ import annotations

import logging

import pandas as pd
from google.cloud import bigquery

logger = logging.getLogger(__name__)


def get_client(project_id: str) -> bigquery.Client:
    """Return a BigQuery client for the given project."""
    return bigquery.Client(project=project_id)


def read_query(query: str, project_id: str) -> pd.DataFrame:
    """Execute a SQL query and return results as a pandas DataFrame."""
    client = get_client(project_id)
    logger.info("Executing query (%d chars) on project %s", len(query), project_id)
    df = client.query(query).to_dataframe()
    logger.info("Query returned %d rows, %d columns", len(df), len(df.columns))
    return df


def read_table(table_id: str, project_id: str) -> pd.DataFrame:
    """Read an entire BigQuery table into a pandas DataFrame."""
    client = get_client(project_id)
    logger.info("Reading table %s", table_id)
    df = client.list_rows(table_id).to_dataframe()
    logger.info("Table %s: %d rows, %d columns", table_id, len(df), len(df.columns))
    return df


def write_dataframe(
    df: pd.DataFrame,
    table_id: str,
    project_id: str,
    write_disposition: str = "WRITE_TRUNCATE",
) -> None:
    """Write a DataFrame to a BigQuery table.

    Args:
        write_disposition: WRITE_TRUNCATE (overwrite) or WRITE_APPEND.
    """
    client = get_client(project_id)
    job_config = bigquery.LoadJobConfig(
        write_disposition=write_disposition,
        create_disposition="CREATE_IF_NEEDED",
        schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION],
    )
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()
    logger.info("Wrote %d rows to %s (%s)", len(df), table_id, write_disposition)
