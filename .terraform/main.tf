terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.TF_TOKEN
}


module "repository_settings" {
  source = "./modules/repository_settings"
}


module "branch_protection" {
  source = "./modules/branch_protection"
}