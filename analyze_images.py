import argparse
import pandas as pd
import numpy as np
from statistics import mean, stdev
from pathlib import Path

def process_directory(input_dir, output_dir):

    if isinstance(input_dir, str):
        input_dir = Path(input_dir)
    elif isinstance(input_dir, Path):
        pass
    else:
        raise TypeError(f"Expected input directory to be a str or Path. Instead it was a {type(input_dir)}")
    
    if not input_dir.exists:
        raise FileNotFoundError(f"The path ''{input_dir}'' was not found.")
    
    if isinstance(output_dir, str):
        output_dir = Path(output_dir)
    elif isinstance(output_dir, Path):
        pass
    else:
        raise TypeError(f"Expected output directory to be a str or Path. Instead it was a {type(output_dir)}")
    
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    # Find all files with "-labels.tif"
    label_files = list(input_dir.rglob("*-labels.tif"))

    if not label_files:
        raise FileNotFoundError(f"No labeled files were found on path {input_dir}")
    else:
        print(f"Found {len(label_files)} files.")


    pass

def process_image(input_image, output_dir):

    pass

def main():
    parser = argparse.ArgumentParser(description="Script to analyze organelles.")
    parser.add_argument("input_dir", type=str, help="Input directory of masks")
    parser.add_argument("output_dir", type=str, help="Output directory")
    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()