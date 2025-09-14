from datetime import datetime

title = "DevOps Infrastructure Documentation"
author = "Alex Brix"
date = datetime.now().strftime("%B %d, %Y")

content_latex = f"""
\\documentclass{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{geometry}}
\\geometry{{margin=1in}}
\\title{{{title}}}
\\author{{{author}}}
\\date{{{date}}}

\\begin{{document}}

\\maketitle

\\section{{Level 1 – Web Console}}
\\begin{{itemize}}
  \\item Login to AWS Web Console
  \\item Launch EC2 instance using public AMI
  \\item SSH access
  \\item Manual configuration
  \\item Manual deployment from Git
\\end{{itemize}}

\\section{{Level 2 – AWS CLI}}
\\begin{{itemize}}
  \\item Use \\texttt{{aws ec2 run-instances}}
  \\item Transition from GUI to CLI
  \\item Faster and repeatable flow
\\end{{itemize}}

\\section{{Level 3 – Infrastructure as Code}}

\\subsection{{Iteration 1 – Basic Terraform}}
\\begin{{verbatim}}
terraform init
terraform apply -auto-approve
\\end{{verbatim}}

\\subsection{{Iteration 2 – Configuration with user-data}}
\\begin{{verbatim}}
#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
systemctl start httpd
systemctl enable httpd
\\end{{verbatim}}

\\subsection{{Iteration 3 – Auto-deploy with user-data}}
Destroy everything $\rightarrow$ Add auto-deploy $\rightarrow$ Reconstruct $\rightarrow$ Verify

\\subsection{{Iteration 4 – Ansible Integration}}
\\begin{{verbatim}}
ansible-playbook -i inventory webserver.yml
\\end{{verbatim}}

\\subsection{{Iteration 5 – Git-based Source}}

The infrastructure code is hosted on GitHub at: \url{{https://github.com/alexbrix/infra}}{{github.com/alexbrix/infra}}.  
This repository contains reusable modules and automation scripts that support the entire deployment pipeline.

\\begin{{itemize}}
  \\item Terraform modules for EC2, VPC, and S3
  \\item Ansible playbooks for web server configuration
  \\item CI/CD pipeline definitions using CodePipeline and CodeBuild
  \\item Verification scripts and buildspec files
\\end{{itemize}}

To deploy the infrastructure:

\\begin{{verbatim}}
git clone https://github.com/alexbrix/infra.git
cd infra
terraform apply -auto-approve
\\end{{verbatim}}


\\subsection{{Iteration 6 – Shared Backend}}
\\begin{{verbatim}}
terraform {{  backend "s3" {{
    bucket         = "alexbrix-terraform-state"
    key            = "infra/terraform.tfstate"
    region         = "eu-north-1"
    dynamodb_table = "terraform-lock-alexbrix"
  }}
}}
\\end{{verbatim}}

\\subsection{{Iteration 7 – Optimization}}
\\begin{{verbatim}}
terraform plan > plan.log
grep "No changes" plan.log && echo "Everything is fine"
\\end{{verbatim}}

\\subsection{{Iteration 8 – Verification Script}}
\\begin{{verbatim}}
#!/bin/bash
terraform plan > verify.log
cat verify.log | grep "No changes"
\\end{{verbatim}}

\\section{{Level 4 – CI/CD and Security}}

\\subsection{{Iteration 1 – CodePipeline + CloudFormation}}
\\begin{{verbatim}}
aws cloudformation create-stack \\
  --stack-name InfraStack \\
  --template-body file://infra.yaml \\
  --capabilities CAPABILITY_IAM
\\end{{verbatim}}

\\subsection{{Iteration 2 – SSM Agent}}
\\begin{{verbatim}}
sudo yum install -y amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
aws ssm start-session --target i-xxxxxxxxxxxx
\\end{{verbatim}}

\\subsection{{Iteration 3 – Security Hardening}}
\\begin{{verbatim}}
aws ec2 revoke-security-group-ingress \\
  --group-id sg-0a1b2c3d4e5f6g7h8 \\
  --protocol tcp --port 22 --cidr 0.0.0.0/0
\\end{{verbatim}}

\\subsection{{Iteration 4 – Automated Verification with CodeBuild}}
\\begin{{verbatim}}
version: 0.2
phases:
  build:
    commands:
      - echo "Verifying infrastructure..."
      - terraform plan
\\end{{verbatim}}

\\section{{Resources Used}}
\\begin{{itemize}}
  \\item S3 Bucket: \\texttt{{alexbrix-terraform-state}}
  \\item DynamoDB Table: \\texttt{{terraform-lock-alexbrix}}
  \\item EC2 Instance:
    \\begin{{itemize}}
      \\item Public IP: \\texttt{{13.53.124.87}}
      \\item Private IP: \\texttt{{10.0.1.15}}
      \\item Region: \\texttt{{eu-north-1}}
      \\item Tag: \\texttt{{webserver-alexbrix}}
      \\item Security Group: \\texttt{{sg-0a1b2c3d4e5f6g7h8}}
    \\end{{itemize}}
\\end{{itemize}}

\\section{{Reflection}}
This iteration marks the transition from manual verification to automated workflows. I learned to use CodeBuild effectively, write and test buildspec.yml files, and apply secure flows using CloudFormation ChangeSets. This step improved both the security and efficiency of the infrastructure.

\\end{{document}}
"""

with open("project_documentation.tex", "w", encoding="utf-8") as f:
    f.write(content_latex)

print("Documentation generated: project_documentation.tex")

