import h2o
import pandas as pd
import streamlit as st
from preprocessor import input_preprocessor
h2o.init()

model = h2o.load_model('StackedEnsemble_Best1000_1_AutoML_1_20230525_225903')

def prediksi(DC235, DC024, DC025, DC205, DC270a, DC237, DC214, DC142a, DC226) :
    df = input_preprocessor(DC235, DC024, DC025, DC205, DC270a, DC237, DC214, DC142a, DC226)
    preds = model.predict(h2o.H2OFrame(df))
    value = preds['predict'][0,:][0,0]

    if value == '1' :
        return 'Layak Minum'
    else :
        return 'Tidak Layak Minum'

dc235_opt = st.selectbox(
    'Lokasi Sumber Air',
    ('Di Hunian Pribadi', 'Di Lahan/Taman Pribadi', 'Lainnya')
)

dc024_opt = st.selectbox(
    'Wilayah',
    ('Aceh', 'Sumatera Utara', 'Sumatera Barat', 
     'Riau', 'Jambi', 'Sumatera Selatan', 'Bengkulu',
     'Lampung', 'Banga Belitung', 'Kepulauan Riau',
     'Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur',
     'Yogyakarta', 'Banten', 'Bali', 'Nusa Tenggara Barat',
     'Nusa Tenggara Timur', 'Kalimantan Barat', 'Kalimatan Tengah',
     'Kalimantan Selatan', 'Kalimantan Timur', 'Kalimantan Utara',
     'Sulawesi Utara', 'Sulawesi Tengah', 'Sulawesi Selatan',
     'Sulawesi Tenggara', 'Gorontalo', 'Sulawesi Barat',
     'Gorontalo', 'Maluku', 'Maluku Utara', 'Papua', 'Papua Barat')
)

dc025_opt = st.selectbox(
    'Jenis Daerah Tempat Tinggal',
    ('Perkotaan', 'Pedesaan')
)

dc205_opt = st.selectbox(
    'Jenis Fasilitas Toilet',
    ('Siram',
     'Siram Menuju Pipa Saluran Pembuangan',
     'Siram Menuju Septic Tank',
     'Siram Menuju Lubang Jamban',
     'Siram Menuju Tempat Lain',
     'Siram (Tempat Dituju Tidak Diketahui)',
     'Siram Tanpa Septic Tank',
     'Siram (Publik / Bersama)',
     'Lubang (Latrine)',
     'Lubang Terventilasi (Improved Latrine)',
     'Lubang Dengan Lempeng',
     'Lubang Tanpa Lempeng',
     'Tanpa Fasilitas',
     'Semak semak / Sungai / Lapangan / Pantai / Kolam',
     'Toilet Kompos',
     'Toilet Ember',
     'Toilet Gantung',
     'Lainnya')
)

dc270a_opt = st.select_slider(
    'Indeks Kekayaan (Kuintil)',
    ([1,2,3,4,5])
)

dc237_opt = st.selectbox(
    'Adanya Tindakan Terhadap Air Agar Aman Diminum',
    ('Ada', 'Tidak')
)

dc214_opt = st.selectbox(
    'Bahan Utama Dinding',
    ('Alami',
     'Bambu / Palem / Batang Kayu',
     'Tanah',
     'Parsial',
     'Bambu Dengan Lumpur',
     'Batu Dengan Lumpur',
     'Tanah Liat Terbuka',
     'Plywood',
     'Kardus',
     'Kayu Yang Digunakan Kembali',
     'Dinding Utuh',
     'Anyaman Bambu',
     'Batu Dengan Semen',
     'Blok Semen',
     'Tanah Liat Tertutup',
     'Papan Kayu',
     'Kawat Plester',
     'Semen Bertulang Serat Kaca / Gipsum / Asbes',
     'Lainnya')
)

dc142a_opt = st.number_input('Ukuran Lantai Rumah (dalam meter persegi)')

dc226_opt = st.selectbox(
    'Jenis Bahan Bakar Memasak',
    ('Listrik',
     'LPG',
     'Gas Alami',
     'Biogas',
     'Kerosene',
     'Batu Bara, Gambut',
     'Arang',
     'Kayu',
     'Jerami / Semak / Rumput',
     'Tanaman Pertanian',
     'Kotoran Hewan',
     'Tidak Ada Kegiatan Memasak Di Rumah',
     'Lainnya')
)

if(st.button('Predict')) :
    st.write('Air {}'.format(prediksi(dc235_opt, dc024_opt, dc025_opt, dc205_opt, dc270a_opt, dc237_opt, dc214_opt, dc142a_opt, dc226_opt)))