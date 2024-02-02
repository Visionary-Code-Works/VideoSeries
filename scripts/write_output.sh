#!/bin/bash

# Base directory containing all parts
base_dir="./"

# Find all part directories and loop through them
find "$base_dir" -type d -name 'part-*' | while read part_dir; do
    echo "Processing $part_dir"

    # Output file for this part
    output_file="${part_dir}/part_output.txt"

    # Ensure the output file is empty
    > "$output_file"

    # Concatenate files from each subdirectory
    for sub_dir in code-examples exercises notes quizzes resources; do
        if [[ -d "${part_dir}/${sub_dir}" ]]; then
            echo "Adding ${sub_dir} to ${output_file}"

            # Add subdirectory name and dashes to output
            echo -e "\n$sub_dir\n$(printf '%.0s-' {1..80})\n" >> "$output_file"

            # Concatenate all files in subdirectory to output
            cat "${part_dir}/${sub_dir}"/* >> "$output_file"

            # Add dashes after each section except the last
            if [[ "$sub_dir" != "resources" ]]; then
                echo -e "\n$(printf '%.0s-' {1..80})\n" >> "$output_file"
            fi
        fi
    done
done

echo "Processing complete."
