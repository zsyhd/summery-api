#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify

app = Flask(__name__)
port = 3000

# داده‌های بخش Summary داشبورد
dashboard_summary = {
    "TotalEvents": 123,
    "Anomalies": 45,             # درصد آنومالی‌ها به صورت عدد
    "AveragePressure": 78.9,     # میانگین فشار
    "AverageTemperature": 65.4   # میانگین دما
}

# API برای summary
@app.route("/api/summary", methods=["GET"])
def get_summary():
    return jsonify(dashboard_summary)

if __name__ == "__main__":   # ✅ اینجا درست شد
    print(f"API running at http://localhost:{port}")
    app.run(port=port)

