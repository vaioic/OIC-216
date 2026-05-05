import argparse
import pandas as pd
import numpy as np
from statistics import mean, stdev
from pathlib import Path
import skimage as sk
import xarray as xr
import re

def process_directory(input_dir, output_dir):

    if isinstance(input_dir, str):
        input_dir = Path(input_dir)
    elif isinstance(input_dir, Path):
        pass
    else:
        raise TypeError(f"Expected input directory to be a str or Path. Instead it was a {type(input_dir)}")
    
    if not input_dir.exists():
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

    all_ds = []

    for lf in label_files:
        ds = process_image(lf, output_dir)
        all_ds.extend(ds)

    combined_ds = xr.concat(all_ds, dim="id", coords="different")

    combined_ds.to_netcdf(output_dir / "data.nc")
    
    # Save as CSV
    df = combined_ds.to_dataframe()
    df.to_csv(output_dir / "combined_data.csv")

    print("Processing complete.")

def process_image(label_image_path, output_dir):

    if isinstance(label_image_path, str):
        label_image_path = Path(label_image_path)
    elif isinstance(label_image_path, Path):
        pass
    else:
        raise TypeError(f"Expected the label_image_path type to be a str or Path. Instead it was a {type(label_image_path)}")
    
    # List of cell types
    class_list = ["None", "Cell", "Mitochondria", "Golgi body", "Lysosome", "Secondary Lysosome", "ER", "Autophagosome", "MVB", "Vacuole", "ILV", "Unsure"]

    # Get the cell ID
    cell_id_match = re.findall(r"\d+", label_image_path.parent.parent.parent.name)
    cell_id_str = cell_id_match[0]    

    # Get the mouse number
    mouse_id_match = re.findall(r"\d+", label_image_path.parent.parent.parent.parent.name)
    mouse_id_str = mouse_id_match[0]

    
    img = sk.io.imread(label_image_path)



    all_ds = []

    if label_image_path.stem == "1-labels":
        props = sk.measure.regionprops_table(img, properties=("label", "centroid", "area"), spacing=(0.0120, 0.0120))

        curr_ds = xr.Dataset(
            data_vars={
                "class": (["id"], ["Cell"]),
                "class_label": (["id"], [1]),  # There should only be 1
                "label": (["id"], props["label"]),
                "area_mu2": (["id"], props["area"]),
                "centroid-0": (["id"], props["centroid-0"]),
                "centroid-1": (["id"], props["centroid-1"]),
            },
            coords={"mouse": mouse_id_str,
                    "cell_id": cell_id_str,
                    "filepath": label_image_path.name}
        )

        all_ds.append(curr_ds)

    else:

        for iClass in range(2, 11):

            curr_mask = img == iClass

            if not np.any(curr_mask):
                continue
            else:
                curr_label = sk.measure.label(curr_mask)
                            
                props = sk.measure.regionprops_table(curr_label, properties=("label", "centroid", "area"), spacing=(0.003, 0.003))

                curr_ds = xr.Dataset(
                    data_vars={
                        "class": (["id"], [class_list[iClass]] * len(props["label"])),
                        "class_label": (["id"], [iClass] * len(props["label"])),
                        "label": (["id"], props["label"]),
                        "area_mu2": (["id"], props["area"]),
                        "centroid-0": (["id"], props["centroid-0"]),
                        "centroid-1": (["id"], props["centroid-1"]),
                    },
                    coords={"mouse": mouse_id_str,
                            "cell_id": cell_id_str,
                            "filepath": label_image_path.name}
                )

                all_ds.append(curr_ds)

    return all_ds

    
def main():
    parser = argparse.ArgumentParser(description="Script to analyze organelles.")
    parser.add_argument("input_dir", type=str, help="Input directory of masks")
    parser.add_argument("output_dir", type=str, help="Output directory")
    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()