from pathlib import Path
import re
import shutil
import time

folder = Path(r"D:\Programming Projects\Github_files\test_captures")
parent_destination_folder = Path(r"D:\Programming Projects\Github_files\test_organised_folder")
DRY_RUN = False
game_name = []
for item in folder.iterdir():
    if item.is_file() and (item.suffix.lower() == ".png" or item.suffix.lower() == ".jxr"):
        game_destination_folder = ""
        destination_file = ""

        full_game_name = item.stem.split()
        
        name_parts = ""
        for words in full_game_name:
            if re.fullmatch(r"\d{2}-\d{2}-\d{4}",words):
                break
            name_parts = (f"{name_parts} {words}")
        clean_name = name_parts.strip()
        if not clean_name:
            clean_name = "Unorganised"
    
        game_name.append(clean_name)
        game_name = list(dict.fromkeys(game_name))

        game_destination_folder = parent_destination_folder / clean_name
        destination_file = game_destination_folder / item.name

        if DRY_RUN:
            print(f"[DRY RUN]: {item.name} ----> {clean_name}/{item.name}")
        else:
            print(f"[DRY RUN]: {item.name} ----> {clean_name}/{item.name}")
            game_destination_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(item,destination_file)

        