"""Configuration management for Digital Marketing Analytics Platform"""

from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support"""

    # Database
    database_url: str = "postgresql://user:password@localhost:5432/marketing_db"
    db_pool_size: int = 20
    db_max_overflow: int = 10

    # Airflow
    airflow_home: str = "/usr/local/airflow"
    airflow_dags_folder: str = "airflow/dags"

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    # ML Models
    churn_model_path: str = "models/churn_model.pkl"
    ltv_model_path: str = "models/ltv_model.pkl"

    # Attribution
    attribution_lookback_days: int = 90
    min_touch_frequency: int = 2

    # Environment
    environment: str = "development"
    debug: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
