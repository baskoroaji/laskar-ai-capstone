# Capstone Project: Kenal Jiwa

## Business Understanding  
Gangguan kesehatan mental di kalangan remaja dan dewasa muda menjadi isu serius di seluruh dunia. WHO melaporkan bahwa sekitar 1 dari 7 remaja usia 10-19 tahun mengalami gangguan mental (World Health Organization, 2024). Depresi, kecemasan, dan gangguan perilaku menduduki peringkat utama penyebab  permasalahan pada kelompok umur ini. Di sisi lain, bunuh diri merupakan penyebab kematian urutan ke-3 bagi usia 15-29 tahun secara global (World Health Organization, 2024). Ketimpangan ini diperparah oleh stigma  sosial, kurangnya literasi kesehatan mental, dan keterbatasan akses layanan konvensional membuat banyak masalah kesehatan mental anak muda tidak terdeteksi dan ditangani secara menyeluruh, khususnya di negara berkembang. Kondisi mental yang buruk di usia muda dapat mengganggu prestasi pendidikan, produktivitas dan keterlibatan sosial kelompok remaja di masa depan (Patel et al., 2018). Lancet Commission dan WHO menekankan bahwa memajukan kesehatan mental adalah bagian penting dari tujuan Sustainable Development Goals (SDGs) 3.4 tentang promotif kesehatan mental (World Health Organization, 2016). Hal ini menunjukkan bahwa peningkatan kesehatan mental anak muda tidak hanya berdampak pada kesejahteraan individu, tetapi juga berkontribusi pada kemajuan pendidikan, kesetaraan gender, dan pertumbuhan ekonomi nasional. 


Situasi ini tercermin pula di Indonesia. Survei Riset Kesehatan Dasar (Riskesdas) tahun 2018 menunjukkan bahwa 6,2% penduduk berusia 15-24 tahun mengalami depresi (Kementerian Kesehatan Republik Indonesia, 2023). Survey lain yang telah dilakukan oleh Indonesia-National Adolescent Mental Health Survey (I-NAMHS) pada tahun 2022 menunjukkan bahwa sekitar 1 dari 3 remaja (34,9 %) atau setara dengan 15,5 juta anak muda di Indonesia mengalami masalah kesehatan mental, namun hanya 2,6% di antaranya yang pernah mengakses layanan dukungan atau konseling untuk masalah emosi (Indonesia – National Adolescent Mental Health Survey, 2023). Temuan ini mengindikasikan adanya kesenjangan serius antara prevalensi gangguan dan intervensi yang tersedia, serta menguatkan kebutuhan akan solusi yang adaptif dan menjangkau kelompok usia ini secara tepat. Pemerintah berupaya dengan melakukan inisiasi seperti Swaperiksa PDSKJI dan fitur screening pada SATUSEHAT Mobile (Kemenkes) telah diluncurkan sebagai bentuk intervensi digital. Namun, kedua platform ini masih terbatas dalam hal user targeting dan belum sepenuhnya mengadopsi pendekatan berbasi pengalaman pengguna yang interaktif. 

Oleh karena itu, Kenal Jiwa hadir sebagai solusi dalam bentuk website asesmen digital berbasis AI yang ditujukan bagi kalangan Gen Z dan dibawahnya. Alasan utama pemilihan target ini adalah karena kelompok usia ini sedang berada di fase rentan secara psikososial, menghadapi tekanan akademik, sosial, identitas diri, serta merupakan digital native yang lebih responsif terhadap pendekatan teknologi. Dalam konteks SDGs, solusi ini mendukung tujuan 3: Kehidupan Sehat dan Sejahtera, terutama pada indikator 3.4 terkait pengurangan mortalitas akibat gangguan mental dan peningkatan pencegahan bunuh diri

### Permasalahan Bisnis  
1. Apakah model machine learning ini dapat bekerja dengan baik dalam pengujian ketika menentukan kondisi keadaan kesehatan mental seseorang?
2. Seberapa tinggi akurasi dari model machine learning (ex: Random Forest, Logistic Regression, XGBoost) dalam mengklasifikan depresi dan anxiety pada populasi Gen Z Indonesia?
3. Algoritma ML (bandingkan 2 algoritma seperti Random Forest, XGBoost, Logistic Regression, dll) mana yang menghasilkan performa terbaik dalam memprediksi status depresi dan kecemasan pada populasi Gen Z Indonesia? 

## Persiapan  

**Sumber data**:  
- Depression Dataset: [Depression Dataset](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset)
- Depression Dataset: [Anxiety Dataset](https://www.kaggle.com/datasets/natezhang123/social-anxiety-dataset)

**Setup environment**:  

1. Buat virtual environment
```
conda create -name capstone_project python=3.12.9
conda activate capstone_project
```

2. Install dependencies
```
pip install requirements.txt
```
3. Running Project
```
streamlit run Home.py
```
