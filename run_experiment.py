import argparse, json
from src.utils.config import load_config

def run_experiment(config_file, dry_run=False):
    config = load_config(config_file)
    print("Loaded config:")
    print(json.dumps(config, indent=2))
    if dry_run:
        print("Dry run successful! (no training executed)")
    else:
        print("Training loop not yet implemented")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_experiment(args.config, dry_run=args.dry_run)
