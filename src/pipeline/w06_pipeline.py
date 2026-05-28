# W06 - Pipeline modular
from pathlib import Path
import duckdb

def run_pipeline(db_path: Path, raw_csv: Path):
    con = duckdb.connect(str(db_path))
    # TODO: agregar lógica del pipeline
    con.close()
    return True

if __name__ == "__main__":
    print("Pipeline W06 ejecutado")
