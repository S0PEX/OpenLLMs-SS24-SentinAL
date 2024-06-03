# Getting Started with SentinAL

Welcome to the SentinAL (Sentiment Analysis Generalization Experiment) repository! This guide will help you get started with setting up the project environment and understanding the file structure.

## Cloning the Repository

To begin, clone the SentinAL repository from GitHub. You can use the following command in your terminal:

```
git clone https://github.com/S0PEX/OpenLLMs-SS24-SentinAL.git
```

## Setting Up Python Virtual Environment

Once you've cloned the repository, navigate to the project directory and create a Python virtual environment. You can do this using the following commands:

```shell
$ cd OpenLLMs-SS24-SentinAL
$ python3 -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```shell
  $ venv\Scripts\activate
  ```
- On macOS and Linux:
  ```shell
  $ source venv/bin/activate
  ```

## Installing Requirements

With the virtual environment activated, install the required Python packages listed in `requirements.txt`. Use the following command:

```shell
$ pip install -r requirements.txt
```

## Folder Structure

Here's an overview of the folder structure:

- **data/**: Contains subdirectories for storing raw data, processed data, and evaluation results.
- **models/**: Stores the pre-trained model configurations and weights for each OpenLLM.
- **notebooks/**: Holds Jupyter notebooks for data preparation, model evaluation, and error analysis.
- **src/**: Contains Python source code for data preprocessing, model implementation, evaluation, and utility functions.
