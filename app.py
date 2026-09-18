from flask import Flask, render_template
from datetime import datetime
import os
# 使用中国东八区
from zoneinfo import ZoneInfo

app = Flask(__name__)

# 直接写北京时间 2026‑09‑22 00:00:00
TARGET_TIME = datetime(2026, 9, 22, 0, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))

@app.route("/")
def index():
    now = datetime.now(tz=ZoneInfo("Asia/Shanghai"))
    if now < TARGET_TIME:
        remain = TARGET_TIME - now
        return render_template("wait.html", remain=remain)
    else:
        return render_template("main.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
