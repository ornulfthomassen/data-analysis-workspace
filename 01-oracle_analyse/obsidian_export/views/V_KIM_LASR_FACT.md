# V_KIM_LASR_FACT

**Schema:** `CCM` | **Type:** `View`

## Description
Exposes data from the `clm_kim.kim_lasr_fact` table, which contains various Key Performance Indicators (KPIs) and related attributes concerning sales, churn, campaigns, and customer interactions. The view serves as a direct projection, renaming some aggregated columns from the source for clearer presentation.

## Data Sources (Inputs)
- ← [[clm_kim.kim_lasr_fact]]
| Column Name |
|---|
| _KPI_ACCEPTED_Sum_ |
| _KPI_ANTICHURN_Sum_ |
| _KPI_CHURN_Sum_ |
| _KPI_NEWSALE_MPP_Sum_ |
| _KPI_PRESENTED_Sum_ |
| _KPI_SALES_Sum_ |
| _KPI_SELECTED_Sum_ |
| _KPI_SUCCESS_Sum_ |
| _VOLUME_Sum_ |
| _KPI_ALL_SALES_Sum_ |
| _KPI_SWAP_Sum_ |
| _CONTACT_DTTM_Max_ |
| campaign_key |
| contact_date_key |
| response_date_key |
| response_date |
| channel_key |
| communication_key |
| treatment_key |
| churn_group_key |
| source_system_key |
| order_from_product_key |
| order_to_product_key |
| response_key |
| sales_matrix |
| sales_matrix_group |
| program |
| campaign |
| activity_objective |
| activity_id |
| activity_name |
| campaign_desc |
| trigger_id |
| dialogue_id |
| order_dealer_key |
| effect_status |
| effect_type |
| kpi_effect_30d |
| treat_swap_terminal |
| activity_main_objective |
| activity_desc |
| swap_match |
| campaign_system |
| contact_product_key |
| dialog_id |
| rolle |
| treatment_product_key |
| contact_handset_key |
| comm_shape_descr |
| res_app_name |
| reservation_days |
| effect_rank |
| newsale_days |
| bank_id_days |
| nr_od_churn_days |
| nr_osd_churn_days |
| camp_call_days |
| newsale_call_days |
| camp_call5_churn70 |
| ns_call5_churn70 |
| kpi_reservation_30d |
| kpi_reservation_7d |
| kpi_ns_od_churn_70d |
| kpi_ns_od_churn_15d |
| ns_od_churn_cat |
| kpi_ns_osd_churn_70d |
| kpi_ns_osd_churn_15d |
| ns_osd_churn_cat |
| nr_churn_serv_prov_nm |
| nr_churn_serv_prov_gr |
| nr_churn_category_name |
| from_service_provider_group |
| dlr_drm_sales_channel_gen04 |
| kpi_ns_call_5d |
| ns_call_days_cat |
| camp_call_days_cat |
| kpi_camp_call_5d |
| owner_age_group |
| user_age_group |
| owner_age |
| user_age |
| main_number_sk |
| subscription_key |
| customer_sk_owner |
| customer_sk_user |
| customer_sk_payer |
| order_match_key |
| order_rank_group_key |
| order_rank |
| contact_key |
| ns_order_category_name |
| old_ns_match |
| order_days |
| product_act1 |
| event_sub_sk |

