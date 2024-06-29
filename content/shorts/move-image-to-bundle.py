# Migrate images from 'assets' to page bundle
# Note: Change paths from markdown files
# Gatchas: 1. assumes image are in one line
from pathlib import Path
import shutil

base = Path("./").resolve()
bundle_dirs = base.glob("*")
bundle_dirs = [x for x in bundle_dirs if x.is_dir()]

for bundle in bundle_dirs:
    content = bundle / "index.md"
    with open(str(content.resolve()), "r") as index_file:
        for line in index_file:
            img_addr_idx = line.find("img/uploads/")
            if img_addr_idx < 0:
                continue
            img_addr = ""
            for char in line[img_addr_idx + len("img/uploads/"):]:
                if char in [" ", ")"]:
                    break
                img_addr += char
            if not img_addr:
                continue
            img_path = base / "../../assets/img/uploads" / img_addr
            dest = bundle / "img"
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy(img_path, dest / img_addr)
