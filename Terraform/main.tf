terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.34.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_location)
  project     = var.project_name
  region      = var.google_provider_region
}

resource "google_storage_bucket" "google_cloud_bucket_for_real_estate_data" {
  name          = var.GCS_Bucket_name
  location      = var.gcs_bucket_location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "bigqeury_for_real_estate_data" {
  dataset_id = var.BQ_Dataset

}  