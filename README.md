# 📸 TG Foto Delivery Bot

A **Telegram bot built with Python & Aiogram 3.x** that automatically receives images, applies a **watermark**, and sends them back to the user.  
Created for fast image processin and clean architecture.

---

## 🚀 Features

- 📥 Receive images directly from Telegram users  
- 🖋️ Add watermark with **Pillow (PIL)**  
- ⚡ Instant image return to the user  
- ⚙️ Configurable via `.env` file  
- 🧱 Docker-ready deployment  

---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Python 3.12+** | Programming language |
| **Aiogram 3.x** | Asynchronous Telegram bot framework |
| **Pillow (PIL)** | Image manipulation and watermarking |
| **FastAPI** | Health endpoints |
| **Docker** | Containerized environment |

---

## 🗂️ Project Structure

```
tg-foto-delivery/
├── Main.py                # Entry point for bot startup
├── Marker.py              # Image watermark logic (Pillow)
├── handlers/              # Telegram update handlers
│   ├── __init__.py
│   └── photo_handler.py
├── requirements.txt       # Project dependencies
├── .gitignore
├── Dockerfile
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/tg-foto-delivery.git
cd tg-foto-delivery
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` File
Copy `.env.example` to `.env` and update the values:

```
BOT_TOKEN=your_telegram_bot_token
```

---

## ▶️ Usage

Run the bot locally:

```bash
python Main.py
```

Then open Telegram and send any photo to your bot — it will automatically respond with a watermarked version.

---

## 🐳 Docker Deployment

### Build the Docker Image
```bash
docker build -t tg-foto-delivery .
```

### Run the Container
```bash
docker run -d --name tg-foto-delivery --env-file .env tg-foto-delivery
```

### Stop the Container
```bash
docker stop tg-foto-delivery
```

---

## 🧑‍💻 Author

**Renars Masaļskis**  
🎓 Riga Technical University — Computer Systems  
🌍 [GitHub Profile](https://github.com/rek1ngs)  
💬 Passionate about **DevOps, Cloud, and Python development**

---

## 🌟 Support

If you find this project useful, please give it a ⭐ on GitHub!  
It helps others discover it and motivates further development.

---
