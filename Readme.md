# Proyek Analisis Data: Bike Sharing Dataset

---

# Dashboard Penggunaan Hari Kerja vs Akhir Pekan

Proyek ini bertujuan untuk memvisualisasikan tren perubahan penggunaan pada persewaan sepeda dalam periode waktu tertentu.
Data yang digunakan mencakup persentase perubahan penggunaan layanan dari waktu ke waktu, dibagi ke dalam periode **6 bulan**. Visualisasi dalam dashboard ini membantu dalam bagaimana penggunaan berubah antara hari kerja dan akhir pekan.

## Fitur Utama

- **Grafik Persentase Perubahan**: Menampilkan perbandingan persentase perubahan dari waktu ke waktu antara hari kerja dan akhir pekan dalam bentuk grafik garis yang interaktif.
- **Penggunaan Data Periode 6 Bulan**: Penampilan data dalam interval 6 bulan untuk memberikan pandangan terhadap pola perubahan penggunaan.

## Pastikan sudah menginstal hal-hal berikut di sistem kamu:

1. **Buat dan aktifkan virtual environment**:
   - Untuk macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Untuk Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
2. **Streamlit**:
   ```bash
   pip install streamlit
   ```
3. **Library Pendukung**:
   ```bash
   pip install pandas matplotlib
   ```

## Cara Menjalankan Dashboard

Langkah-langkah berikut untuk menjalankan dashboard:

1. Clone atau unduh repository proyek ini.
   
2. Navigasikan ke direktori proyek. Jika ada berkas bernama `dashboard.py`, jalankan command berikut di terminal atau command prompt:
   
   ```bash
   streamlit run dashboard/dashboard.py
   ```

   Jika file Python dashboard ada di lokasi lain atau bernama berbeda, sesuaikan path-nya.

3. Dashboard akan terbuka secara otomatis di browser web default.
