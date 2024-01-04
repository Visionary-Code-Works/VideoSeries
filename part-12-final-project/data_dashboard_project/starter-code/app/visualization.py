
import pandas as pd
import plotly.express as px

# Function to load processed data
def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

# Function to create a visualization
def create_visualization(data, column_name):
    """
    Creates a visualization for the given column in the dataset.
    :param data: DataFrame, the dataset.
    :param column_name: str, the name of the column to visualize.
    :return: plotly.graph_objects.Figure, the generated figure.
    """
    fig = px.histogram(data, x=column_name)
    return fig

# Function to save the visualization
def save_visualization(fig, filename):
    try:
        fig.write_html(filename)
        print("Visualization saved successfully.")
    except Exception as e:
        print(f"Error saving visualization: {e}")

# Main function to run the visualization process
def main():
    input_filepath = 'path/to/input/processed_data.csv' # Update this path
    output_filename = 'path/to/output/visualization.html' # Update this path

    # Load data
    data = load_data(input_filepath)
    if data is not None:
        # Create and save visualization
        fig = create_visualization(data, 'example_column') # Replace 'example_column' with your column name
        save_visualization(fig, output_filename)

if __name__ == "__main__":
    main()
