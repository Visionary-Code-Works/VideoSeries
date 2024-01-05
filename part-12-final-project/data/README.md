# Data

Several datasets available through libraries like Scikit-learn (sklearn), TensorFlow, and PyTorch can be used to represent different types of data you might encounter in a project like the Web-Based Data Dashboard. Here's how some of these datasets could fit into each category:

## 1. Raw Data (data/raw/)

- **Description**: Original, unmodified data files.
- **Examples**:
  - **Sklearn Datasets**: Datasets like `iris`, `digits`, or `wine` can be used as raw data. These are clean but unprocessed.
  - **TensorFlow Datasets**: Datasets like `MNIST` or `CIFAR-10` can represent raw image data.
  - **PyTorch Datasets**: Use datasets available in `torchvision.datasets` like `FashionMNIST` or `CelebA` as raw data examples.

## 2. Processed Data (data/processed/)

- **Description**: Data that has been cleaned, transformed, or otherwise processed.
- **Examples**:
  - Process sklearn's `iris` dataset by normalizing the features and encoding the labels.
  - For TensorFlow's `MNIST`, you could process the data by reshaping the images and normalizing pixel values.
  - In PyTorch, you might process `FashionMNIST` by applying transformations like normalization, resizing, or data augmentation techniques.

## 3. Intermediate Data (data/interim/)

- **Description**: Data partway through the cleaning or transformation process.
- **Examples**:
  - Intermediate sklearn data could be a partially imputed dataset or data with some features engineered.
  - In TensorFlow, intermediate data could be images that have been resized but not yet normalized.
  - For PyTorch, consider a dataset where certain preprocessing steps have been applied (e.g., converting to grayscale) but others are still pending.

## 4. External Data (data/external/)

- **Description**: Data from external sources, not generated within the project.
- **Examples**:
  - Any dataset not included by default in sklearn, TensorFlow, or PyTorch that you import from another source.
  - This could include datasets downloaded from other repositories or external APIs.

To use these datasets, you can typically import them directly from the respective libraries. For example, in sklearn, you can import datasets using `from sklearn.datasets import load_iris`. TensorFlow and PyTorch offer similar functions for accessing their datasets.

Remember, while these datasets are excellent for practice and examples, they are often clean and well-structured, unlike real-world raw data, which can be messy and require significant preprocessing.
