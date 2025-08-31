from pathlib import Path
from typing import Dict, Any
import yaml

def load_script(path: str) -> Dict[str, Any]:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert "segments" in data, "YAML must include a 'segments' list"
    return data

def safe_filename(text: str) -> str:
    bad = '<>:"/\\|?*'
    for ch in bad:
        text = text.replace(ch, "")
    return "_".join(text.strip().split())[:64]