import unittest
import pandas as pd
from data_processing import load_data, preprocess_data, save_processed_data


class TestDataProcessing(unittest.TestCase):
    def test_load_data(self):
        # Test for load_data function
        data = load_data("path/to/test/data.csv")  # Replace with a valid test data path
        self.assertIsInstance(data, pd.DataFrame)

    def test_preprocess_data(self):
        # Test for preprocess_data function
        data = pd.DataFrame({"col1": [1, 2, None], "col2": [4, None, 6]})
        processed_data = preprocess_data(data)
        self.assertFalse(processed_data.isnull().values.any())

    def test_save_processed_data(self):
        # Test for save_processed_data function
        data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        save_processed_data(
            data, "path/to/output/test_processed_data.csv"
        )  # Replace with a valid output path
        loaded_data = pd.read_csv(
            "path/to/output/test_processed_data.csv"
        )  # Replace with the same valid output path
        self.assertTrue(loaded_data.equals(data))


if __name__ == "__main__":
    unittest.main()
