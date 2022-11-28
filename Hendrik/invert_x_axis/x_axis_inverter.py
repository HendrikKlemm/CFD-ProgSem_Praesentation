import json
import pandas as pd

# INPUTS
json_file_name = "filenames_for_inversion.json" # contains .csv files

#FUNCTIONS
def get_file_list(json_file_name):
    """returns list of files specified in the json file

    Arguments:
    json_file_name: str, file name of json file
    
    Returns: 
    file_list: list of strings, csv file names
    """
    with open(json_file_name, "r") as f:
        file_list = json.load(f)
        file_list = file_list["files"]
    return file_list

def invert_rows(file_list):
    """loops over csv files in file_list and inverts rows

    Arguments:
    file_list: list of strings, csv file names
    
    Returns:
    
    """
    for file in file_list:
        df_in = pd.read_csv(file)
        print(df_in.head())
        
        df_out = df_in.reindex(index=df_in.index[::-1])
        print(df_out.head())
        
        df_out.to_csv('out_'+file, sep=',', index=0, index_label=0)

if __name__ == '__main__':
    file_list = get_file_list(json_file_name)
    invert_rows(file_list)