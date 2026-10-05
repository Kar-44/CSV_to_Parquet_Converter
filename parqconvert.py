import pandas as pd
import argparse
import os
import glob

def convert_csv_to_parquet(csv_path: str, parquet_path: str = None):
    """
    Converts a single CSV file to Parquet format.
    """
    # If no output path is provided, use the original filename with a .parquet extension
    if parquet_path is None:
        parquet_path = os.path.splitext(csv_path)[0] + '.parquet'

    try:
        print(f"Reading {csv_path}...")
        # Read the CSV into a pandas DataFrame
        # For extremely large files, consider pyarrow.csv.read_csv instead to save memory
        df = pd.read_csv(csv_path)

        print(f"Converting to {parquet_path}...")
        # Save the DataFrame as a Parquet file
        # 'pyarrow' engine is the industry standard for fast, compressed Parquet files
        df.to_parquet(parquet_path, engine='pyarrow', index=False)

        print(f"Successfully converted: {parquet_path}")

    except Exception as e:
        print(f"Error converting {csv_path}: {e}")

def batch_convert(directory: str):
    """
    Converts all CSV files in a given directory to Parquet format.
    """
    # Look for all files ending in .csv in the target directory
    csv_files = glob.glob(os.path.join(directory, '*.csv'))

    if not csv_files:
        print(f"No CSV files found in directory: {directory}")
        return

    print(f"Found {len(csv_files)} CSV file(s). Starting batch conversion...\n")
    for csv_file in csv_files:
        convert_csv_to_parquet(csv_file)

if __name__ == "__main__":
    # Setup argparse so the script can be run easily from the command line
    parser = argparse.ArgumentParser(description="Convert CSV file(s) to Parquet format.")
    parser.add_argument(
        "input",
        help="Path to a single CSV file, or a directory containing CSV files."
    )

    args = parser.parse_args()
    input_path = args.input

    # Determine if the user passed a directory or a single file
    if os.path.isdir(input_path):
        batch_convert(input_path)
    elif os.path.isfile(input_path) and input_path.lower().endswith('.csv'):
        convert_csv_to_parquet(input_path)
    else:
        print("Invalid input. Please provide a valid CSV file path or a directory path.")