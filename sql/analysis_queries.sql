-- 1) Total de estados por região
SELECT
    region_name,
    COUNT(*) AS total_states
FROM ibge_states
GROUP BY region_name
ORDER BY total_states DESC, region_name;

-- 2) Estados ordenados pelo tamanho do nome
SELECT
    state_name,
    state_abbr,
    name_length
FROM ibge_states
ORDER BY name_length DESC, state_name;

-- 3) Estados da região Sudeste
SELECT
    state_name,
    state_abbr
FROM ibge_states
WHERE region_name = 'Sudeste'
ORDER BY state_name;

-- 4) Quantidade total carregada e última data de ingestão
SELECT
    COUNT(*) AS total_rows,
    MAX(ingestion_date) AS last_ingestion_date
FROM ibge_states;
