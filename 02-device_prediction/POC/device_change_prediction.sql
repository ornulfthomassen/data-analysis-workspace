
# *********************************************************************
# BUILD scoring FOR DEVICE change PREDICTION
# Output table: `tnn-consumer-common-nx.DataScience.device_change_prediction`
# *********************************************************************

#Find all device first use for each EXISTING subscription wher we have device usage info
CREATE OR REPLACE TABLE
  `tnn-consumer-common-nx.DataScience.subscription_hist_tmp_p` AS
  WITH 
  HIST_1 AS(
SELECT 
m.main_number_sk,
max(s.customer_sk_user) as customer_sk_user,
S.period_month_date,
upper(s.device_marketing_name) as device_marketing_name,
upper(s.device_producername) as device_producername,
b.device_release_date,
upper(s.device_category) as device_category,
case when s.device_type IN ('PDA','CLAMSHELL','SMARTPHONE','BLOCK','SLIDER','RUGGED') then 'Mobile phone' else 'Other device' end as device_group,
s.net_other_fee,
no_days_mno_start,
s.no_days_prod_start,
s.net_discount_amount_use,
s.net_amount_use_cpa_3mo,
s.kr_mb_last3,
s.net_revenue,
s.net_amount_use_roam_3mo,
s.net_per_fee_bind_3mo,
s.no_mms_dom_last1,
s.kr_mb_last1,
s.net_use,
s.mb_last3,
s.net_disc_amt_use_roam_3mo,
s.mb_last1,
s.kr_mb_last2,
s.net_fee,
s.no_days_subs_start,
s.mb_last2,
s.net_revenue_adj_3mo
FROM `tnn-consumer-common-nx.ADM.subscription_hist` s
LEFT JOIN `tnn-consumer-common-nx-gold.Dimensions.subscription_master_history` m 
 ON CAST(s.subscription_id AS NUMERIC) = m.subscription_id
 left join (
  select upper(r.device_marketing_name) as device_marketing_name,
        upper(r.device_producername) as device_producername,
        min(r.period_month_date) as device_release_date
FROM `tnn-consumer-common-nx.ADM.subscription_hist` r
 where r.period_month_date is not null
 and r.device_type IN ('PDA','CLAMSHELL','SMARTPHONE','BLOCK','SLIDER','RUGGED')
 group by all
 ) b on b.device_marketing_name = upper(s.device_marketing_name)
 and b.device_producername = upper(s.device_producername)
 where s.period_month_date is not null
 and s.device_type IN ('PDA','CLAMSHELL','SMARTPHONE','BLOCK','SLIDER','RUGGED')
group by all),
active_subs as (
  select main_number_sk 
  FROM `tnn-consumer-common-nx.ADM.subscription_hist` s
  LEFT JOIN `tnn-consumer-common-nx-gold.Dimensions.subscription_master_history` m 
  ON CAST(s.subscription_id AS NUMERIC) = m.subscription_id
  where period_month_date = DATE_SUB(DATE_ADD(DATE_TRUNC(CURRENT_DATE(), MONTH), INTERVAL 0 MONTH), INTERVAL 1 DAY)
   and s.device_type IN ('PDA','CLAMSHELL','SMARTPHONE','BLOCK','SLIDER','RUGGED')
)
select a.*, ROW_NUMBER() OVER (PARTITION BY a.customer_sk_user, a.period_month_date ORDER BY a.device_release_date DESC) as rank_by_release_date from HIST_1 a
join active_subs b on a.main_number_sk = b.main_number_sk
;


# current_device_release_days

###################################################################

# build change device history, remove noice and build features
CREATE OR REPLACE TABLE
  `tnn-consumer-common-nx.DataScience.device_change_hist_tmp_p` AS
