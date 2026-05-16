-- BigQuery reporting views for Looker Studio (XPON multi-channel analytics)
-- Dataset: xpon_marketing (adjust project/dataset in Looker connection)

CREATE OR REPLACE VIEW `xpon_marketing.mart_campaign_performance` AS
SELECT
  event_date,
  campaign_id,
  campaign_name,
  channel,
  SUM(impressions) AS impressions,
  SUM(clicks) AS clicks,
  SUM(conversions) AS conversions,
  SUM(spend_aud) AS spend_aud,
  SAFE_DIVIDE(SUM(conversions), SUM(clicks)) AS conversion_rate,
  SAFE_DIVIDE(SUM(spend_aud), SUM(conversions)) AS cac_aud,
  SAFE_DIVIDE(SUM(revenue_aud), SUM(spend_aud)) AS roas
FROM `xpon_marketing.gold_campaign_daily`
GROUP BY 1, 2, 3, 4;

CREATE OR REPLACE VIEW `xpon_marketing.mart_channel_attribution` AS
SELECT
  event_date,
  channel,
  attribution_model,
  SUM(attributed_conversions) AS attributed_conversions,
  SUM(attributed_revenue_aud) AS attributed_revenue_aud
FROM `xpon_marketing.gold_attribution`
GROUP BY 1, 2, 3;

CREATE OR REPLACE VIEW `xpon_marketing.mart_customer_ltv` AS
SELECT
  customer_id,
  first_touch_channel,
  churn_score,
  predicted_ltv_aud,
  ltv_band,
  scored_at
FROM `xpon_marketing.gold_customer_scores`;
