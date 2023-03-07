import boto3
from pathlib import Path
import os
import glob
import pandas as pd
import json

def get_file_folders(s3_client, bucket_name, prefix=""):
    file_names = []
    folders = []

    default_kwargs = {
        "Bucket": bucket_name,
        "Prefix": prefix
    }
    next_token = ""

    while next_token is not None:
        updated_kwargs = default_kwargs.copy()
        if next_token != "":
            updated_kwargs["ContinuationToken"] = next_token

        response = s3_client.list_objects_v2(**default_kwargs)
        contents = response.get("Contents")

        for result in contents:
            key = result.get("Key")
            if key[-1] == "/":
                folders.append(key)
            else:
                file_names.append(key)

        next_token = response.get("NextContinuationToken")

    return file_names, folders


def download_files(s3_client, bucket_name, local_path, file_names, folders):

    local_path = Path(local_path)
    
    for folder in folders:
        folder_path = Path.joinpath(local_path, folder)
        folder_path.mkdir(parents=True, exist_ok=True)

    for idx, file_name in enumerate(file_names):
        file_path = Path.joinpath(local_path, file_name)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        s3_client.download_file(
            bucket_name,
            file_name,
            str(file_path)
        )
        print(idx, '/', len(file_names), ', installed to '+str(file_path))

def save_to_csv():
    df = pd.DataFrame()

    path = glob.glob('./Data/*')
    for file_path in path:
        with open(file_path, 'r') as file:
            json_dict = json.load(file)
            df = df.append(json_dict, ignore_index=True)
    df.to_csv('./all_data.csv', encoding="utf-8-sig")
    print('saved csv')

def main():
    client = boto3.client("s3")

    file_names, folders = get_file_folders(client, "awpsprocesseddata")
    download_files(
        client,
        "awpsprocesseddata",
        "./Data",
        file_names,
        folders
    )
    save_to_csv()

if __name__ == "__main__":
    main()