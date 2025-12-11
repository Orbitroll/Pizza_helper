# Edit this file with your actual AWS credentials
# Then run it: .\init_with_creds.ps1

$Env:AWS_ACCESS_KEY_ID = "YOUR_ACCESS_KEY_HERE"
$Env:AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_KEY_HERE"
$Env:AWS_DEFAULT_REGION = "us-east-1"

Write-Host "Credentials set. Initializing Terraform..."
terraform init
