#!/bin/bash

# Define the main directory
repo_name="python-series"

# Create the main directory
mkdir $repo_name
cd $repo_name

# Create a README file
echo "Python Series Repository" > README.md
echo "This repository contains materials for the Python video series, including code examples, notes, and additional resources." >> README.md

# Function to create subdirectories and files for each part
create_part() {
    mkdir "part-$1-$2"
    cd "part-$1-$2"
    mkdir code-examples
    mkdir notes
    mkdir resources
    echo "Code examples for Part $1: $2" > code-examples/README.md
    echo "Notes for Part $1: $2" > notes/README.md
    echo "Resources for Part $1: $2" > resources/README.md
    cd ..
}

# Create directories for each part
parts=("01-intro-to-python" "02-data-types-and-structures" "03-control-structures" "04-functions-and-modules" "05-advanced-data-structures" "06-object-oriented-programming" "07-error-and-exception-handling" "08-file-handling-and-io" "09-external-libraries-and-tools" "10-python-in-practice" "11-advanced-topics")
for part in "${parts[@]}"; do
    IFS='-' read -ra ADDR <<< "$part"
    create_part "${ADDR[0]}" "${ADDR[1]}"
done

# Create the final project directory
mkdir final-project
cd final-project
echo "Final Project for the Python Series" > project-description.md
mkdir starter-code
mkdir solution
echo "Starter code for the final project" > starter-code/README.md
echo "Sample solution for the final project" > solution/README.md
cd ..

# Create additional materials directory
mkdir additional-materials
cd additional-materials
mkdir challenges
mkdir quizzes
mkdir case-studies
echo "Coding challenges for the Python series" > challenges/README.md
echo "Quizzes for the Python series" > quizzes/README.md
echo "Case studies related to the Python series" > case-studies/README.md
cd ..

# End script
echo "Repository structure for '$repo_name' created successfully."
