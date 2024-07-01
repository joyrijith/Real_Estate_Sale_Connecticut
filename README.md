
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
![Flow drawio](https://github.com/joyrijith/Real_Estate_Sale_Connecticut/assets/89081604/23d6fda6-186a-4c82-ac3a-7d1d9e88c3db)


1. Get the source data as CSV file <br>
2. Using Mage, extracting data from the CSV file and storing the data in Google Cloud Storage **(Data Lake)** as parquet file <br>
3. Using Mage, extracting data from GCS cleaning the data and loading data into Big Query **(DWH)** <br>
4. Using DBT, extracting data from BQ to create different models for analysis <br>
5. Using Google Looker, creating visualizations and dashboards <br>

## Prerequisites
- **GCP**
 To run this end to end pipline, the user would need access to GCP. <br>
 In GCP, create service account for this project and have the following access **BigQuery Admin**, **Storage Admin**, and **Compute Admin** <br>
 Create the json key in the service account and save the private key generated <br>
 Save the private key file in the root folder of mage to be able to access GCP using mage
- **dbt** Create user access in dbt for developing models
- **docker** To compose and build mage 
- **Google Looker Studio**  Create user access for building visualizations.
## Running the Project
- **Clone the Repository** : Clone the repository in your local machine
- **Download Terraform** : Donwload Terraform and set path of the Terraform file in your environment variable , and install Terraform plugin from Hashicorp in your VS code
- **Setting Terraform** : We use GCP as the cloud platform for our project. Navigate to Terraform folder -> set the region to your region and update the  project name to your GCP project id
- **Initializing Terraform** :  Run terraform init which will set your working directory having congiguration files.
- **Terraform Plan** : Execute terraform plan which shows the changes that are done in the config which will take affect when Terraform Apply in executed.
- **Terraform Apply** : This will build the resources in GCP (GCS and BQ) needed for this project
- **Setting up Mage** : Go to Mage project folder and run docker-compose build and docker-compose up which will build the run docker-compose.yml file to run Mage
- **Running Mage locally** : Once the docker-compose up is executed successfully go to your web broswer and search for [localhost:6789](http://localhost:6789/overview?tab=week) which will launch Mage using your local port 6789
- Once the project is setup on an editor the folder structure should look like this.<br>
![image](https://github.com/joyrijith/Real_Estate_Sale_Connecticut/assets/89081604/7d1330d6-00cc-45bf-a609-ff02411fe750)

- **Pipelines in Mage** - Once the project is cloned in your editor and mage is opened in your browser using local port, 2 pipelines should be present in Mage. <br>
Below pipeline `Real_Estate_Sale_Connecticut_API_TO_GCS` has two loaders -
  - Loader `data_exporter_google_cloud_storage_full_file` loads the complete data set from the source into Google Cloud Storage as a parquet file. <br>
  - Loader `uploading_partitioned_file_to_gcs` loads the data set as partitioned parquet files in GCS. Partition is done based on every month.<br>
  
![image](https://github.com/joyrijith/Real_Estate_Sale_Connecticut/assets/89081604/cf2e21b8-3590-471a-b76c-8583171745ca)
![image](https://github.com/joyrijith/Real_Estate_Sale_Connecticut/assets/89081604/848bd806-134e-48a0-9640-ca13728fc3a5)

Pipeline `real_estate_sale_connecticut_gcs_to_bq_with_transformations` extracts the data from GCS cleans the data, removes unwanted data and then loads the cleaned data into BQ (DWH) <br>
![image](https://github.com/joyrijith/Real_Estate_Sale_Connecticut/assets/89081604/7dfc515b-df79-4524-8a07-6f13bac62cd6)

- **Modelling in dbt** - After creating profile in [dbt](https://auth.cloud.getdbt.com/) , set up your project <br>
Enter your project name, connect to the repository of your hcoice and connect to BQ to extract the data present in the DWH
![image](https://github.com/joyrijith/Real_Estate_Sale_Connecticut/assets/89081604/bb45dcdb-076a-4aad-8768-0cb08d66a3e8)

  

  
## Visualization and Key Insights 
## Contributions
