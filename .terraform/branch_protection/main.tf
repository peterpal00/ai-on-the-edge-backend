resource "github_branch_protection" "develop" {
  repository = var.repo_name
  pattern    = "develop"

  enforce_admins       = false
  require_code_owner_reviews = true
  dismiss_stale_reviews     = true
  require_up_to_date          = true
  require_signed_commits = true
  include_admins = false
  restrict_review_dismissals = true
  allow_force_pushes = false
  allows_deletions =  false
  require_linear_history = false

  restrictions {
    users = ["peterpal00"]
  }

}

resource "github_branch_protection" "production" {
  repository = var.repo_name
  pattern    = "production"

  enforce_admins       = false
  require_code_owner_reviews = true
  dismiss_stale_reviews     = true
  require_up_to_date          = true
  require_signed_commits = true
  include_admins = false
  restrict_review_dismissals = true
  allow_force_pushes = false
  allows_deletions =  false
  require_linear_history = true

  restrictions {
    users = ["peterpal00"]
  }

}