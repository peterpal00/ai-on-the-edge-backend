resource "github_repository" "ai-edge-backend" {
  name                   = "ai-on-the-edge-backend"
  description            = "A training project for creating a backend system and CI/CD."
  visibility            = "public"
  has_issues             = true
  has_wiki               = true
  has_downloads          = true
  allow_merge_commit     = true
  allow_squash_merge     = false
  allow_rebase_merge     = false
  allow_auto_merge       = true
  delete_branch_on_merge = false
  default_branch         = "develop"
  vulnerability_alerts   = true
  allow_update_branch    = true
}

# add collaborators
resource "github_repository_collaborator" "peterpal00" {
  repository = var.repo_name
  username   = "peterpal00"
  permission = "admin"
}

resource "github_repository_label" "bug" {
  repository = var.repo_name
  name       = "bug"
  color      = "CC0000"
  description = "An issue with the system 🐛."
}

resource "github_repository_label" "feature" {
  repository = var.repo_name
  name       = "feature"
  color      = "#336699"
  description = "New functionality."
}

resource "github_repository_label" "dependencies" {
  repository = var.repo_name
  name       = "dependencies"
  color      = "#b4a8d1"
  description = "Issue related to dependencies."
}

resource "github_repository_label" "documentation" {
  repository = var.repo_name
  name       = "documentation"
  color      = "#0052cc"
  description = "Creating docs."
}

resource "github_repository_label" "refactoring" {
  repository = var.repo_name
  name       = "refactoring"
  color      = "#fbca04"
  description = "Changes in the way the code works internally without changing the output produced. Contrast to \"cleanup\"."
}

resource "github_repository_label" "techdept" {
  repository = var.repo_name
  name       = "techdept"
  color      = "#ff7619"
  description = "Changes that remove or significantly update old unused code and/or dependencies."
}

resource "github_repository_label" "CI_CD" {
  repository = var.repo_name
  name       = "CI/CD"
  color      = "#5319e7"
  description = "Everything which related to CI/CD."
}
