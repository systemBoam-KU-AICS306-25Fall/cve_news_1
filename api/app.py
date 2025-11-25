from flask import Flask, jsonify
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "news_pipeline"))

from news_pipeline.build_pipeline import build_news_pipeline

app = Flask(__name__)

@app.route("/api/cve-news", methods=["GET"])
def get_cve_news():
    data = build_news_pipeline()
    data = [item for item in data if len(item["cves"]) > 0]

    return jsonify({
        "count": len(data),
        "news": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5566, debug=True)
