# Digital Marketing Analytics Platform

Customer acquisition, engagement, and retention analytics platform with real-time dashboarding and ML-powered attribution modeling.

## Overview

End-to-end marketing intelligence platform processing multi-channel campaign data (email, social, web, paid ads) with:
- Real-time ETL pipeline aggregating marketing events
- Customer journey attribution modeling
- Predictive churn/LTV scoring  
- Campaign performance dashboards
- A/B testing framework with statistical significance tests

## Tech Stack

- **Data Pipeline**: Python 3.10+ (Pandas, PySpark)
- **Database**: PostgreSQL + TimescaleDB (time-series)
- **Analytics**: dbt (data models + tests)
- **ML/Analytics**: Scikit-learn, XGBoost
- **Dashboard**: Streamlit + Plotly
- **Orchestration**: Airflow DAGs
- **Infrastructure**: Docker, Kubernetes
- **CI/CD**: GitHub Actions

## Architecture

```
Campaign Events (Email/Social/Web/Paid)
         ↓
    [Bronze Layer]  Raw event ingestion + schema validation
         ↓
    [Silver Layer]  Event enrichment + customer deduplication
         ↓
    [Gold Layer]    Attribution + customer metrics + campaign KPIs
         ↓
    [dbt Models]    Reporting tables + data marts
         ↓
    [Dashboards]    Real-time KPI monitoring + performance analysis
    [ML Models]     Churn prediction + LTV scoring
```

## Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Channel Attribution** | Credit allocation across touchpoints (first-click, last-click, ML-based) |
| **Customer Segmentation** | RFM, behavioral, predictive clustering |
| **Campaign Analytics** | Performance by channel/segment with A/B testing |
| **Churn Prediction** | Early warning system with 30/60/90-day predictions |
| **LTV Forecasting** | Customer lifetime value estimation with confidence intervals |
| **Real-time Dashboard** | Live KPI monitoring (CAC, ROI, conversion rates) |

## Project Structure

```
digital_marketing/
├── data/
│   ├── raw/                 # Raw campaign event exports
│   └── processed/           # Cleaned datasets
├── src/
│   ├── etl/
│   │   ├── extractors.py   # Campaign platform connectors
│   │   ├── transformers.py # Event enrichment logic
│   │   └── loaders.py      # Database write operations
│   ├── attribution/
│   │   ├── models.py       # Attribution algorithms
│   │   └── utils.py        # Attribution helpers
│   ├── ml/
│   │   ├── churn_model.py  # Churn prediction
│   │   └── ltv_model.py    # LTV forecasting
│   ├── analytics/
│   │   └── metrics.py      # KPI calculations
│   └── dashboards/
│       ├── app.py          # Streamlit app entry
│       └── pages/          # Multi-page dashboard
├── dbt/
│   ├── models/
│   │   ├── staging/        # Base models
│   │   ├── intermediate/   # Transformed data
│   │   └── marts/          # Reporting tables
│   └── tests/
├── airflow/
│   └── dags/
│       ├── campaign_etl_dag.py
│       └── ml_scoring_dag.py
├── tests/
│   ├── unit/
│   └── integration/
├── config/
│   └── settings.py
├── requirements.txt
├── .env.example
├── docker-compose.yml
└── .github/
    └── workflows/
        ├── ci.yml
        └── cd.yml
```

## Setup

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Docker & Docker Compose
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/willtran112358/digital-marketing-analytics.git
cd digital_marketing

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your database credentials

# Initialize database
python src/etl/setup_db.py

# Run dbt models
cd dbt
dbt run
dbt test
cd ..
```

### Running the Platform

```bash
# Start services with Docker
docker-compose up -d

# Run ETL pipeline
python -m src.etl.main

# Launch dashboard
streamlit run src/dashboards/app.py

# Trigger Airflow DAG
airflow dags trigger campaign_etl_dag
```

## Configuration

Environment variables in `.env`:

```
DATABASE_URL=postgresql://user:password@localhost:5432/marketing_db
AIRFLOW_HOME=/path/to/airflow
ENVIRONMENT=development
LOG_LEVEL=INFO
```

## Data Model

### Key Tables

- `events` — Raw marketing events (clicks, views, conversions)
- `customers` — Enriched customer profiles  
- `campaigns` — Campaign metadata + performance metrics
- `attribution` — Attribution credit allocation per customer
- `predictions` — Churn/LTV model scores

## Testing

```bash
# Unit tests
pytest tests/unit -v

# Integration tests
pytest tests/integration -v

# dbt tests
dbt test
```

## Performance

- Pipeline latency: ~5 minutes (end-to-end)
- Dashboard refresh: Real-time (Streamlit + PostgreSQL)
- ML model retraining: Daily (Airflow scheduler)

## Contributing

1. Create a branch (`git checkout -b feature/your-feature`)
2. Commit changes (`git commit -m 'Add feature'`)
3. Push branch (`git push origin feature/your-feature`)
4. Open Pull Request

## License

MIT License — See LICENSE file

## Contact

**Author**: WillTran  
**GitHub**: [@willtran112358](https://github.com/willtran112358)
