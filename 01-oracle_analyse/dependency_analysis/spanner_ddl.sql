-- ============================================================
-- Spanner Graph DDL for Oracle Dependency Analysis
-- Database: s07601-p-tnn-consumer
-- Instance: nova-eu-west1-01
-- Project:  tnn-nova-spanner
-- ============================================================

-- Kjør disse i Spanner Studio, i riktig rekkefølge.

-- 1. Node-tabell: Oracle-objekter (views og prosedyrer)
CREATE TABLE OracleObjects (
  object_name   STRING(500) NOT NULL,
  object_type   STRING(20),
  schema_name   STRING(100),
  functionality STRING(MAX),
) PRIMARY KEY (object_name);

-- 2. Edge-tabell: Avhengigheter mellom objekter
--    "object_name (source) skriver til linked_table, target_object leser fra linked_table"
--    object_name må hete det samme som PK i OracleObjects pga. INTERLEAVE
CREATE TABLE Dependencies (
  object_name   STRING(500) NOT NULL,
  target_object STRING(500) NOT NULL,
  linked_table  STRING(500) NOT NULL,
  source_type   STRING(20),
  target_type   STRING(20),
  FOREIGN KEY (target_object) REFERENCES OracleObjects(object_name),
) PRIMARY KEY (object_name, target_object, linked_table),
  INTERLEAVE IN PARENT OracleObjects ON DELETE CASCADE;

-- 3. Property Graph
CREATE PROPERTY GRAPH OracleDependencyGraph
  NODE TABLES (
    OracleObjects
      KEY (object_name)
      LABEL OracleObject
        PROPERTIES (object_name, object_type, schema_name, functionality)
  )
  EDGE TABLES (
    Dependencies
      KEY (object_name, target_object, linked_table)
      SOURCE KEY (object_name) REFERENCES OracleObjects (object_name)
      DESTINATION KEY (target_object) REFERENCES OracleObjects (object_name)
      LABEL DependsOn
        PROPERTIES (linked_table, source_type, target_type)
  );

-- ============================================================
-- Eksempel-spørringer (GQL) — kjør i Spanner Studio
-- ============================================================

-- Alle avhengigheter for én prosedyre
-- GRAPH OracleDependencyGraph
-- MATCH (src:OracleObject {object_name: 'CLM_ADM.P_RDM_CUSTOMER_MAPPING'})-[d:DependsOn]->(dst:OracleObject)
-- RETURN src.object_name AS src_object, d.linked_table AS via_table,
--        dst.object_name AS dst_object, dst.object_type AS dst_type;

-- Grafvisualisering: returner elementer med TO_JSON()
-- GRAPH OracleDependencyGraph
-- MATCH (src:OracleObject {object_name: 'CLM_ADM.P_ADM_MONTH_DIM'})-[d:DependsOn]->(dst:OracleObject)
-- RETURN TO_JSON(src) AS source, TO_JSON(d) AS edge, TO_JSON(dst) AS target;

-- Kryss-skjema-avhengigheter
-- GRAPH OracleDependencyGraph
-- MATCH (src:OracleObject)-[d:DependsOn]->(dst:OracleObject)
-- WHERE src.schema_name != dst.schema_name
-- RETURN src.schema_name AS src_schema, src.object_name AS src_object,
--        dst.schema_name AS dst_schema, dst.object_name AS dst_object,
--        d.linked_table AS via_table;
