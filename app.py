import json
import os
from pathlib import Path

from flask import Flask, request

app = Flask(__name__)

BASE_PATH = Path(os.getenv("OUTDIR", "."))


@app.route("/<path>", methods=["POST"])
def post_bin(path):
    path = (BASE_PATH / path).with_suffix(".json")

    with path.open("w") as opened_path:
        json.dump(request.json, opened_path)
    return "ok"


@app.route("/<path>", methods=["GET"])
def get_bin(path):
    path = (BASE_PATH / path).with_suffix(".json")

    if not path.exists() or not path.is_file():
        return "Not found", 404

    with path.open("r") as opened_path:
        return opened_path.read()
