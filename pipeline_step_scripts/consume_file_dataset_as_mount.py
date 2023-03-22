from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.core.model import Model
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
import tempfile

# Parse input arguments
parser = argparse.ArgumentParser("Consume File Dataset as Mount")

args, _ = parser.parse_known_args()

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Get default datastore
ds = ws.get_default_datastore()

# Get dataset path
file_dataset = current_run.input_datasets['sample_file_dataset']

target_file_path = os.path.join(file_dataset, 'sample_data.csv')
sample_df = pd.read_csv(target_file_path)
print(sample_df)

target_file_path2 = os.path.join(file_dataset, 'sample_data_2.csv')
sample_df2 = pd.read_csv(target_file_path2)
print(sample_df2)
