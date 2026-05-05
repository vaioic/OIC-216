import pandas as pd

def analyze_from_csv(file_path, output_path):
    # 1. Load the data
    df = pd.read_csv(file_path)

    # 2. Define the organelles of interest
    target_organelles = ["Mitochondria", "Lysosome", "ER", "Golgi body"]

    # 3. Create a summary of TOTAL AREAS
    # Group by mouse and cell, then turn the 'class' names into columns
    area_pivot = df.groupby(['mouse', 'cell_id', 'class'])['area_mu2'].sum().unstack('class').fillna(0)

    # 4. Create a summary of COUNTS (number of organelles)
    # We count the 'label' column to see how many objects were in each class
    count_pivot = df.groupby(['mouse', 'cell_id', 'class'])['label'].count().unstack('class').fillna(0)

    # 5. Initialize the final analysis dataframe
    # We use the index from our pivots (mouse + cell_id)
    analysis = pd.DataFrame(index=area_pivot.index)

    # 6. Add Total Cell Area
    # This assumes your "container" class is named "Cell"
    if 'Cell' in area_pivot.columns:
        analysis['total_cell_area'] = area_pivot['Cell']
    else:
        # If 'Cell' label is missing, we can't calculate ratios
        analysis['total_cell_area'] = 0

    # 7. Loop through each organelle to build the specific columns
    for org in target_organelles:
        # Check if the organelle exists in any of the images
        if org in area_pivot.columns:
            analysis[f'num_{org.lower()}'] = count_pivot[org].astype(int)
            analysis[f'total_{org.lower()}_area'] = area_pivot[org]
            
            # Calculate Ratio: (Organelle Total Area / Cell Total Area)
            # Use a check to avoid division by zero
            analysis[f'{org.lower()}_to_cell_ratio'] = (
                analysis[f'total_{org.lower()}_area'] / analysis['total_cell_area']
            ).replace([float('inf'), -float('inf')], 0).fillna(0)
        else:
            # If the organelle was never found, fill with zeros
            analysis[f'num_{org.lower()}'] = 0
            analysis[f'total_{org.lower()}_area'] = 0.0
            analysis[f'{org.lower()}_to_cell_ratio'] = 0.0

    # 8. Save the results
    analysis.reset_index().to_csv(output_path, index=False)
    print(f"Analysis complete. Results saved to {output_path}")

# Run the function
analyze_from_csv("test/combined_data.csv", "test/organelle_summary_stats.csv")