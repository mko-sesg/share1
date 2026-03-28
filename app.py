from flask import Flask, jsonify, send_from_directory
import sqlite3
from pathlib import Path

app = Flask(__name__, static_folder=".")
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "shop.db"

@app.route("/")
def index():
 return send_from_directory(".", "index.html")

@app.route("/js/<path:filename>")
def js_files(filename):
 return send_from_directory("js", filename)

@app.route("/css/<path:filename>")
def css_files(filename):
 return send_from_directory("css", filename)

@app.route("/api/products")
def get_products():
 conn = sqlite3.connect(DB_PATH)
 conn.row_factory = sqlite3.Row
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM product")
 rows = [dict(row) for row in cursor.fetchall()]
 conn.close()
 return jsonify(rows)
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=3000, debug=True)