import json
import pandas as pd

with open("filenames_for_inversion.json", "r") as f:
    file_list = json.load(f)
    file_list = file_list["files"]

for file in file_list:
    df_in = pd.read_csv(file)
    print(df_in.head())
    
    df_out = df_in.reindex(index=df_in.index[::-1])
    print(df_out.head())
    
    df_out.to_csv('out_'+file, sep=',', index=0, index_label=0)