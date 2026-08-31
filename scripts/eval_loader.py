from pathlib import Path
import json

def load_evals(root: Path):
    eval_dir = root / "evals"
    index = json.loads((eval_dir / "index.json").read_text(encoding="utf-8"))
    items=[]
    for meta in index["categories"].values():
        doc=json.loads((eval_dir / meta["file"]).read_text(encoding="utf-8"))
        items.extend(doc["evals"])
    return {"version": index["version"], "count": index["count"], "synthetic_data_only": index["synthetic_data_only"], "evals": items}
