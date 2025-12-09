import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memuat dataset
df = pd.read_csv("StudentsPerformance.csv")

# Judul Aplikasi
st.title("Data Performa Siswa - Tingkat Pendidikan Orang Tua")

# Menampilkan beberapa baris pertama dari dataset
st.write("### 5 Baris Pertama dari Dataset")
st.write(df.head())

# Menampilkan distribusi tingkat pendidikan orang tua
st.write("### Distribusi Tingkat Pendidikan Orang Tua")
education_counts = df['parental level of education'].value_counts()
st.write(education_counts)

# Menampilkan grafik batang distribusi tingkat pendidikan orang tua
st.write("### Diagram Batang: Tingkat Pendidikan Orang Tua")
st.bar_chart(education_counts)

# Menambahkan filter berdasarkan tingkat pendidikan orang tua
st.sidebar.title("Filter Berdasarkan Tingkat Pendidikan Orang Tua")
education_filter = st.sidebar.selectbox("Pilih Tingkat Pendidikan Orang Tua", options=["Semua"] + list(df['parental level of education'].unique()))

# Menyaring data berdasarkan pilihan
if education_filter != "Semua":
    filtered_data = df[df['parental level of education'] == education_filter]
else:
    filtered_data = df

# Menampilkan data yang sudah difilter
st.write("### Data yang Terfilter")
st.write(filtered_data)

# Menampilkan statistik nilai berdasarkan tingkat pendidikan orang tua
st.write("### Statistik Nilai Siswa Berdasarkan Tingkat Pendidikan Orang Tua")
avg_scores = filtered_data.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()
st.write(avg_scores)

# Menampilkan grafik sebar untuk nilai matematika vs membaca
st.write("### Grafik Sebar: Nilai Matematika vs Membaca")
plt.figure(figsize=(8, 6))
plt.scatter(filtered_data['math score'], filtered_data['reading score'], c=filtered_data['parental level of education'].map(education_counts), cmap='viridis')
plt.title('Klasterisasi: Nilai Matematika vs Membaca')
plt.xlabel('Nilai Matematika')
plt.ylabel('Nilai Membaca')
plt.colorbar(label='Tingkat Pendidikan Orang Tua')
st.pyplot(plt)
