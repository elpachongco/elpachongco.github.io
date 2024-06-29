from pathlib import Path

a = Path(".")
files = [x for x in a.glob("**/*") if x.is_file()]

for file in files:
    p = a / file.name / "index..md"
    p.mkdir(exist_ok=True, parents=True)
    breakpoint()
