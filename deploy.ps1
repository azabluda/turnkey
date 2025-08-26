# Deploy ECR, build and push Docker image, then deploy main stack
param(
    [string]$Region = "eu-central-1",
    [string]$ImageTag = "latest"
)

# Step 1: Deploy ECR stack
Write-Host "Deploying ECR stack..."
&{ aws cloudformation deploy --template-file .\templates\ecr-only.yaml --stack-name turnkey-ecr --region $Region; if(!$?){throw} }

# Step 2: Get ECR URI
$ecrUri = &{ aws cloudformation describe-stacks --stack-name turnkey-ecr --region $Region --query "Stacks[0].Outputs[?OutputKey=='ECRRepositoryUri'].OutputValue" --output text; if(!$?){throw} }
Write-Host "ECR URI: $ecrUri"

# Step 3: Build Docker image
Write-Host "Building Docker image..."
&{ docker build -t "${ecrUri}:$ImageTag" .; if(!$?){throw} }

# Step 4: Authenticate Docker to ECR
Write-Host "Authenticating Docker to ECR..."
&{ aws ecr get-login-password --region $Region | docker login --username AWS --password-stdin $ecrUri; if(!$?){throw} }

# Step 5: Push Docker image
Write-Host "Pushing Docker image..."
&{ docker push "${ecrUri}:$ImageTag"; if(!$?){throw} }

# Step 6: Deploy main stack
Write-Host "Deploying main stack..."
&{ aws cloudformation deploy --template-file .\templates\main.yaml --stack-name turnkey-main --region $Region --capabilities CAPABILITY_NAMED_IAM --parameter-overrides ECRRepositoryUri="${ecrUri}:$ImageTag"; if(!$?){throw} }

Write-Host "Deployment complete."

# Print the public URL of the EC2 instance running the webapp
$instanceId = &{ aws cloudformation describe-stack-resources --stack-name turnkey-main --region $Region --logical-resource-id ECSContainerInstance --query "StackResources[0].PhysicalResourceId" --output text; if(!$?){throw} }
$publicIp = &{ aws ec2 describe-instances --instance-ids $instanceId --region $Region --query "Reservations[0].Instances[0].PublicIpAddress" --output text; if(!$?){throw} }
Write-Host "Webapp is available at: http://$publicIp/"
