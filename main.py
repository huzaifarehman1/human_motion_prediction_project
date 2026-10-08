from pathlib import Path

def combine_txt_files(directory):
    directory = Path(directory)
    combined = []

    for file in directory.glob("*.txt"):
        try:
            content = file.read_text(encoding="utf-8").strip()

            # Only include TXT files that contain data
            if content:
                combined.append(content)

        except UnicodeDecodeError:
            print(f"Skipped (not UTF-8): {file}")

    return "\n".join(combined)


# Example
directory = "/home/huzaifa/Code/AI_ML/DL/human_activity/UCI HAR Dataset/UCI HAR Dataset/train/Inertial Signals"

result = combine_txt_files(directory)





