# 🌐 Website Availability Checker

A **Streamlit-based** web application to check whether a list of websites is reachable (HTTP 200 OK).  
This tool allows you to add multiple URLs, format them automatically, and check their availability concurrently using Python’s `ThreadPoolExecutor`.

---

## 🚀 Features
- ✅ Check if websites return a successful HTTP 200 status.
- 🌍 Automatically formats user-entered URLs.
- ⚡ Concurrently checks multiple sites using threads.
- 🖥️ Simple and interactive UI built with Streamlit.
- 🔄 Add, clear, and re-check URLs dynamically.

---

## 📂 Project Structure
```
site-connectivity-check/
│── src/
│   └── app.py          # Main Streamlit application
│── requirements.txt    # Python dependencies
│── LICENSE             # License file
└── README.md           # Project documentation
```

---

## 🛠 Requirements

Dependencies are listed in `requirements.txt`.  
Install them with:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/site-connectivity-check.git
cd site-connectivity-check/src
```

### 2. Run the Streamlit app
```bash
streamlit run app.py
```

### 3. Use the Application
- Enter a website URL (e.g., `google.com`)
- Click **"Add URL"**
- Click **"Check All"** to check availability
- ✅ Green check = reachable / ❌ Red cross = unreachable

---

## 🧩 How It Works
1. **URL Formatting** – Removes `http(s)://` and `www.` prefixes, then adds `https://www.` for consistency.  
2. **Availability Check** – Sends an HTTP GET request with a custom `User-Agent`.  
3. **Concurrency** – Uses Python’s `ThreadPoolExecutor` to check multiple URLs in parallel.  
4. **Interactive UI** – Built using Streamlit for real-time feedback.

---

## ✅ Example Output

| URL                    | Status |
|------------------------|--------|
| https://www.google.com | ✅ |
| https://www.invalid.xyz| ❌ |

---

## 📄 License
This project is licensed under the [MIT License](../LICENSE).

---

## 👨‍💻 Author
**Mahdi Ghasemi**  
📧 Email: mahdi.ghasemi.dev@gmail.com  
🌐 GitHub: [Mahdi Ghasemi](https://github.com/MahdiGhasemidev)  

---

### ⭐ If you find this project useful, give it a star!
