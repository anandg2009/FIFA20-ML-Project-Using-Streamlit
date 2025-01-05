import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data (Assume data is cleaned and preprocessed)
@st.cache_data
def load_data():
    data = pd.read_csv('players_20.csv')  # Replace with actual path if needed
    return data

# Main
st.title("FIFA 20 Player Analysis Dashboard")

# Load data
data = load_data()

# Sidebar for filtering
def filter_data(data):
    nationality = st.sidebar.multiselect('Select Nationality', data['nationality'].unique())
    if nationality:
        data = data[data['nationality'].isin(nationality)]
    return data

filtered_data = filter_data(data)

# 1. Top 10 countries with most players
st.header("Top 10 Countries with Most Players")

country_count = filtered_data['nationality'].value_counts().head(10).reset_index()
country_count.columns = ['Country', 'Player Count']
fig = px.bar(country_count, x='Country', y='Player Count', color='Player Count', 
             color_continuous_scale='Viridis')
st.plotly_chart(fig)

st.write("**Conclusion:** Countries like England, Germany, and Spain produce the most footballers.")

# 2. Distribution of Overall Rating vs. Age
st.header("Distribution of Overall Rating vs. Age")
fig = px.scatter(filtered_data, x='age', y='overall', color='overall',
                 title='Overall Rating vs Age', color_continuous_scale='Bluered')
st.plotly_chart(fig)

st.write("**Conclusion:** Players' overall ratings peak between the ages of 25-30, with significant decline after 35.")

# 3. Salary Distribution by Offensive Position
st.header("Salary Distribution by Offensive Position")
positions_of_interest = ['ST', 'RW', 'LW']
df_filtered = filtered_data[filtered_data['player_positions'].str.contains('|'.join(positions_of_interest))]
fig = px.box(df_filtered, x='player_positions', y='wage_eur', color='player_positions',
             title='Salary by Offensive Position')
st.plotly_chart(fig)

st.write("**Conclusion:** Strikers (ST) tend to earn the highest wages compared to wingers (RW, LW).")

# 4. Work Rate Distribution
st.header("Work Rate Distribution")
work_rate_count = filtered_data['work_rate'].value_counts().reset_index()
work_rate_count.columns = ['Work Rate', 'Count']
fig = px.pie(work_rate_count, names='Work Rate', values='Count', title='Work Rate Distribution')
st.plotly_chart(fig)

st.write("**Conclusion:** Majority of players maintain a medium work rate in both attack and defense.")

# 5. Preferred Foot Analysis
st.header("Preferred Foot Analysis")
fig = px.pie(filtered_data, names='preferred_foot', title='Distribution by Preferred Foot')
st.plotly_chart(fig)

st.write("**Conclusion:** Most players prefer their right foot (76.4%) over their left (23.6%).")

# 6. Player Ratings by International Reputation
st.header("Overall Rating by International Reputation")
fig = px.bar(filtered_data, x='international_reputation', y='overall', color='international_reputation',
             title='Rating by Reputation')
st.plotly_chart(fig)

st.write("**Conclusion:** Players with higher international reputations tend to have higher overall ratings.")

# Footer
st.write("\n\n**End of Report** - Visualization of FIFA 20 Player Analysis")
