# Sistem Case-Based Reasoning (CBR) untuk Retrieval Putusan KDRT Mahkamah Agung

## Deskripsi Proyek

Proyek ini merupakan implementasi sistem **Case-Based Reasoning (CBR)** pada domain hukum, khususnya perkara **Kekerasan Dalam Rumah Tangga (KDRT)** yang bersumber dari putusan Mahkamah Agung Republik Indonesia.

Sistem dikembangkan untuk membantu proses pencarian kasus hukum yang memiliki kemiripan dengan kasus baru menggunakan pendekatan:

* TF-IDF
* Cosine Similarity
* Support Vector Machine (SVM)
* Naive Bayes
* IndoBERT Embedding

Implementasi dilakukan menggunakan Python dan Google Colab sesuai dengan tahapan yang ditentukan pada tugas.

---

# Tujuan

1. Mengumpulkan dan mempersiapkan dataset putusan KDRT.
2. Membangun representasi kasus hukum yang terstruktur.
3. Melakukan retrieval kasus serupa menggunakan metode machine learning dan transformer.
4. Mengevaluasi performa sistem retrieval.
5. Menerapkan konsep Case-Based Reasoning pada domain hukum.

---

# Dataset

Dataset terdiri dari 30 putusan Mahkamah Agung Republik Indonesia pada domain Kekerasan Dalam Rumah Tangga (KDRT).

Sumber data:

https://putusan3.mahkamahagung.go.id

Format awal data:

* PDF Putusan
* TXT hasil ekstraksi teks

---

# Struktur Folder

```text
project/

│
├── data/
│   ├── raw/
│   │   ├── putusan_001.txt
│   │   ├── putusan_002.txt
│   │   └── ...
│   │
│   ├── processed/
│   │   ├── cases.csv
│   │   ├── cases.json
│   │   ├── metadata_summary.csv
│   │   ├── feature_summary.csv
│   │   └── dataset_profile.csv
│   │
│   └── eval/
│       └── queries.json
│
├── notebooks/
│   ├── Tahap_1_Data_Preparation.ipynb
│   ├── Tahap_2_Case_Representation.ipynb
│   ├── Tahap_3_Case_Retrieval.ipynb
│   ├── Tahap_4_Case_Reuse.ipynb
│   └── Tahap_5_Evaluation.ipynb
│    
├── README.md
└── requirements.txt
```

---

# Tahap 1 — Data Preparation

## Tujuan

Mempersiapkan corpus putusan KDRT yang siap diproses.

## Kegiatan

* Mengumpulkan putusan KDRT
* Ekstraksi teks dari PDF
* Cleaning dokumen
* Normalisasi teks
* Penyimpanan corpus

## Output

```text
data/raw/*.txt
```

---

# Tahap 2 — Case Representation

## Tujuan

Membentuk representasi kasus yang dapat digunakan pada sistem CBR.

## Informasi yang Diekstrak

### Metadata

* Nomor perkara
* Tahun putusan
* Tingkat peradilan
* Pengadilan asal
* Pasal
* Terdakwa
* Korban

### Konten Utama

* Ringkasan fakta
* Argumen hukum
* Amar putusan

### Feature Engineering

* Jenis KDRT
* Outcome
* Retrieval Text
* Word Count
* Unique Words

## Output

```text
cases.csv
cases.json
metadata_summary.csv
feature_summary.csv
dataset_profile.csv
```

---

# Tahap 3 — Case Retrieval

## Tujuan

Menemukan kasus lama yang paling mirip dengan kasus baru.

## Pendekatan

### TF-IDF

Menggunakan:

```python
TfidfVectorizer
```

### Machine Learning

* Support Vector Machine (SVM)
* Naive Bayes

### Transformer

* IndoBERT

Model:

```text
indobenchmark/indobert-base-p1
```

### Similarity

Menggunakan:

```python
cosine_similarity()
```

## Fungsi Retrieval

```python
retrieve(query, k=5)
```

Proses:

1. Pre-processing query
2. Transform query menjadi vektor
3. Hitung cosine similarity
4. Ambil Top-K kasus

## Output

```text
data/eval/queries.json
```

---

# Tahap 4 — Case Reuse

## Tujuan

Menggunakan solusi dari kasus lama yang paling mirip untuk memberikan rekomendasi pada kasus baru.

## Kegiatan

* Mengambil top-k kasus hasil retrieval
* Mengidentifikasi outcome
* Menghasilkan rekomendasi solusi

Output:

```text
recommended_solution
```

---

# Tahap 5 — Evaluation

## Tujuan

Mengukur performa sistem retrieval.

## Metrik Evaluasi

### Classification

* Accuracy
* Precision
* Recall
* F1-Score

### Retrieval

* Precision@K
* Recall@K
* Mean Reciprocal Rank (MRR)

## Output

```text
evaluation_report.csv
```

---

# Library yang Digunakan

```text
pandas
numpy
scikit-learn
transformers
torch
matplotlib
seaborn
json
re
```

---

# Cara Menjalankan

## 1. Install Dependensi

```bash
pip install -r requirements.txt
```

## 2. Jalankan Tahap 1

```bash
Tahap_1_Data_Preparation.ipynb
```

## 3. Jalankan Tahap 2

```bash
Tahap_2_Case_Representation.ipynb
```

## 4. Jalankan Tahap 3

```bash
Tahap_3_Case_Retrieval.ipynb
```

## 5. Jalankan Tahap 4

```bash
Tahap_4_Case_Reuse.ipynb
```

## 6. Jalankan Tahap 5

```bash
Tahap_5_Evaluation.ipynb
```

---

# Penulis

Nama: Dino Alfian Zamri
Nama: M. Yusron Alghoni

NIM: 202310370311329
NIM: 202310370311333

Mata Kuliah: Penalaran_Komputer_Case-Based-Reasoning

Program Studi: Informatika

Universitas: Muhammadiyah Malang

---

# Kesimpulan

Sistem ini menerapkan pendekatan Case-Based Reasoning pada domain hukum KDRT dengan memanfaatkan representasi teks, machine learning, dan transformer untuk menemukan kasus-kasus serupa secara otomatis sehingga dapat membantu proses analisis hukum berbasis preseden kasus.
