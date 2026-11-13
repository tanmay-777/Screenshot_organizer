from pathlib import Path
import re
import shutil
import time


        

        



def extract_game_name(file_stem):
    full_game_name = file_stem.split()

    name_parts = ""
    for words in full_game_name:
        if re.fullmatch(r"\d{2}-\d{2}-\d{4}",words):
            break
        name_parts = (f"{name_parts} {words}")
    clean_name = name_parts.strip()
    if not clean_name:
        clean_name = "Unorganised"
    return clean_name
    

def organize_captures(source_folder,parent_destination_folder,dry_run=True):
    for item in source_folder.iterdir():
        if item.is_file() and (item.suffix.lower() == ".png" or item.suffix.lower() == ".jxr"):
            game_destination_folder = ""
            destination_file = ""
            clean_name = extract_game_name(item.stem)
            game_destination_folder = parent_destination_folder / clean_name
            destination_file = game_destination_folder / item.name

            if dry_run:
                print(f"[DRY RUN]: {item.name} ----> {clean_name}/{item.name}")
            else:
                print(f"[MOVED] {item.name} ----> {clean_name}/{item.name}")
                game_destination_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(item,destination_file)

if __name__ == "__main__":
    folder = Path(r"D:\Programming Projects\Github_files\test_captures")
    parent_destination_folder = Path(r"D:\Programming Projects\Github_files\test_organised_folder")
    DRY_RUN = True
    organize_captures(folder,parent_destination_folder, DRY_RUN)