import streamlit as st
import pandas as pd
import plotly.express as px

# Load your final CSV
df = pd.read_csv(r"final_data.csv")

st.set_page_config(page_title="Industry Sentiment Dashboard", layout="wide")
st.title("📊 Industry Sentiment Dashboard")
st.markdown("""
This dashboard visualizes how media sentiment and company reputation vary across different industry categories.  
""")

# Unified card function
def unified_card(label, color, key):
    st.markdown(f"""
        <style>
            div[data-testid="stCheckbox"] > label[data-testid="stMarkdownContainer"] {{
                background-color: {color};
                padding: 18px;
                border-radius: 12px;
                display: block;
                font-size: 16px;
                font-weight: 600;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 15px;
            }}
            div[data-testid="stCheckbox"] {{
                margin-bottom: -15px;
            }}
        </style>
    """, unsafe_allow_html=True)
    return st.checkbox(label, key=key)


# Preview Toggle Card
show_table = st.checkbox("📊 Show Overall Stats & Snapshot")

if show_table:
    st.sidebar.header("🔍 Filters")
    selected_category = st.sidebar.multiselect(
        "Select Sentiment Categories",
        options=df["sentiment_category"].unique(),
        default=df["sentiment_category"].unique(),
        key="overall_filter"
    )

    # Filter data
    filtered_df = df[df["sentiment_category"].isin(selected_category)]

    # Show preview
    st.subheader("🧾 Filtered Data Snapshot")
    st.dataframe(filtered_df)

    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Industries", len(filtered_df))
    col2.metric("Avg Company Rating", round(filtered_df['avg_rating'].mean(), 2))
    col3.metric("Avg News Sentiment", round(filtered_df['avg_sentiment'].mean(), 3))
    col4.metric("Total Articles", int(filtered_df['article_count'].sum()))


# ------------------- BAR CHART -------------------
if unified_card("📊 Show Bar Chart: Avg Rating vs Sentiment", "#e0f2ff", "bar_chart"):
    selected_bar = st.sidebar.multiselect(
        "🎯 Select Industries for Bar Chart",
        options=df['sentiment_category'].unique(),
        default=df['sentiment_category'].unique(),
        key="bar_filter"
    )
    bar_df = df[df['sentiment_category'].isin(selected_bar)].copy()
    bar_df['normalized_rating'] = (bar_df['avg_rating'] - 3.5) / 0.5 * 0.5

    fig1 = px.bar(
        bar_df.melt(id_vars='sentiment_category', value_vars=['normalized_rating', 'avg_sentiment']),
        x='sentiment_category', y='value', color='variable',
        barmode='group', title="Consumer vs Media Perception Across Industries"
    )
    st.plotly_chart(fig1, use_container_width=True)
    with st.expander("📌 Insight"):
        st.markdown("""
        #### 📊 Insight: Avg Rating vs Media Sentiment

        - Consumer and media sentiment don’t always align, **Business and Science have high ratings but low sentiment**.
        - **Education stands out** with highest sentiment but lowest customer rating, a classic **perception vs reality gap**.
        - **Tech is under fire**, both sentiment and ratings are below average, hinting at trust issues.
        - **Normalized scale** helps expose subtle but meaningful perception mismatches across sectors.
        - This chart highlights **which sectors need better media relations vs operational improvements**.
        """)

# ------------------- PIE CHART -------------------
if unified_card("🧩 Show Pie Chart: Media Article Distribution", "#eaffea", "pie_chart"):
    selected_pie = st.sidebar.multiselect(
        "🎯 Select Industries for Pie Chart",
        options=df['sentiment_category'].unique(),
        default=df['sentiment_category'].unique(),
        key="pie_filter"
    )
    pie_df = df[df['sentiment_category'].isin(selected_pie)]

    fig2 = px.pie(
        pie_df, values='article_count', names='sentiment_category',
        title='Share of Media Coverage by Industry',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig2, use_container_width=True)
    with st.expander("📌 Insight"):
        st.markdown("""
        #### 🧩 Insight: Media Article Distribution by Industry

        - **Over 50%** of media coverage is concentrated on Business, showing it’s the **most visible and scrutinized** sector.
        - **Science and Tech receive similar attention**, yet have different sentiment and rating dynamics.
        - **Education gets the least media attention** despite having the most positive sentiment.
        - Indicates **media priorities may not reflect public satisfaction**.
        - Helps identify **which industries are overexposed vs underrepresented** in the media narrative.

        """)

# ------------------- LINE CHART -------------------
if unified_card("📈 Show Line Chart: Weighted Index vs Rating", "#fffbdc", "line_chart"):
    selected_line = st.sidebar.multiselect(
        "🎯 Select Industries for Line Chart",
        options=df['sentiment_category'].unique(),
        default=df['sentiment_category'].unique(),
        key="line_filter"
    )
    line_df = df[df['sentiment_category'].isin(selected_line)]

    fig3 = px.line(
        line_df, x='sentiment_category', y=['weighted_index', 'avg_rating'],
        markers=True, title='Weighted Sentiment vs Company Rating'
    )
    st.plotly_chart(fig3, use_container_width=True)
    with st.expander("📌 Insight"):
        st.markdown("""
        #### 📈 Insight: Weighted Sentiment vs Company Rating

        - **Business has the highest weighted sentiment**, due to sheer article volume, not necessarily positivity.
        - **Tech shows low influence and mid-level trust**, could be due to PR neglect or controversy.
        - **Education’s rating remains lowest despite a rise in weighted sentiment**, suggesting media praise isn’t converting to public approval.
        - **Science shows balance**, moderate rating, decent sentiment, consistent coverage.
        - Weighted sentiment gives a **nuanced view of media power and public perception combined**.
        """)

# ------------------- BUBBLE CHART -------------------
if unified_card("🔵 Show Bubble Chart: Sentiment vs Rating", "#ffe0e0", "bubble_chart"):
    selected_bubble = st.sidebar.multiselect(
        "🎯 Select Industries for Bubble Chart",
        options=df['sentiment_category'].unique(),
        default=df['sentiment_category'].unique(),
        key="bubble_filter"
    )
    bubble_df = df[df['sentiment_category'].isin(selected_bubble)]

    fig4 = px.scatter(
        bubble_df, x='avg_sentiment', y='avg_rating', size='article_count',
        color='sentiment_category', hover_name='sentiment_category',
        title='Sentiment vs Rating with Media Volume'
    )
    st.plotly_chart(fig4, use_container_width=True)
    with st.expander("📌 Insight"):
        st.markdown("""
        #### 🔵 Insight: Sentiment vs Rating with Media Volume

        - **Bubble size adds depth**, Business has the largest media footprint and highest user approval.
        - **Education floats high on sentiment**, but user rating is lowest, **disconnect warning**.
        - **Tech is small, low, and quiet**, indicating it may be **ignored or distrusted** right now.
        - **Science appears balanced** with decent sentiment, rating, and media coverage.
        - Best industries to watch are in the **top-right quadrant**, high rating, high sentiment, high exposure.
        """)

# ------------------- Footer -------------------
st.markdown("---")
st.markdown("""
            📍 **Developed by Vivek Joshi** \n
            _Powered by Streamlit & Plotly_ \n
            _**Data Source:** Curated from company reviews and news articles with VADER sentiment analysis_ \n
            __[Github Link]__
            """)
