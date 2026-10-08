"""import pandas as pd
from pathlib import Path

def combine_txt_dataframes(directory, output_file="combined.csv"):
    directory = Path(directory)

    dataframes = []

    for file in directory.glob("*.txt"):
        try:
            df = pd.read_csv(file, sep=r"\s+", engine="python")

            if not df.empty:
                dataframes.append(df)
                print(f"Loaded: {file.name} -> {df.shape}")

        except Exception as e:
            print(f"Skipped {file.name}: {e}")

    if not dataframes:
        print("No valid data found.")
        return

    combined = pd.concat(dataframes, ignore_index=True)

    combined.to_csv(output_file, index=False)

    print(f"\nCombined shape: {combined.shape}")
    print(f"Saved to: {output_file}")


# Example
combine_txt_dataframes(
    "root",
    "combined_Test.csv"
)"""








