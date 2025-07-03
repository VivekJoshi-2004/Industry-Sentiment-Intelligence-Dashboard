# 📊 Industry Sentiment Intelligence Dashboard

An interactive Streamlit dashboard that analyzes and visualizes **public perception vs media sentiment** across industries using real-world company reviews and news articles.

> Built with 💡 critical thinking, data storytelling, and clean UI.

---

## 🚀 Live Demo

🔗 [Click here to try the live app]((https://industry-sentiment-intelligence-dashboard.streamlit.app/))  


---

## 📁 Project Structure

├── app.py # Main Streamlit app
├── final_data.csv # Cleaned and aggregated dataset
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 📊 Features

- 📌 **Filter & Explore** sentiment data across TECH, BUSINESS, SCIENCE, and EDUCATION
- 📉 **Bar, Line, Pie & Bubble charts** to compare:
  - Customer Ratings
  - Media Sentiment
  - Media Volume (Weighted Index)
- 🎯 **Detailed insights** per chart for storytelling and data interpretation
- 📦 Clean UI with collapsible visual cards and expander-based insights

---

## 🧠 What Makes This Special?

- ✅ **Weighted Sentiment Index** combining media volume × tone
- ✅ Normalization for fair cross-metric comparison
- ✅ Consumer vs media mismatch detection
- ✅ Emphasis on **critical thinking** and presentation — not just visuals

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/sentiment-dashboard.git
cd sentiment-dashboard

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

📡 Deployment
This app is deployed on Streamlit Cloud:

- Push to GitHub.
- Go to streamlit.io/cloud
- Connect your repo and deploy app.py.

📌 Dataset Overview
news_sentiment.csv: VADER sentiment analysis of articles mapped to industries

Final CSV created by aggregating and labeling all metrics for analysis

📈 Sample Visuals
![image](https://github.com/user-attachments/assets/568eea1d-efef-4444-9862-62d199327317)

Chart	Description
📊 Bar Chart	Compare Avg Rating vs Sentiment
![image](https://github.com/user-attachments/assets/49b51176-f9eb-47a0-b70d-41c14345e2a7)

🧩 Pie Chart	Media Coverage Distribution
![image](https://github.com/user-attachments/assets/667a2810-da58-4071-b56b-fec78ce85c09)

📈 Line Chart	Weighted Sentiment Index vs Rating
![image](https://github.com/user-attachments/assets/aab3395b-dcdc-4b0d-a4a1-5eaa38f2b7c9)

🔵 Bubble Chart	Sentiment vs Rating with Media Volume
![image](https://github.com/user-attachments/assets/a8f42964-f1d1-40ac-9134-a5a31f9e7c1e)


👨‍💻 Author
Vivek Joshi

🧠 Passionate about using AI, data & automation to solve real-world problems

⭐ Star this Repo
If you found this useful or impressive, consider giving it a ⭐ on GitHub!
