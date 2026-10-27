#   Real-Time News & Social Media Sentiment Analyzer Dashboard

A fully interactive web application built with **Python**, **Streamlit**, and **Natural Language Processing (NLP)** to analyze public sentiment, polarity scores, and category breakdowns across multiple digital platforms in real-time.

[![Live App Status](https://img.shields.io/badge/Streamlit-Live-brightgreen?style=for-the-badge&logo=streamlit)](https://setimentanalyzer.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)

---

##   Live Demo
Check out the live application here: **[setimentanalyzer.streamlit.app](https://setimentanalyzer.streamlit.app/)**

---

##   Key Features
* **Multi-Platform Feed Analysis:** Aggregate and filter posts/headlines from sources like Twitter, News API, and Reddit.
* **NLP Sentiment Classification:** Uses **TextBlob** to compute semantic polarity and categorize text into **Positive 😊**, **Negative 😞**, or **Neutral 😐**.
* **Interactive Custom Text Tester:** Allows users to input any custom news headline, tweet, or review to instantly analyze its sentiment and numerical polarity score in real-time.
* **Dynamic Analytics & Visualizations:** Interactive bar charts and metrics tracking total record volume and sentiment breakdowns filtered by platform or category.

---

##   Tech Stack
* **Frontend & UI:** Streamlit (Python-based web framework)
* **Data Manipulation:** Pandas
* **Natural Language Processing (NLP):** TextBlob (Lexicon-based sentiment scoring)
* **Hosting & Deployment:** Streamlit Community Cloud

---

##   Project Structure
```text
sentiment-analyzer-dashboard/
│
├── app.py              # Main Streamlit application script
├── requirements.txt    # Python package dependencies
└── README.md           # Project documentation
