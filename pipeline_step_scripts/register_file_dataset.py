
from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.core.model import Model
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
import yaml

# Parse input arguments
parser = argparse.ArgumentParser("Register File Dataset")
parser.add_argument("--input_json", type=str, dest='input_json', help='input json dataset')
parser.add_argument("--input_yaml", type=str, dest='input_yaml', help='input yaml dataset')
parser.add_argument('--sample_file_dataset', dest='sample_file_dataset', required=True)

args, _ = parser.parse_known_args()
input_json = args.input_json
input_yaml = args.input_yaml
sample_file_dataset = args.sample_file_dataset

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Get default datastore
ds = ws.get_default_datastore()

# Generate random sample data
random_df = pd.util.testing.makeDataFrame()
print(random_df)

random_df2 = pd.util.testing.makeDataFrame()
print(random_df2)

print("input file location")
print(input_json)
testObject = pd.read_json(path_or_buf=input_json, lines=True)
print(testObject)

print('*****************')
print("input yaml location")
print(input_yaml)



with open(input_yaml) as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)


# Save file dataset
os.makedirs(sample_file_dataset, exist_ok=True)
random_df.to_csv(os.path.join(sample_file_dataset, 'sample_data.csv'))
random_df2.to_csv(os.path.join(sample_file_dataset, 'sample_data_2.csv'))
