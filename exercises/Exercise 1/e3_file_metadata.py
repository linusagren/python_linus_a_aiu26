from pathlib import Path
from datetime import datetime

file_path = Path("e3_metadata.log")
metadata = file_path.stat()

file_name = file_path.name #.stem for no suffix
file_size = metadata.st_size
last_modified = datetime.fromtimestamp(metadata.st_mtime)

print("=== File metadata ===")
print(f"Filename: {file_name}")
print(f"Size (MB): {round(file_size / 1024**2, 1)}")
print(f"Last Modified Year: {last_modified.year}")