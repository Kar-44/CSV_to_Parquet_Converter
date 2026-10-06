# CSV to Parquet converter

A simple way to convert CSV files into Parquet.

## Requirements
Installed `pandas` and `pyarrow` 

```bash
pip install pandas pyarrow
```

## How to run:
1. Open the script
2. In script's terminal type: "python3 parqconvert.py /path/to/your/file.csv"
3. If everything went correctly, you should receive a SUCCESS message in the terminal and a parquet file in the same folder as the CSV file.

## Why use Parquet format?
Parquet is column based greatly compressed binary format. It improves performance on large datasets and saves storage. I originally made this converter as a complimentary program
to my other project - Backtesting Engine. The Backtesting engine needs to take in large amount of market data which is often in CSV files in publically accessible sources.
Converting large dataset from CSV to Parquet greatly increases performance.
