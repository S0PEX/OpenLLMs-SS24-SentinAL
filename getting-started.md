# Getting Started with SentinAL

Welcome to the SentinAL (Sentiment Analysis Generalization Experiment) repository! This guide will help you get started with setting up the project environment and understanding the file structure.

## Warning

In order for the Jupyter notebook to function correctly, please ensure that the Python base path is set to the project's root directory. For Visual Studio Code users, you can set `jupyter.notebookFileRoot` to `${workspaceFolder}` in your settings.

```json
// .vscode/settings.json
{
  "jupyter.notebookFileRoot": "${workspaceFolder}"
}
```

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

Below is an outline of the folder structure:

- **data/**: This directory contains subfolders for storing raw data, processed data, and evaluation results.
- **models/**: Here, you'll find the pre-trained model configurations and weights for each OpenLLM. Since some models are implemented using Hugging Face Transformers, the weights and configurations will be downloaded during runtime. Therefore, we only provide their transformer pipeline implementation adapted to our generic model class.
- **notebooks/**: This section holds Jupyter notebooks for data preparation, model evaluation, and error analysis.
- **src/**: In this directory, you'll find Python source code for data preprocessing, model implementation, evaluation, and utility functions.
