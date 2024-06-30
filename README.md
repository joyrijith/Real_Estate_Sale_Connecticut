
# Real Estate Sale

## Table of Contents
- [Project Synopsis](#project-synopsis)
- [Dataset](#dataset)
- [Tools Used](#tools-used)
- [Project Flow](#project-flow)
- [Prerequisites](#prerequisites)
- [Running the Project](#running-the-project)
- [Visualization and Key Insights](#visualization-and-key-insights)
- [Contributions](#contributions)

## Project Synopsis
This is a capstone project for [DataTalks DE Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/README.md). <br>
In this project an end to end pipeline was built using Mage, DBT,GCP , Terraform and Google Looker studio to clean, build model and analyse the Real Estate Sale for the state of Connecticut (USA) between 2008 and 2021
## Dataset
The Dataset used for this project is obtained from [here](https://data.ct.gov/Housing-and-Development/Real-Estate-Sales-2001-2021-GL/5mzw-sjtu/about_data). <br>
The original dataset is the Real Estate Sale transactions between 2001 and 2021. The data analysed and used for the project was between 2008 to 2021. <br>
Approximately 635K rows of data was analyzed for this project
## Tools Used
- [Mage](https://www.mage.ai/) - **Mage** is used as the orchestration tool for this project. <br>
  Using Python/SQL data is transferred from the data source (API) to GCS (Google Cloud Storage). From GCS using Mage the data is being cleaned and uploaded in Big Query which is further modelled further

-  [GCP](https://cloud.google.com/storage?hl=en) - **GCP** is the cloud platform utilised for this project. GCS and BQ in GCP are utislied . **GCS** is used for storing the raw data parquet file as a whole and partitioned based on month. **BQ** from GCP is used as the **Data Warehouse**.
  
-  [dbt](https://auth.cloud.getdbt.com/) - **DBT** is used for modelling the data present in BQ to create meaningful insights and analysis of the Real Estate Sale Data for the state of Connecticut
  
-  [Google Looker Studio](https://lookerstudio.google.com/overview) - Google Looker Studio is used for building the visualization of the anlaysis done of the data and build useful and meaningful dashboards

-  [Terraform](https://www.terraform.io/) - Used Terraform to build and tear down the GCP resources.
## Project Flow
![Flow drawio](https://github.com/joyrijith/Real_Estate_Sale_Connecticut/assets/89081604/31290b99-d5dd-4754-bbc0-f14bb06b4643)

1.Get the source data as CSV file <br>
2.Using Mage, extracting data from the CSV file and storing the data in Google Cloud Storage **(Data Lake)** as parquet file <br>
3.Using Mage, extracting data from GCS cleaning the data and loading data into Big Query **(DWH)** <br>
4.Using DBT, extracting data from BQ to create different models for analysis <br>
5.Using Google Looker, creating visualizations and dashboards <br>

## Prerequisites
## Running the Project
## Visualization and Key Insights
## Contributions
