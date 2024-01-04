#!/bin/bash

# Create the base directory for the project (replace 'data_dashboard_project' with your project name)
mkdir data_dashboard_project
cd data_dashboard_project

# Create and touch files in the root directory
touch README.md
touch project-description.md

# Create subdirectories
mkdir starter-code
mkdir solution
mkdir testing
mkdir resources

# Create files inside 'starter-code'
cd starter-code
touch app.py
touch requirements.txt
mkdir templates
mkdir static
cd ..

# Create a markdown file inside 'solution'
cd solution
touch Walkthrough.md
cd ..

# Create testing related files
cd testing
touch unit_tests.py
touch debugging_guide.md
cd ..

# Create resource related files
cd resources
touch API_Documentation.md
touch Flask_Pandas_Plotly_Resources.md
cd ..

# Optional files
touch data_processing.py
touch visualization.py

echo "Project directory structure created successfully."
