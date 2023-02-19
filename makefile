tf_plan:
	terraform plan -out=tfplan -detailed-exitcode

tf_apply:
	terraform apply tfplan