WITH
#3.1 Rank devices and only keep devices that have first use less than 2 years after release
  RankedDevices AS (
  SELECT
    MIN(a.period_month_date) AS device_first_use_date,
    MAX(period_month_date) AS device_last_use_date,
    a.device_release_date,
    a.main_number_sk,
    a.device_marketing_name,
    a.device_producername,
    a.device_category,
    case when DATE_DIFF(MIN(a.period_month_date), device_release_date, DAY) <= 730 then 0 else 1 end as use_after_2y
  FROM `tnn-consumer-common-nx.DataScience.subscription_hist_tmp_p` a
  GROUP BY ALL ),
  #3.2 Find previous device release date
  LaggedDeviceRelease AS (
  SELECT
    device_first_use_date,
    device_last_use_date,
    device_release_date,
    main_number_sk,
    device_marketing_name,
    device_producername,
    device_category,
    LAG(device_release_date, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS previous_device_release_date
  FROM
    RankedDevices
  where use_after_2y = 0
    #  where device_release_date > pre_max_device_release_date
  ORDER BY
    main_number_sk,
    device_first_use_date ),
    #3.3 Find previous and next device for each device change
  LaggedDevices AS (
  SELECT
    device_first_use_date,
    device_last_use_date,
    previous_device_release_date,
    device_release_date,
    main_number_sk,
    device_marketing_name,
    device_producername,
    device_category,
    ROW_NUMBER() OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS first_device_rank,
    ROW_NUMBER() OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS last_device_rank,
    LAG(device_first_use_date, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS previous_device_first_use_date,
    LAG(device_first_use_date, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS next_device_first_use_date,
    LAG(device_marketing_name, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS next_device,
    LAG(device_marketing_name, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS pre_device,
    LAG(device_producername, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS next_producer,
    LAG(device_producername, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS pre_producer
  FROM
    LaggedDeviceRelease
    #  where DATE_DIFF(device_release_date, previous_device_release_date, DAY) > 1
  ORDER BY
    main_number_sk,
    device_first_use_date ),
    #3.4 Remove replacement devices and those that are used more than 30 days except first and last device
  RemvoveDevices AS (
  SELECT
    device_first_use_date,
    device_last_use_date,
    device_release_date,
    main_number_sk,
    device_marketing_name,
    device_producername,
    device_category,
    next_device,
    pre_device
  FROM
    LaggedDevices
  WHERE
    first_device_rank = 1
    OR last_device_rank = 1
    OR ( UPPER(device_marketing_name) <> UPPER(pre_device)
      AND DATE_DIFF(next_device_first_use_date, device_first_use_date, DAY) > 30 )
  ORDER BY
    main_number_sk,
    device_first_use_date ),
    #3.5 Find the newest device release date pr subscription
  MaxReleaseDate AS (
  SELECT
    a.device_first_use_date,
    a.device_last_use_date,
    a.device_release_date,
    a.main_number_sk,
    a.device_marketing_name,
    a.device_producername,
    a.device_category,
    a.next_device,
    a.pre_device,
    MAX(b.device_release_date) AS max_device_release_date
  FROM
    RemvoveDevices a
  LEFT JOIN
    RemvoveDevices b
  ON
    a.main_number_sk = b.main_number_sk
    AND DATE_DIFF(a.device_first_use_date, b.device_first_use_date, DAY) >= 0
  GROUP BY ALL ),
# After clean of changes, we need to repeat all steps above
#3.6 Find previous release date
  LaggedDeviceRelease2 AS (
  SELECT
    device_first_use_date,
    device_last_use_date,
    device_release_date,
    main_number_sk,
    device_marketing_name,
    device_producername,
    device_category,
    LAG(device_release_date, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS previous_device_release_date
  FROM
    MaxReleaseDate
  WHERE
    device_release_date >= max_device_release_date
  ORDER BY
    main_number_sk,
    device_first_use_date ),
     #3.7 Find previous and next device for each device change
  LaggedDevices2 AS (
  SELECT
    device_first_use_date,
    device_last_use_date,
    previous_device_release_date,
    device_release_date,
    main_number_sk,
    device_marketing_name,
    device_producername,
    device_category,
    ROW_NUMBER() OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS first_device_rank,
    ROW_NUMBER() OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS last_device_rank,
    LAG(device_first_use_date, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS previous_device_first_use_date,
    LAG(device_first_use_date, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS next_device_first_use_date,
    LAG(device_marketing_name, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS next_device,
    LAG(device_marketing_name, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS pre_device,
    LAG(device_producername, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date DESC) AS next_producer,
    LAG(device_producername, 1, NULL) OVER (PARTITION BY main_number_sk ORDER BY device_first_use_date) AS pre_producer
  FROM
    LaggedDeviceRelease2
  ORDER BY
    main_number_sk,
    device_first_use_date ),
  #3.8 Find days since release date and days since previous device.
  DaysDevices AS (
  SELECT
    device_first_use_date,
    device_last_use_date,
    previous_device_release_date,
    device_release_date,
    main_number_sk,
    device_marketing_name,
    device_producername,
    device_category,
    first_device_rank,
    last_device_rank,
    previous_device_first_use_date,
    next_device_first_use_date,
    next_device,
    next_producer,
    pre_device,
    pre_producer,
    CASE
      WHEN first_device_rank > 1 THEN DATE_DIFF(device_first_use_date, previous_device_first_use_date, DAY)
      ELSE NULL
  END
    AS days_since_previous_device,
    CASE
      WHEN last_device_rank > 1 THEN DATE_DIFF(next_device_first_use_date, device_first_use_date, DAY)
      ELSE NULL
  END
    AS days_to_next_device,
    CASE
      WHEN first_device_rank > 1 THEN DATE_DIFF(device_first_use_date, device_release_date, DAY)
      ELSE NULL
  END
    AS days_first_use_after_release
  FROM
    LaggedDevices2 )
SELECT
  *
FROM
  DaysDevices;

###################################################################

# Find the median change days for each subscription
CREATE OR REPLACE TABLE
  `tnn-consumer-common-nx.DataScience.main_stat_tmp` AS
WITH
  DeviceStats AS (
  SELECT
    days_since_previous_device,
    days_first_use_after_release,
    main_number_sk,
    device_marketing_name,
    pre_device,
    device_producername,
    device_category,
    previous_device_first_use_date,
    device_first_use_date,
    device_release_date,
    last_device_rank,
    PERCENTILE_CONT(days_since_previous_device, 0.5) OVER (PARTITION BY main_number_sk) AS med_days_since_previous_device
  FROM
    `tnn-consumer-common-nx.DataScience.device_change_hist_tmp_p`
  WHERE
    device_marketing_name IS NOT NULL 
    )
SELECT
  *
FROM
  DeviceStats;

###################################################################

  # Find the stats change days generic for all subscription
CREATE OR REPLACE TABLE
  `tnn-consumer-common-nx.DataScience.gen_stat_tmp` AS
WITH
  DeviceStats AS (
  SELECT
    days_since_previous_device,
    days_first_use_after_release,
    DATE_TRUNC(device_first_use_date, MONTH) AS first_use_month,
    PERCENTILE_CONT(days_since_previous_device, 0.5) OVER (PARTITION BY DATE_TRUNC(device_first_use_date, MONTH)) AS med_days_since_previous_device
  FROM
    `tnn-consumer-common-nx.DataScience.device_change_hist_tmp_p`
  WHERE
    days_since_previous_device IS NOT NULL )
SELECT
  first_use_month,
  AVG(days_first_use_after_release) AS avg_gen_days_first_use_after_release,
  AVG(days_since_previous_device) AS avg_gen_change_days,
  AVG(med_days_since_previous_device) AS med_gen_change_days,
  STDDEV(days_since_previous_device) AS stddev_gen_change_days
FROM
  DeviceStats
GROUP BY
  1;

###################################################################

  # Find the stats change days for each device model name
CREATE OR REPLACE TABLE
  `tnn-consumer-common-nx.DataScience.device_name_stat_tmp` AS
WITH
  DeviceStats AS (
  SELECT
    DATE_TRUNC(device_first_use_date, MONTH) AS first_use_month,
    device_marketing_name,
    days_first_use_after_release,
    days_to_next_device,
    PERCENTILE_CONT(days_to_next_device, 0.5) OVER (PARTITION BY device_marketing_name) AS med_days_to_next_device_name
  FROM
    `tnn-consumer-common-nx.DataScience.device_change_hist_tmp_p`
  WHERE
    (days_to_next_device IS NOT NULL) )
SELECT
  first_use_month,
  device_marketing_name,
  AVG(days_first_use_after_release) AS avg_dev_days_first_use_after_release,
  AVG(days_to_next_device) AS avg_dev_change_days,
  AVG(days_to_next_device) AS med_dev_change_days,
  STDDEV(days_to_next_device) AS stddev_dev_change_days
FROM
  DeviceStats
GROUP BY
  1,
  2;

###################################################################

#Keep the continuous variable: Keep the current_device_days as it is.
#Add new binary features: Create new columns that explicitly flag these important time periods. For example:
#is_near_12_month_milestone: A binary flag (1 or 0) that is 1 if current_device_days is between, for example, 330 and 420 days (11-14 months).
#is_near_24_month_milestone: A similar flag for the 2-year mark (e.g., between 700 and 790 days).

  # Join adm subscription and all change days statistics from before each period.
CREATE OR REPLACE TABLE `tnn-consumer-common-nx.DataScience.device_change_prediction` AS
WITH
  device_prediction_tmp1 AS (
SELECT 
  s.main_number_sk,
  s.customer_sk_user,
  s.period_month_date,
  s.device_producername,
  s.device_release_date,
  s.device_category,
  s.device_group,
  s.device_marketing_name AS current_device,
  CASE WHEN s.device_producername = 'APPLE' THEN 1 ELSE 0 END AS device_producername_APPLE,
  CASE WHEN s.device_producername = 'SAMSUNG' THEN 1 ELSE 0 END AS device_producername_SAMSUNG,
  CASE WHEN s.device_producername = 'DORO' THEN 1 ELSE 0 END AS device_producername_DORO,
  CASE WHEN s.device_producername = 'HUAWEI' THEN 1 ELSE 0 END AS device_producername_HUAWEI,
  CASE WHEN s.device_producername = 'NOKIA' THEN 1 ELSE 0 END AS device_producername_NOKIA,
  CASE
    WHEN s.device_producername = 'MOTOROLA' THEN 1
    ELSE 0
END
  AS device_producername_MOTOROLA,
  CASE
    WHEN s.device_producername = 'SONY' THEN 1
    ELSE 0
END
  AS device_producername_SONY,
  CASE
    WHEN s.device_producername = 'GOOGLE' THEN 1
    ELSE 0
END
  AS device_producername_GOOGLE,
  CASE
    WHEN s.device_producername = 'ONEPLUS' THEN 1
    ELSE 0
END
  AS device_producername_ONEPLUS,
  CASE
    WHEN s.device_producername = 'XIAOMI' THEN 1
    ELSE 0
END
  AS device_producername_XIAOMI,
  CASE
    WHEN s.device_producername = 'KAMMUNICA POLSKA' THEN 1
    ELSE 0
END
  AS device_producername_KAMMUNICA_POLSKA,
  CASE
    WHEN s.device_producername = 'CATERPILLAR' THEN 1
    ELSE 0
END
  AS device_producername_CATERPILLAR,
  CASE
    WHEN s.device_producername = 'SHANDONG KAER ELECTRIC' THEN 1
    ELSE 0
END
  AS device_producername_SHANDONG_KAER_ELECTRIC,
  CASE
    WHEN s.device_producername = 'TCL COMMUNICATION' THEN 1
    ELSE 0
END
  AS device_producername_TCL_COMMUNICATION,
  CASE
    WHEN s.device_producername = 'ALCATEL' THEN 1
    ELSE 0
END
  AS device_producername_ALCATEL,
  CASE
    WHEN s.device_producername = 'ASUS' THEN 1
    ELSE 0
END
  AS device_producername_ASUS,
  CASE
    WHEN s.device_producername = 'SONYERICSSON' THEN 1
    ELSE 0
END
  AS device_producername_SONYERICSSON,
  CASE
    WHEN s.device_producername = 'JABLOCOM' THEN 1
    ELSE 0
END
  AS device_producername_JABLOCOM,
  CASE
    WHEN s.device_producername = 'LG' THEN 1
    ELSE 0
END
  AS device_producername_LG,
  CASE
    WHEN s.device_producername = 'NOTHING TECHNOLOGY LIMITED' THEN 1
    ELSE 0
END
  AS device_producername_NOTHING_TECHNOLOGY_LIMITED,
CASE WHEN s.device_producername NOT IN ( 'APPLE', 'SAMSUNG', 'DORO', 'HUAWEI', 'NOKIA', 'MOTOROLA', 'SONY', 'GOOGLE', 'ONEPLUS', 'XIAOMI', 'KAMMUNICA POLSKA', 'CATERPILLAR', 'SHANDONG KAER ELECTRIC', 'TCL COMMUNICATION', 'ALCATEL', 'ASUS', 'SONYERICSSON', 'JABLOCOM', 'LG', 'NOTHING TECHNOLOGY LIMITED') THEN 1 ELSE 0 END AS device_producername_OTHER_TOP_20,
  CAST(s.net_other_fee AS FLOAT64) AS net_other_fee,
  CAST(s.no_days_mno_start AS FLOAT64) AS no_days_mno_start,
  CAST(s.no_days_prod_start AS FLOAT64) AS no_days_prod_start,
  CAST(s.net_discount_amount_use AS FLOAT64) AS net_discount_amount_use,
  CAST(s.net_amount_use_cpa_3mo AS FLOAT64) AS net_amount_use_cpa_3mo,
  CAST(s.kr_mb_last3 AS FLOAT64) AS kr_mb_last3,
  CAST(s.net_revenue AS FLOAT64) AS net_revenue,
  CAST(s.net_amount_use_roam_3mo AS FLOAT64) AS net_amount_use_roam_3mo,
  CAST(s.net_per_fee_bind_3mo AS FLOAT64) AS net_per_fee_bind_3mo,
  CAST(s.no_mms_dom_last1 AS FLOAT64) AS no_mms_dom_last1,
  CAST(s.kr_mb_last1 AS FLOAT64) AS kr_mb_last1,
  CAST(s.net_use AS FLOAT64) AS net_use,
  CAST(s.mb_last3 AS FLOAT64) AS mb_last3,
  CAST(s.net_disc_amt_use_roam_3mo AS FLOAT64) AS net_disc_amt_use_roam_3mo,
  CAST(s.mb_last1 AS FLOAT64) AS mb_last1,
  CAST(s.kr_mb_last2 AS FLOAT64) AS kr_mb_last2,
  CAST(s.net_fee AS FLOAT64) AS net_fee,
  CAST(s.no_days_subs_start AS FLOAT64) AS no_days_subs_start,
  CAST(s.mb_last2 AS FLOAT64) AS mb_last2,
  CAST(s.net_revenue_adj_3mo AS FLOAT64) AS net_revenue_adj_3mo,
    EXTRACT(MONTH FROM s.period_month_date) AS current_month_nr,
  EXTRACT(MONTH FROM s.device_release_date) AS current_release_month_nr,
  DATE_DIFF( CASE WHEN s.period_month_date > DATE( EXTRACT(YEAR FROM s.period_month_date), 12, 25) THEN DATE(EXTRACT(YEAR FROM s.period_month_date) + 1, 12, 25) 
  ELSE DATE(EXTRACT(YEAR FROM s.period_month_date), 12, 25) END , s.period_month_date, DAY) AS days_until_christmas,
  DATE_DIFF(CASE WHEN s.period_month_date > DATE( EXTRACT(YEAR FROM s.period_month_date), 6, 30) THEN DATE(EXTRACT(YEAR FROM s.period_month_date) + 1, 6, 30) 
  ELSE DATE(EXTRACT(YEAR FROM s.period_month_date), 6, 30) END, s.period_month_date, DAY) AS days_until_summer,
  f.device_name,
  f.manufacturer,
  f.device_series_annual,
  f.display_type,
  f.context_summary,
  f.generation,
  f.device_series_annual_no,
  SAFE_CAST(f.release_year AS int) AS release_year,
  SAFE_CAST(f.ram_gb AS float64) AS ram_gb,
  SAFE_CAST(f.storage_base_gb AS float64) AS storage_base_gb,
  SAFE_CAST(f.display_size_inches AS float64) AS display_size_inches,
  SAFE_CAST(f.camera_rear_mp AS float64) AS camera_rear_mp,
  SAFE_CAST(f.camera_front_mp AS float64) AS camera_front_mp,
  SAFE_CAST(f.launch_price_nok AS float64) AS launch_price_nok,
  DATE_DIFF( DATE_TRUNC(s.period_month_date, MONTH), DATE_TRUNC(s.device_release_date, MONTH), DAY) AS current_device_release_days,
  # AGG: 
  MIN(dc.device_first_use_date) AS current_device_first_use_date,
  MAX(DATE_DIFF( DATE_TRUNC(s.period_month_date, MONTH), DATE_TRUNC(dc.device_first_use_date, MONTH), DAY)) AS current_device_days,
  AVG(SAFE_DIVIDE( DATE_DIFF( DATE_TRUNC(s.period_month_date, MONTH), DATE_TRUNC(dc.device_first_use_date, MONTH), DAY), COALESCE(dc.days_since_previous_device, dname.avg_dev_change_days))) AS current_days_vs_avg_change_days,
  MIN(DATE_DIFF(dc.device_first_use_date, s.device_release_date, DAY)) AS days_first_use_after_release,
  AVG(dc.days_since_previous_device) AS avg_change_days,
  AVG(dc.med_days_since_previous_device) AS med_change_days,
  AVG(dgen.avg_gen_days_first_use_after_release) AS avg_gen_days_first_use_after_release,
  AVG(dgen.avg_gen_change_days) AS avg_gen_change_days,
  AVG(dgen.med_gen_change_days) AS med_gen_change_days,
  AVG(dgen.stddev_gen_change_days) AS stddev_gen_change_days,
  AVG(dname.avg_dev_days_first_use_after_release) AS avg_dev_days_first_use_after_release,
  AVG(dname.avg_dev_change_days) AS avg_dev_change_days,
  AVG(dname.med_dev_change_days) AS med_dev_change_days,
  AVG(dname.stddev_dev_change_days) AS stddev_dev_change_days,
  MIN(EXTRACT(MONTH FROM dc.device_first_use_date)) AS current_purchase_month_nr
FROM
  `tnn-consumer-common-nx.DataScience.subscription_hist_tmp_p` AS s
LEFT JOIN
  `tnn-consumer-common-nx`.`DataScience`.`main_stat_tmp` AS dc
ON
  s.main_number_sk = dc.main_number_sk
  AND DATE_TRUNC(s.period_month_date, MONTH) >= DATE_TRUNC(dc.device_first_use_date, MONTH)
  AND s.device_marketing_name = dc.device_marketing_name
LEFT JOIN
  `tnn-consumer-common-nx`.`DataScience`.`gen_stat_tmp` AS dgen
ON
  dgen.first_use_month BETWEEN DATE_SUB(DATE_TRUNC(s.period_month_date, MONTH), INTERVAL 13 MONTH)
  AND DATE_SUB(DATE_TRUNC(s.period_month_date, MONTH), INTERVAL 1 MONTH)
LEFT JOIN
  `tnn-consumer-common-nx`.`DataScience`.`device_name_stat_tmp` AS dname
ON
  UPPER(s.device_marketing_name) = UPPER(dname.device_marketing_name)
  AND DATE_TRUNC(s.period_month_date, MONTH) >= DATE_TRUNC(dname.first_use_month, MONTH)
JOIN
  `tnn-consumer-common-nx`.`DataScience`.`device_features` AS f
ON
  UPPER(s.device_producername || ' ' || s.device_marketing_name) = UPPER(f.user_input)
WHERE period_month_date = DATE_SUB(DATE_ADD(DATE_TRUNC(CURRENT_DATE(), MONTH), INTERVAL 0 MONTH), INTERVAL 1 DAY)
  GROUP BY ALL
    )
SELECT * FROM device_prediction_tmp1;

drop table `tnn-consumer-common-nx.DataScience.main_stat_tmp`;
drop table `tnn-consumer-common-nx.DataScience.gen_stat_tmp`;
drop table `tnn-consumer-common-nx.DataScience.device_name_stat_tmp`;








