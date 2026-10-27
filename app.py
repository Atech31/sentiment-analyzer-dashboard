import streamlit as st
import pandas as pd
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer Dashboard", page_icon="", layout="wide")

st.title("Real-Time News & Social Media Sentiment Analyzer")
st.markdown("Analyze public sentiment, polarity scores, and category breakdowns using Python & NLP.")

# Sample Social Media / News Data
data = [
    {"source": "Twitter", "category": "Tech", "text": "Excited to test out the new AI models! They are lightning fast and super accurate. Absolutely love it!", "date": "2026-06-01"},
    {"source": "News API", "category": "Economy", "text": "Market drops significantly as inflation concerns rise amid global supply chain disruptions.", "date": "2026-06-01"},
    {"source": "Reddit", "category": "Tech", "text": "The latest software update broke my workflow completely. Very frustrating experience.", "date": "2026-06-02"},
    {"source": "Twitter", "category": "Sports", "text": "What a stunning match last night! Historic victory for the team under extreme pressure.", "date": "2026-06-02"},
    {"source": "News API", "category": "Economy", "text": "Tech stocks surge to an all-time high following strong quarterly earnings reports.", "date": "2026-06-03"},
    {"source": "Reddit", "category": "Entertainment", "text": "The movie was utterly boring and a total waste of time and money. Do not watch.", "date": "2026-06-03"},
]

df = pd.DataFrame(data)

# Function to calculate sentiment polarity using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    # Polarity ranges from -1 (Negative) to 1 (Positive)
    if analysis.sentiment.polarity > 0.1:
        return "Positive 😊"
    elif analysis.sentiment.polarity < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def get_polarity_score(text):
    return round(TextBlob(text).sentiment.polarity, 2)

# Apply sentiment analysis on dataset
df['Sentiment'] = df['text'].apply(get_sentiment)
df['Polarity_Score'] = df['text'].apply(get_polarity_score)

# Sidebar filters
st.sidebar.header("Filter Options")
selected_source = st.sidebar.selectbox("Select Platform / Source", ["All"] + list(df['source'].unique()))
selected_category = st.sidebar.selectbox("Select Category", ["All"] + list(df['category'].unique()))

# Filter logic
filtered_df = df.copy()
if selected_source != "All":
    filtered_df = filtered_df[filtered_df['source'] == selected_source]
if selected_category != "All":
    filtered_df = filtered_df[filtered_df['category'] == selected_category]

# Dashboard Layout
tab1, tab2 = st.tabs(["💬 Sentiment Feed & Analysis", "📈 Analytics & Summary"])

with tab1:
    st.subheader("Live Feed Sentiment Breakdown")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Interactive custom text sentiment tester
    st.markdown("---")
    st.subheader("Test Custom Headline / Tweet")
    user_input = st.text_input("Enter any text or news headline to analyze its sentiment:")
    if user_input:
        res = get_sentiment(user_input)
        score = get_polarity_score(user_input)
        st.success(f"**Sentiment Result:** {res} (Polarity Score: {score})")

with tab2:
    st.subheader("Overall Sentiment Distribution")
    sentiment_counts = filtered_df['Sentiment'].value_counts()
    st.bar_chart(sentiment_counts)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records Analyzed", len(filtered_df))
    col2.metric("Positive Posts", len(filtered_df[filtered_df['Sentiment'] == "Positive 😊"]))
    col3.metric("Negative Posts", len(filtered_df[filtered_df['Sentiment'] == "Negative 😞"]))
