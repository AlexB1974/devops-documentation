# DevOps Documentation Generator

This project automates the creation of infrastructure documentation using LaTeX. It generates a structured `.tex` file that describes each layer of a DevOps setup, including manual provisioning, CLI usage, Infrastructure as Code, CI/CD pipelines, and security hardening.

## Files Included

- `generate_documentation.py`: Python script that builds the LaTeX document
- `project_documentation.tex`: Output file containing the full infrastructure documentation

## How to Use

1. Clone the repository:
   git clone https://github.com/AlexB1974/devops-documentation.git
   cd devops-documentation

2. Run the Python script:
   python3 generate_documentation.py

3. Open the generated `.tex` file in your LaTeX editor (TeXworks, Overleaf, Sublime Text)

4. Compile to PDF using pdflatex:
   pdflatex project_documentation.tex

## Requirements

- Python 3.x
- LaTeX distribution (TeX Live, MiKTeX)
- Git (optional)

## Technologies Covered

- AWS EC2, S3, DynamoDB
- Terraform and Ansible
- CodePipeline and CodeBuild
- CloudFormation
- Bash scripting
- GitHub integration

## Future Improvements

- Add architecture diagrams
- Include cost estimation
- Integrate CloudWatch monitoring
- Implement blue/green deployments

## Author

Alex Brix  
GitHub: https://github.com/AlexB1974

## License

This project is licensed under the MIT License.

