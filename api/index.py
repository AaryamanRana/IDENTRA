import sys
from pathlib import Path

# Add root directory to sys.path so core, ui, and modules are importable
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from ui.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
