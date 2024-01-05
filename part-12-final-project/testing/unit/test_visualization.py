
import unittest
import pandas as pd
from visualization import create_visualization

class TestVisualization(unittest.TestCase):
    def test_create_visualization(self):
        # Test for create_visualization function
        data = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [5, 4, 3, 2, 1]})
        fig = create_visualization(data, 'col1')
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
