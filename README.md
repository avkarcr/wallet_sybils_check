# Wallet Sybil Detector

This script reads two input files: one containing a list of wallet addresses and another containing a Sybil database. It identifies occurrences of wallet addresses from the first file in the Sybil database and writes the results to an output file.

## Features

- Reads wallet addresses and Sybil database from specified files.
- Compares wallet addresses to identify occurrences in the Sybil database.
- Outputs the results to a specified file.
- Provides command-line interface for easy usage.

## Usage

### Command-Line Arguments

- `my_wallets.txt` (str): Path to the file containing wallet addresses.
- `sybils_database.txt` (str): Path to the Sybil database file.
- `-o` or `--output` (str, optional): Path to the output file. Default is `output.txt`.

### Example

```bash
python main.py my_wallets.txt sybils_database.txt -o output.txt
OR
python main.py my_wallets.txt sybils_database.txt
