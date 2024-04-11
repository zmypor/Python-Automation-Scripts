import pandas as pd

def read_excel(file_path):
  df = pd.read_excel(file_path)
  return df

def write_to_excel(data, file_path):
  df = pd.DataFrame(data)
  df.to_excel(file_path, index=False)