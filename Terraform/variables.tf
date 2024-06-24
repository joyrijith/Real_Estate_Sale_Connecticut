variable "BQ_Dataset" {
    description = "BQ Dataset name for Real_Estate_Sale Project"
    default = "real_estate_sale"
  
}

variable "GCS_Bucket_name" {
    description = "My GCS bucket name for Real_Estate_Sale Project"
    default = "real_estate_sale_connecticut"
  
}

variable "credentials_location" {
    description = "my credentials location"
    default = "./keys/creds.json"
  
}

variable "project_name" {
    description = "my project name"
    default = "astute-backup-427300-m6"
  
}

variable "google_provider_region" {
    description = "My Google service provider region "
    default = "us-central1"
  
}


variable "gcs_bucket_location" {
    description = "My GCS bucket location "
    default = "US"
  
}