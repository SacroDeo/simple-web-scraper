# app.py
from flask import Flask, render_template, request, jsonify, send_file
from scraper import scrape_entire_page
from openpyxl import Workbook
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def do_scrape():
    url = request.form.get('url')

    if not url:
        return jsonify({"error": "Please provide a URL."})

    data = scrape_entire_page(url)

    if "error" in data:
        return jsonify(data)

    # Save results to Excel
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scraped_page_{timestamp}.xlsx"
    filepath = os.path.join(os.getcwd(), filename)

    wb = Workbook()
    ws = wb.active
    ws.title = "Page Text"
    ws.append(["Visible Text"])

    for line in data["results"]:
        ws.append([line])

    wb.save(filepath)

    return jsonify({
        "message": f"Scraping successful. Saved as {filename}.",
        "file": filename
    })

@app.route('/download/<filename>')
def download(filename):
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return jsonify({"error": "File not found."})

if __name__ == '__main__':
    app.run(debug=True)
