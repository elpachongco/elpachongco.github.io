from pathlib import Path
import shutil

base = Path("./").resolve()
files = base.glob("**/*")
files = [x for x in files if x.is_file()]

for file in files:
    b = base / file.stem / "img"
    b.mkdir(parents=True, exist_ok=True)
    shutil.copy(str(file), str(base/file.stem/"index.md"))
