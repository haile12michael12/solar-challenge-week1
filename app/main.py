import streamlit as st
import pandas as pd
import altair as alt
from utils import load_data, get_top_regions

# Load data
@st.cache
def load_data():
    data = pd.read_csv('data/benin_clean.csv')  # Adjust for other countries as needed
    return data

# Main app function
def main():
    st.title("Solar Data Insights Dashboard")

    # Country selection
    country = st.selectbox("Select Country", ["Benin", "Country2", "Country3"])  # Add more countries
    df = load_data()

    # Filter data based on selected country
    df_country = df[df['Country'] == country]

    # Boxplot of GHI
    st.subheader("GHI Boxplot")
    boxplot = alt.Chart(df_country).mark_boxplot().encode(
        x='GHI',
        y='Country',
    )
    st.altair_chart(boxplot, use_container_width=True)

    # Top regions table
    st.subheader("Top Regions by GHI")
    top_regions = get_top_regions(df_country)
    st.write(top_regions)

if __name__ == "__main__":
    main()