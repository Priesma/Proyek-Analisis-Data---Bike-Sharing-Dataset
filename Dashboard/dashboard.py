import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define dataset URLs
day_url = "https://raw.githubusercontent.com/Priesma/Proyek-Analisis-Data---Bike-Sharing-Dataset/refs/heads/main/day.csv"
hour_url = "https://raw.githubusercontent.com/Priesma/Proyek-Analisis-Data---Bike-Sharing-Dataset/refs/heads/main/hour.csv"

# Load datasets
day_data = pd.read_csv(day_url)
hour_data = pd.read_csv(hour_url)

# Convert 'dteday' to datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Add weekend column
day_data['weekend'] = day_data['weekday'].isin([5, 6]).astype(int)

# Determine the busiest day (highest bike rentals)
busiest_day = day_data.loc[day_data['cnt'].idxmax()]

# Group by 6-month period and compare weekdays vs weekends
day_data['month'] = day_data['dteday'].dt.to_period('6M')
grouped = day_data.groupby(['month', 'weekend'])['cnt'].mean().unstack()

# Calculate percentage change between weekday and weekend rentals
grouped['percentage_change'] = ((grouped[0] - grouped[1]) / grouped[1]) * 100

# Calculate total percentage change across all periods
percentage_change_total = ((day_data[day_data['weekend'] == 0]['cnt'].mean() -
                             day_data[day_data['weekend'] == 1]['cnt'].mean()) /
                            day_data[day_data['weekend'] == 1]['cnt'].mean()) * 100

# Start Streamlit dashboard
st.title("Bike Sharing Analysis Dashboard")

# Display the busiest day
st.header("1. Busiest Day for Bike Rentals")
st.write(f"**Date:** {busiest_day['dteday'].strftime('%Y-%m-%d')}")
st.write(f"**Total Rentals:** {busiest_day['cnt']}")

# Visualize busiest day
fig, ax = plt.subplots()
ax.bar(busiest_day['dteday'].strftime('%Y-%m-%d'), busiest_day['cnt'], color='green')
ax.set_title('Busiest Day for Bike Rentals')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Rentals')
st.pyplot(fig)

# Display percentage change between weekday and weekend usage
st.header("2. Percentage Change in Usage: Weekdays vs Weekends (6-Month Periods)")
st.write(grouped)

# Visualize percentage change
fig, ax = plt.subplots()
grouped[[0, 1]].plot(kind='bar', figsize=(10, 6), ax=ax, color=['blue', 'orange'])
ax.set_title('Average Bike Rentals: Weekdays vs Weekends (6-Month Periods)')
ax.set_xlabel('6-Month Period')
ax.set_ylabel('Average Rentals')
ax.legend(['Weekdays', 'Weekends'])
st.pyplot(fig)

# Visualize the percentage change trend over time
fig, ax = plt.subplots()
ax.plot(grouped.index.astype(str), grouped['percentage_change'], marker='o', color='red')
ax.set_title('Percentage Change: Weekdays vs Weekends (6-Month Periods)')
ax.set_xlabel('6-Month Period')
ax.set_ylabel('Percentage Change (%)')
ax.grid(True)
st.pyplot(fig)

# Display total percentage change
st.write(f"**Overall Percentage Change:** {percentage_change_total:.2f}%")
