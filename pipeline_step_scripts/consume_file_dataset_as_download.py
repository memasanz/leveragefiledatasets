from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.core.model import Model
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
import tempfile

# Parse input arguments
parser = argparse.ArgumentParser("Consume File Dataset as Download")
parser.add_argument('--local_download_dir', type=str, required=True)

args, _ = parser.parse_known_args()
local_download_dir = args.local_download_dir

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Get default datastore
ds = ws.get_default_datastore()

target_file_path = os.path.join(local_download_dir, 'sample_data.csv')
sample_df = pd.read_csv(target_file_path)
print(sample_df)

target_file_path2 = os.path.join(local_download_dir, 'sample_data_2.csv')
sample_df2 = pd.read_csv(target_file_path2)
print(sample_df2)
