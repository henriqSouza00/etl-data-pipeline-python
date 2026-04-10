# ETL Data Pipeline with Python

## 📊 Dashboard Power BI

O projeto inclui um dashboard desenvolvido no Power BI para visualização dos dados tratados na pipeline ETL.

### Principais análises:
- Distribuição de estados por região
- Total de estados
- Comparação entre regiões

Arquivo disponível em:
`/dashboard/dashboard_estados.pbix`

Projeto de portfólio focado em **Data Engineering**, com pipeline ETL completo:

- **Extract**: consome dados da API pública do IBGE
- **Transform**: trata, padroniza e enriquece os dados com `pandas`
- **Load**: carrega os dados em **SQLite** por padrão ou **MySQL** via variável de ambiente
- **Analyze**: inclui consultas SQL prontas para exploração

## Objetivo

Demonstrar uma pipeline simples, organizada e pronta para portfólio, usando boas práticas de:

- estrutura em camadas
- configuração por `.env`
- logging
- separação de responsabilidades
- persistência em banco

## Fonte de dados

API pública do IBGE:

`https://servicodados.ibge.gov.br/api/v1/localidades/estados`

## Estrutura

```text
etl-data-pipeline-python/
├──dashboard/
     ├── dashboard_estados.pdf
     ├── dashboard_estados.pbix
├── data/
├── sql/
│   └── analysis_queries.sql
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── .env.example
├── requirements.txt
└── README.md
```

## Como rodar

### 1) Criar e ativar ambiente virtual

**Windows**

```bash
py -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Instalar dependências

```bash
pip install -r requirements.txt
```

### 3) Configurar ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
copy .env.example .env
```

ou

```bash
cp .env.example .env
```

### 4) Executar

```bash
python -m src.main
```

## Banco de dados

Por padrão, o projeto usa **SQLite**, gerando o arquivo:

`data/ibge_states.db`

Se quiser usar **MySQL**, altere no `.env`:

```env
DB_TYPE=mysql
MYSQL_USER=seu_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=portfolio_data
```

## O que a pipeline faz

1. Extrai a lista de estados do Brasil
2. Normaliza os campos
3. Cria colunas derivadas
4. Carrega os dados na tabela `ibge_states`
5. Salva também um CSV em `data/ibge_states.csv`

## Campos finais

- `state_id`
- `state_name`
- `state_abbr`
- `region_id`
- `region_name`
- `capitalized_state_name`
- `name_length`
- `ingestion_date`
- `source`

## Consultas SQL

Veja o arquivo:

`sql/analysis_queries.sql`

## Ideias para evolução

- adicionar testes unitários
- orquestrar com Airflow
- rodar em Docker
- criar dashboard no Power BI
- expandir para municípios e mesorregiões

## Autor

**Henrique Souza**  
Data Analyst | Data Engineering (SQL, ETL, Data Quality)
