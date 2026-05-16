# Looker Studio (Google Data Studio) — XPON BI Layer

XPON delivers client-facing marketing analytics through **Looker Studio**, not custom web apps. BigQuery marts are the single source of truth; Looker connects via the native **BigQuery connector** with service-account or user OAuth (client workspace).

## Report packs (typical XPON delivery)

| Page | Data source (BigQuery view) | Metrics |
|------|----------------------------|---------|
| Executive summary | `mart_campaign_performance` | Spend, conversions, ROAS, CAC |
| Channel mix | `mart_channel_attribution` | First/last/linear credit by channel |
| Campaign drill-down | `mart_campaign_performance` | Filters: campaign, date, geo (AU) |
| Cohort & LTV | `mart_customer_ltv` | Predicted LTV, churn risk band |

## Connection steps

1. GCP: grant Looker Studio service account `roles/bigquery.dataViewer` on dataset `xpon_marketing`.
2. Looker Studio → **Create** → **Report** → **BigQuery** → project + dataset.
3. Add charts from views in `bigquery_marts.sql` (deploy views first).
4. Optional: copy XPON org template and re-point data sources per client GA4 property.

## Design notes

- Use **date range** control on `event_date` (partition key).
- Blended data: GA4 export tables + ads cost tables joined in BigQuery views (not in Looker).
- ML outputs (`churn_score`, `ltv_band`) exposed as dimensions in `mart_customer_ltv` for scorecard tiles.

## Related GCP products

- **GA4 BigQuery Export** → bronze events  
- **dbt** → gold marts (this repo’s Python modules prototype the transforms)  
- **Looker Studio** → BI only (no Streamlit / custom Flask UI in XPON’s standard stack)
