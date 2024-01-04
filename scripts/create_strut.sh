#!/bin/bash

# Base project directory
mkdir -p data_dashboard_project
cd data_dashboard_project

# Root directory files
touch README.md
touch project-description.md
touch .gitignore
touch LICENSE

# Starter code directory and subdirectories
mkdir -p starter-code/app/main
touch starter-code/app/main/__init__.py
touch starter-code/app/main/routes.py
touch starter-code/app/app.py
touch starter-code/app/config.py

mkdir -p starter-code/requirements
touch starter-code/requirements/dev.txt
touch starter-code/requirements/prod.txt

mkdir -p starter-code/templates/partials
mkdir -p starter-code/static/css
mkdir -p starter-code/static/js
mkdir -p starter-code/static/images

# Solution directory and subdirectories
mkdir -p solution/src
mkdir -p solution/docs
touch solution/docs/Walkthrough.md

# Testing and debugging
mkdir -p testing/unit
mkdir -p testing/integration
mkdir -p testing/test_data
touch testing/debugging_guide.md

# Resources
mkdir -p resources/API_Docs
mkdir -p resources/Tutorials
mkdir -p resources/Reference_Materials

# Data directory
mkdir -p data/raw
mkdir -p data/interim
mkdir -p data/processed
mkdir -p data/external

# Scripts
mkdir -p scripts/utility_scripts
touch scripts/data_processing.py
touch scripts/visualization.py

# Deployment
mkdir -p deployment/Docker
mkdir -p deployment/cloud
mkdir -p deployment/CI_CD
touch deployment/deployment_guide.md

# Environment and Configuration
mkdir -p config/env_vars
touch config/settings.py

# User documentation
mkdir -p user_docs
touch user_docs/User_Guide.md
touch user_docs/FAQ.md
touch user_docs/Troubleshooting.md

# Project management
mkdir -p project_management
touch project_management/roadmap.md
touch project_management/changelog.md
touch project_management/contribution.md

echo "Project directory structure created successfully."
