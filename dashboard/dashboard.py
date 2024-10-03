import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URL untuk mengunduh dataset harian dan dataset per jam
day_url = "https://raw.githubusercontent.com/Priesma/Proyek-Analisis-Data---Bike-Sharing-Dataset/main/data/day.csv"
hour_url = "https://raw.githubusercontent.com/Priesma/Proyek-Analisis-Data---Bike-Sharing-Dataset/main/data/hour.csv"

# Memuat dataset dari URL
day_data = pd.read_csv(day_url)
hour_data = pd.read_csv(hour_url)

# Mengonversi kolom 'dteday' menjadi format datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Menambahkan kolom untuk menandai akhir pekan (weekend), 1 jika hari Sabtu atau Minggu, 0 jika hari kerja
day_data['weekend'] = day_data['weekday'].isin([5, 6]).astype(int)

# Menentukan hari tersibuk (jumlah penyewaan sepeda tertinggi)
busiest_day = day_data.loc[day_data['cnt'].idxmax()]

# Mengelompokkan data per periode 6 bulan, membandingkan penyewaan pada hari kerja vs akhir pekan
day_data['month'] = day_data['dteday'].dt.to_period('6M')
grouped = day_data.groupby(['month', 'weekend'])['cnt'].mean().unstack()

# Menghitung persentase perubahan penyewaan sepeda antara hari kerja dan akhir pekan
grouped['percentage_change'] = ((grouped[0] - grouped[1]) / grouped[1]) * 100

# Menghitung total persentase perubahan dari seluruh periode
percentage_change_total = ((day_data[day_data['weekend'] == 0]['cnt'].mean() - 
                             day_data[day_data['weekend'] == 1]['cnt'].mean()) / 
                            day_data[day_data['weekend'] == 1]['cnt'].mean()) * 100

# Mulai Streamlit dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")

# Menampilkan hari tersibuk (jumlah penyewaan sepeda tertinggi)
st.header("1. Hari Tersibuk untuk Penyewaan Sepeda")
st.write(f"**Tanggal:** {busiest_day['dteday'].strftime('%Y-%m-%d')}")
st.write(f"**Total Penyewaan:** {busiest_day['cnt']}")

# Visualisasi hari tersibuk dalam bentuk diagram batang
fig, ax = plt.subplots()
ax.bar([busiest_day['dteday'].strftime('%Y-%m-%d')], [busiest_day['cnt']], color='green')
ax.set_title('Hari Tersibuk untuk Penyewaan Sepeda')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Menampilkan persentase perubahan antara penggunaan pada hari kerja dan akhir pekan
st.header("2. Persentase Perubahan Penggunaan: Hari Kerja vs Akhir Pekan (Periode 6 Bulan)")
st.write(grouped)

# Visualisasi rata-rata penyewaan selama hari kerja dan akhir pekan dalam bentuk diagram batang
fig, ax = plt.subplots()
grouped[[0, 1]].plot(kind='bar', figsize=(10, 6), ax=ax, color=['blue', 'orange'])
ax.set_title('Rata-Rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan (Periode 6 Bulan)')
ax.set_xlabel('Periode 6 Bulan')
ax.set_ylabel('Rata-Rata Penyewaan')
ax.legend(['Hari Kerja', 'Akhir Pekan'])
st.pyplot(fig)

# Visualisasi tren persentase perubahan penggunaan dari waktu ke waktu
fig, ax = plt.subplots()
ax.plot(grouped.index.astype(str), grouped['percentage_change'], marker='o', color='red')
ax.set_title('Persentase Perubahan: Hari Kerja vs Akhir Pekan (Periode 6 Bulan)')
ax.set_xlabel('Periode 6 Bulan')
ax.set_ylabel('Persentase Perubahan (%)')
ax.grid(True)
st.pyplot(fig)

# Menampilkan total persentase perubahan
st.write(f"**Persentase Perubahan Total:** {percentage_change_total:.2f}%")
