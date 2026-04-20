# 📰 News App

A lightweight and efficient Python-based news search application that brings the latest headlines and detailed news articles directly to your terminal. Powered by the **News API**, this tool allows you to stay informed on any topic you are interested in with just a single query.

---

## ✨ Features

- **🔍 Topic-Based Search**: Instantly fetch news articles on any keyword or topic.
- **📰 Quick Summaries**: View the top 5 most relevant articles with titles and brief descriptions.
- **🔗 Direct Links**: Get direct URLs to the full articles for in-depth reading.
- **⚡ Fast & Simple**: Minimalistic interface designed for speed and ease of use.
- **🛠️ Clean Architecture**: Organized project structure for easy maintenance and expansion.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+**: Make sure you have Python installed. You can check by running `python --version`.
- **API Key**: You'll need an API key from [NewsAPI.org](https://newsapi.org/).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Vignesh-Salian/news-app-python.git
   cd news-app-python/News\ App\ using\ APIs/news-app-1
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Create a `.env` file in the project root directory and add your API key. You can copy the provided `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and insert your actual key:
   ```env
   NEWS_API_KEY="YOUR_NEWS_API_KEY_HERE"
   ```

---

## 💻 Usage

Run the application using the following command:

```bash
python src/main.py
```

**Example Interaction:**
```text
What type of news are you interested in today: artificial intelligence

Top news for 'artificial intelligence':

1. The Future of AI in 2024
Description: A deep dive into how AI is shaping our world...
Read more: https://example.com/ai-future

------------------------------------------------------------
```

---

## 🛠️ Technologies Used

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Requests-Library-2CA5E0?style=for-the-badge" alt="Requests" />
  <img src="https://img.shields.io/badge/News_API-Data-black?style=for-the-badge" alt="News API" />
</p>

- **Python**: Core logic and scripting.
- **Requests Library**: For making HTTP requests to the News API.
- **News API**: The source for global news data.

---


## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

<p align="left">
  <a href="https://github.com/Vignesh-Salian">
    <img src="https://img.shields.io/badge/VIGNESH%20SALIAN-DEVELOPER-0078D4?style=for-the-badge&logo=github&logoColor=white" alt="Vignesh Salian" />
  </a>
  <a href="https://github.com/Vignesh-Salian">
    <img src="https://img.shields.io/github/followers/Vignesh-Salian?label=Follow&style=for-the-badge&logo=github" alt="Follow Vignesh Salian" />
  </a>
</p>
