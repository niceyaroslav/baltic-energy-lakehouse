# Baltic Energy Lakehouse

A production-inspired Data Engineering project demonstrating the design and implementation of a modern Lakehouse architecture using Apache Spark, Apache Iceberg, and AWS services.

The goal of this project is to build a realistic end-to-end data platform while gaining hands-on experience with modern Data Engineering technologies and best practices.

---

# Project Goals

This project is designed to simulate a real-world Data Engineering environment.

The primary objectives are:

* Build an end-to-end data pipeline
* Learn Apache Spark beyond the DataFrame API
* Understand Apache Iceberg internals
* Implement Bronze / Silver / Gold architecture
* Build incremental ETL pipelines
* Practice distributed data processing
* Explore AWS-based Lakehouse architecture
* Develop production-quality project structure and documentation

---

# Architecture

```text
                Public APIs
         (Weather & Electricity Prices)
                     │
                     ▼
             Data Ingestion Layer
                     │
                     ▼
        Bronze Layer (Raw JSON Files)
                     │
                     ▼
             Apache Spark Jobs
                     │
                     ▼
      Silver Layer (Iceberg Tables)
                     │
                     ▼
      Business Transformations
                     │
                     ▼
       Gold Analytics Tables
                     │
                     ▼
      Athena / SQL / Dashboard
```

---

# Data Sources

Current public APIs:

* Open-Meteo Weather API
* Baltic Electricity Prices API

Additional public datasets may be added during development.

---

# Technology Stack

## Core

* Python 3.12+
* uv
* Apache Spark
* Apache Iceberg
* PyArrow
* Pandas
* Pydantic

## AWS

* Amazon S3
* AWS Glue Catalog
* Amazon EMR
* Amazon Athena

## Planned

* Apache Airflow
* Streamlit
* Terraform
* Docker

---

# Repository Structure

```text
.
├── src/
│   └── energy_lakehouse/
│       ├── common/
│       ├── ingestion/
│       │   ├── clients/
│       │   └── writers/
│       ├── spark/
│       └── config.py
│
├── tests/
│
├── docs/
│
├── data/
│   ├── bronze/
│   └── warehouse/
│
├── pyproject.toml
└── README.md
```

---

# Project Roadmap

## Phase 1 — Local Data Lake

* [ ] Project setup
* [ ] API clients
* [ ] Local Bronze storage
* [ ] Configuration management

---

## Phase 2 — Apache Spark

* [ ] Read Bronze data
* [ ] Data validation
* [ ] Data cleaning
* [ ] Silver Iceberg tables

---

## Phase 3 — Business Layer

* [ ] Gold tables
* [ ] Analytical SQL
* [ ] Incremental processing

---

## Phase 4 — AWS Migration

* [ ] S3 storage
* [ ] Glue Catalog
* [ ] EMR Spark cluster
* [ ] Athena integration

---

## Phase 5 — Production Features

* [ ] Airflow orchestration
* [ ] Dashboard
* [ ] Monitoring
* [ ] Documentation
* [ ] CI/CD

---

# Learning Objectives

This repository focuses on practical understanding of:

* Distributed Computing
* Spark Execution Model
* Data Partitioning
* Shuffle Operations
* Query Optimization
* Apache Iceberg
* Lakehouse Architecture
* Incremental ETL
* AWS Data Engineering
* Data Pipeline Design

---

# Current Status

🚧 Work in Progress

The project is developed incrementally while documenting architectural decisions, implementation details, and lessons learned.

---

# License

This project is licensed under the MIT License.
