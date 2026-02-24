import json
import os

WRISTBAND_FILE = os.path.join(os.path.dirname(__file__), "wristbands.json")

def load_wristbands():
    """Load the list of currently taken wristband numbers from file."""
    if os.path.exists(WRISTBAND_FILE):
        with open(WRISTBAND_FILE, "r") as f:
            return json.load(f)
    return []

def save_wristbands(data):
    """Save the list of currently taken wristband numbers to file."""
    with open(WRISTBAND_FILE, "w") as f:
        json.dump(data, f)
