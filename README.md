
---

# 🌍 Full Page Web Scraper → Excel

A simple **Flask-based web application** that scrapes **all visible text** from any public webpage and saves it as an **Excel file (.xlsx)**.

No CSS selectors or coding required — just enter a URL, click **Scrape Entire Page**, and download the results.

---

## 🚀 Features

* 🧾 **Scrapes all visible text** — automatically removes scripts, styles, and hidden tags
* 💾 **Exports results to Excel (.xlsx)** — clean, one-line-per-row format
* 🌐 **Web-based UI** — simple, responsive, built with TailwindCSS
* 🕵️ **Respects `robots.txt`** — checks if scraping is allowed before proceeding
* 🌀 **Loading spinner** — shows progress while scraping
* ⚙️ **Lightweight & local** — runs entirely on your machine

---

## 🗂️ Project Structure
here is a picture of the structure how should it look

![WhatsApp Image 2025-10-26 at 22 19 55_e04a8202](https://github.com/user-attachments/assets/03cf72b1-b1f5-47f6-aa5d-a1b160920701)

```
web_scraper_app/
│
├── app.py               # Flask backend (routes + file saving)
├── scraper.py           # Scraping logic (requests + BeautifulSoup)
├── templates/
│   └── index.html       # Frontend (UI with Tailwind + JS)
└── README.md            # Documentation (this file)
```


---

## 🧰 Requirements

* Python **3.8+**
* pip (Python package installer)

### 📦 Python libraries used

| Library                   | Purpose                      |
| ------------------------- | ---------------------------- |
| `Flask`                   | Web server and routing       |
| `requests`                | Fetching HTML from URLs      |
| `beautifulsoup4` + `lxml` | Parsing and cleaning HTML    |
| `openpyxl`                | Creating Excel files (.xlsx) |

---

## ⚙️ Installation

1. **Clone or download** this repository:

   ```bash
   git clone https://github.com/yourusername/web-scraper-excel.git
   cd web-scraper-excel
   ```

2. **Install dependencies:**

   ```bash
   pip install flask requests beautifulsoup4 lxml openpyxl
   ```

3. **Run the Flask app:**

   ```bash
   python app.py
   ```

4. **Open your browser:**

   Go to 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥️ How to Use

1. Enter a webpage URL (e.g. `https://quotes.toscrape.com/`)
2. Click **Scrape Entire Page**
3. Wait for the 🌀 spinner to finish
4. When scraping is complete, a **download link** for the Excel file appears
5. Click it to save your file locally

---

## 📊 Output Example

If you scrape `https://example.com/`, your Excel file (`scraped_page_20251026_184455.xlsx`) will look like this:

| Visible Text                                                                               |
| ------------------------------------------------------------------------------------------ |
| Example Domain                                                                             |
| This domain is for use in illustrative examples in documents.                              |
| You may use this domain in literature without prior coordination or asking for permission. |
| More information...                                                                        |

---

## 🌐 Test URLs (safe to scrape)

You can test your scraper using these public demo sites:

| Site             | URL                                                                                      | Description                      |
| ---------------- | ---------------------------------------------------------------------------------------- | -------------------------------- |
| Example.com      | [https://example.com](https://example.com)                                               | Simple static page               |
| Quotes to Scrape | [https://quotes.toscrape.com](https://quotes.toscrape.com)                               | Demo site for scraping tutorials |
| Books to Scrape  | [https://books.toscrape.com](https://books.toscrape.com)                                 | Sample e-commerce site           |
| Wikipedia        | [https://en.wikipedia.org/wiki/Web_scraping](https://en.wikipedia.org/wiki/Web_scraping) | Informational page               |

---

## ⚙️ How It Works (Under the Hood)

1. **User submits URL** via the web form.
2. Flask receives it at `/scrape`.
3. The backend:

   * Checks if the site allows scraping (via `robots.txt`)
   * Fetches the HTML using `requests`
   * Parses it with `BeautifulSoup`
   * Removes non-visible content (scripts, styles, comments)
   * Extracts all readable text lines
4. The text is written to an **Excel file** using `openpyxl`.
5. Flask sends a success message + download link back to the UI.

---

## 💡 Technical Details

* **Frontend:** TailwindCSS + vanilla JavaScript
* **Backend:** Flask REST API
* **Excel engine:** openpyxl
* **Scraping logic:** BeautifulSoup (`lxml` parser)
* **Output format:** One visible text line per Excel row

---

## 🌀 Loading Indicator

When you click **Scrape Entire Page**:

* The button text changes to *“Scraping…”*
* A white loading spinner appears next to it
* The button is temporarily disabled
  Once scraping finishes, the spinner hides and a download link appears.

---

## 🧠 Good to Know

* This scraper fetches **only visible text** (ignores `<script>`, `<style>`, and hidden elements).
* It does **not** execute JavaScript — so dynamic content won’t appear.
* For JS-heavy sites (like React apps), use **Selenium** or **Playwright** instead.
* Always respect website **Terms of Service** and **robots.txt** rules.

---

## 🧾 Example Output Files

| Filename                            | Created On | Description               |
| ----------------------------------- | ---------- | ------------------------- |
| `scraped_page_20251026_184455.xlsx` | 2025-10-26 | Example.com text          |
| `scraped_page_20251026_191210.xlsx` | 2025-10-26 | Quotes to Scrape homepage |

---

## 🔒 Ethical & Legal Notes

✅ Allowed:

* Testing on demo or open sites (e.g., *quotes.toscrape.com*)
* Scraping your own websites
* Educational or personal learning use

🚫 Not Allowed:

* Scraping sites that disallow it in `robots.txt`
* Collecting personal, copyrighted, or private data
* Excessive request frequency that harms servers

---

## 🧑‍💻 Author

**Your Name**
📧 [your.email@example.com](mailto:your.email@example.com)
💼 GitHub: [@yourusername](https://github.com/yourusername)

---

## 🪪 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
You’re free to use, modify, and distribute it — please credit the original author.

---

## 🏁 Future Enhancements

* [ ] Add **page title and URL** headers to the Excel output
* [ ] Option to **include all hyperlinks** on the page
* [ ] Display **preview of extracted text** before download
* [ ] Support **multi-page scraping** with progress bar

---

Would you like me to include a **section with screenshots** (UI + Excel output preview) in the README next?
I can generate sample images to make your documentation look professional.
