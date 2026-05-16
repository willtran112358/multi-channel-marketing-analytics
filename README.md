# XPON Multi-Channel Marketing Analytics

> Marketing intelligence platform for **XPON** (Australia) — deep integration with **Google Analytics 4**, **Google Cloud Platform** (BigQuery, Pub/Sub, Dataflow), and multi-channel campaign data for Australian enterprise clients.

XPON implements and operates GA / GCP analytics stacks for clients across Australia. This repo models the **end-to-end pipeline**: GA4 & ads exports → GCP landing → attribution marts → churn/LTV ML → Streamlit dashboards.

## Overview

- **GA4** event export & BigQuery daily/sharded tables
- **GCP**: BigQuery (warehouse), Pub/Sub (streaming), optional Dataflow/Beam transforms
- Multi-channel ingestion: email, paid search, social, web, CRM
- Attribution: first/last/linear and ML-assisted credit
- Churn & LTV scoring with confidence intervals
- Campaign ROI, CAC, and A/B test significance

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Web analytics** | Google Analytics 4, GA4 BigQuery Export |
| **Cloud** | GCP BigQuery, Cloud Storage, Pub/Sub |
| **Pipeline** | Python 3.10+, Pandas, PySpark (optional) |
| **Warehouse modeling** | dbt (BigQuery adapter) |
| **ML** | scikit-learn, XGBoost |
| **Dashboard** | Streamlit, Plotly |
| **Orchestration** | Airflow / Cloud Composer patterns |
| **CI/CD** | GitHub Actions |

## Architecture

```mermaid
graph TB
    GA4["GA4 Properties<br/>Web & App events"] --> BQ["BigQuery<br/>analytics_* datasets"]
    ADS["Google Ads / CM360"] --> BQ
    CRM["CRM / Email ESP"] --> BQ

    BQ --> BRONZE["Bronze<br/>Raw event tables"]
    BRONZE --> SILVER["Silver<br/>Sessionize & dedupe"]
    SILVER --> GOLD["Gold<br/>Attribution & KPIs"]

    GOLD --> DBT["dbt marts<br/>Tests & docs"]
    DBT --> ML["ML<br/>Churn • LTV"]
    DBT --> DASH["Streamlit<br/>XPON client dashboards"]

    style GA4 fill:#e8f5e9,stroke:#2e7d32
    style BQ fill:#4285f4,stroke:#fff,color:#fff
    style GOLD fill:#fff3e0,stroke:#ef6c00
```

## Key Features

| Feature | Description |
|---------|-------------|
| **GA4 → BigQuery** | Scheduled export, event param flattening, user pseudo-ID stitching |
| **GCP-native ELT** | Partitioned tables, cost-aware clustering, IAM service accounts |
| **Multi-touch attribution** | Channel credit across AU campaign portfolios |
| **Client reporting** | XPON-branded KPI packs (CAC, ROAS, conversion funnels) |

## Project Structure

```
├── data/raw/              # Sample GA4 & ads extracts
├── src/etl/               # Extractors & transforms
├── src/analytics/         # Attribution & segmentation
├── src/ml/                # Churn / LTV models
├── src/dashboard/         # Streamlit app
├── dags/                  # Airflow DAGs
└── tests/
```

## Quick Start

```bash
git clone https://github.com/willtran112358/xpon-multi-channel-mkt-analytics.git
cd xpon-multi-channel-mkt-analytics
python -m venv .venv && source .venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pytest tests/ -q
streamlit run src/dashboard/app.py
```

## Configuration

Set GCP project and GA4 property in `.env` (see `.env.example`):

- `GCP_PROJECT_ID`
- `GA4_PROPERTY_ID`
- `BIGQUERY_DATASET`

---

**Portfolio demo** — synthetic/sample data only; no XPON or client PII.

**Will Tran** — [@willtran112358](https://github.com/willtran112358)
