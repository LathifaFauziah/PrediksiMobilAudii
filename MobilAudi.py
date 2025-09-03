import streamlit as st

# Judul aplikasi
st.title("🚗 Prediksi Harga Mobil Audi (Rumus Sederhana)")

# ===== Gambar =====
st.image('Audiimage.jpeg', use_container_width=True)

# ===== Deskripsi =====
st.markdown(
    """
    Audi merupakan salah satu produsen mobil premium asal Jerman yang dikenal dengan
    kombinasi desain elegan, teknologi canggih, serta performa bertenaga. Sebagai bagian
    dari Volkswagen Group, Audi telah menjadi pionir dalam menghadirkan inovasi di dunia otomotif.

    Dari mobil kompak hingga supercar, Audi selalu menghadirkan pengalaman berkendara yang
    memadukan kenyamanan, keamanan, dan kekuatan mesin. Bahkan dalam pasar mobil bekas,
    Audi tetap menjadi pilihan menarik berkat kualitas material, kabin mewah, dan teknologi
    yang relevan hingga kini. Dengan perawatan yang baik, mobil Audi bekas mampu memberikan
    nilai investasi yang tinggi sekaligus kepuasan berkendara jangka panjang.
    """
)

# Input user
model_mobil = st.selectbox("Pilih Model Mobil", ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "Q2", "Q3", "Q4", "Q5", "Q6","Q7","Q8"])
tahun = st.selectbox("Pilih Tahun Mobil", [2010, 2011, 2012, 2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
transmisi = st.selectbox("Pilih Transmisi", ["Manual", "Automatic","SemiAuto"])
bahan_bakar = st.selectbox("Pilih Jenis Bahan Bakar", ["Petrol", "Diesel", "Hybrid"])
pajak = st.text_input("Masukkan Pajak Mobil (Rp)", "750.000")
kilometer = st.text_input("Masukkan Kilometer yang Sudah Ditempuh", "20.000")
mesin = st.text_input("Masukkan Ukuran Mesin (cc)", "1.500")
tangki_per_liter = st.text_input("Masukkan Kapasitas Tangki Bahan Bakar (liter)", "50")

# Konversi input (hapus titik, ubah ke int)
try:
    pajak = int(pajak.replace(".", ""))
    kilometer = int(kilometer.replace(".", ""))
    mesin = int(mesin.replace(".", ""))
    tangki_per_liter = int(tangki_per_liter.replace(".", ""))
except ValueError:
    st.error("Masukkan angka yang valid (gunakan format 1.500.000)")
    pajak, kilometer, mesin, tangki_per_liter = 0, 0, 0, 0

# Tombol prediksi
if st.button("🔮 Prediksi Harga"):
    # Harga dasar sesuai model
    harga_dasar = {
        "A1": 250_000_000,
        "A2": 280_000_000,
        "A3": 320_000_000,
        "A4": 137_000_000,
        "A5": 285_000_000,
        "A6": 165_000_000,
        "A7": 375_000_000,
        "A8": 590_000_000,
        "Q2": 600_000_000,
        "Q3": 400_000_000,
        "Q4": 230_000_000,
        "Q5": 700_000_000,
        "Q6": 418_000_000,
        "Q7": 500_000_000,
        "Q8": 850_000_000,
    }[model_mobil]

# Depresiasi tiap tahun
    depresiasi_per_tahun = 15_000_000
    depresiasi = (2025 - tahun) * depresiasi_per_tahun

    # Transmisi
    tambahan_transmisi = 10_000_000 if transmisi == "Automatic" else 0

    # Bahan bakar
    if bahan_bakar == "Diesel":
        tambahan_bahan_bakar = 5_000_000
    elif bahan_bakar == "Hybrid":
        tambahan_bahan_bakar = 20_000_000
    else:
        tambahan_bahan_bakar = 0

    # Kilometer (setiap 10.000 km = -2 juta)
    pengaruh_km = (kilometer // 10000) * 2_000_000

    # Pajak (0.1% dari pajak ditambahkan)
    pengaruh_pajak = pajak * 0.001

    # Mesin
    tambahan_mesin = 5_000_000 if mesin > 1500 else 0

    # Hitung harga akhir
    harga_prediksi = (
        harga_dasar
        - depresiasi
        - pengaruh_km
        + tambahan_transmisi
        + tambahan_bahan_bakar
        + pengaruh_pajak
        + tambahan_mesin
    )

    # Batas harga minimum
    harga_prediksi = max(harga_prediksi, 50_000_000)

    st.success(f"💰 Prediksi harga Audi {model_mobil} ({tahun}) adalah Rp {harga_prediksi:,.0f}")