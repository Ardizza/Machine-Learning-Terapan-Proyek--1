# Laporan Proyek Machine Learning - Rafi Ardizza Fadhillah Setiadi
## Domain Proyek
### Latar Belakang
Penyakit jantung adalah salah satu penyebab utama kematian di seluruh dunia. Deteksi dini dan penanganan yang tepat dapat menyelamatkan banyak nyawa. Menggunakan data medis, kita dapat mengembangkan model machine learning yang mampu memprediksi apakah seorang pasien memiliki penyakit jantung, yang pada akhirnya dapat membantu dokter dalam mengambil keputusan yang lebih baik dan lebih cepat.

### Mengapa dan bagaimana masalah ini harus diselesaikan:
* Penyakit jantung sering kali tidak menunjukkan gejala awal yang jelas, sehingga banyak kasus baru terdeteksi saat sudah pada tahap lanjut.
* Model prediksi dapat memberikan alat tambahan bagi tenaga medis untuk screening awal dan pencegahan.

## Business Understanding
### Problem Statements
* Bagaimana cara memprediksi apakah seorang pasien memiliki penyakit jantung berdasarkan data medis yang tersedia?
* Algoritma machine learning mana yang memberikan hasil prediksi terbaik untuk kasus ini?

### Goals
* Mengembangkan model machine learning yang dapat memprediksi penyakit jantung dengan akurasi tinggi.
* Membandingkan beberapa algoritma untuk menentukan model terbaik.

### Solution Statements
* Menggunakan Logistic Regression sebagai baseline model.
* Membandingkan hasil prediksi dengan algoritma Random Forest.
* Melakukan hyperparameter tuning pada model Random Forest untuk meningkatkan akurasi.

## Data Understanding
Dataset yang digunakan adalah dari Kaggle dengan link [Heart Disease Dataset](https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores) Dataset ini berisi 1025 sampel dan 14 atribut.

### Kondisi Dataset:
* Nilai Null: Dataset ini tidak memiliki nilai null, sehingga tidak diperlukan penanganan missing values.
* Sebaran Data: Dataset ini terdiri dari 14 atribut yang memiliki sebaran nilai yang bervariasi, seperti umur, tekanan darah, kolesterol, dan lain-lain.
* Distribusi Kelas: Distribusi kelas pada variabel target cukup seimbang antara pasien yang memiliki penyakit jantung dan yang tidak, sehingga tidak diperlukan penanganan untuk masalah class imbalance.

### Variabel pada Heart Disease Dataset adalah sebagai berikut:
* age: Umur pasien.
* sex: Jenis kelamin (1 = laki-laki, 0 = perempuan).
* cp: Tipe nyeri dada (0-3).
* trestbps: Tekanan darah saat istirahat.
* chol: Kolesterol serum dalam mg/dl.
* fbs: Gula darah puasa > 120 mg/dl (1 = benar, 0 = salah).
* restecg: Hasil elektrokardiografi istirahat (0-2).
* thalach: Detak jantung maksimal yang tercapai.
* exang: Angina akibat olahraga (1 = ya, 0 = tidak).
* oldpeak: Depresi ST yang diinduksi oleh olahraga relatif terhadap istirahat.
* slope: Kemiringan segmen ST latihan puncak (0-2).
* ca: Jumlah pembuluh darah utama (0-4) yang diwarnai oleh fluoroskopi.
* thal: Thalassemia (1-3).
* target: Diagnosis penyakit jantung (1 = memiliki penyakit jantung, 0 = tidak memiliki penyakit jantung).

### Exploratory Data Analysis (EDA):
1. Informasi Dataset :
   Menampilkan informasi mengenai tipe data dari masing-masing kolom serta jumlah nilai non-null di setiap kolom.

2. Statistik Deskriptif :
   Menampilkan statistik deskriptif dari dataset seperti mean, standar deviasi, nilai minimum dan maksimum, serta kuartil.

3. Visualisasi Data :
* Distribusi Variabel Target
* Pairplot
* Heatmap Korelasi Fitur

## Data Preparation
### Data Cleaning
1. Data Cleaning :
Langkah ini memastikan bahwa dataset bersih dan siap untuk digunakan dalam analisis. Dalam kasus ini, tidak ada nilai yang hilang (missing values) pada dataset, sehingga tidak diperlukan penanganan lebih lanjut untuk nilai yang hilang.

2. Normalisasi Data : 
Normalisasi adalah proses penskalaan fitur-fitur sehingga mereka berada dalam skala yang sama. Ini penting karena banyak algoritma pembelajaran mesin bekerja lebih baik ketika fitur-fitur memiliki rentang nilai yang serupa.

3. Memisahkan Fitur dan Label : 
Memisahkan fitur dan label adalah langkah di mana kita memisahkan atribut input (fitur) dari target output (label) yang ingin diprediksi oleh model.

4. Split Data Menjadi Training dan Testing Set : 
Membagi data menjadi training dan testing set adalah langkah untuk memastikan model dapat dievaluasi secara objektif. Data training digunakan untuk melatih model, sedangkan data testing digunakan untuk menguji performa model pada data yang belum pernah dilihat sebelumnya.

## Modeling
### Proses dan Tahapan:
1. Logistic Regression : 
Logistic Regression adalah metode statistik yang digunakan untuk analisis prediktif ketika hasilnya adalah variabel biner. Algoritma ini mengestimasikan probabilitas suatu peristiwa terjadi dengan menggunakan fungsi logit. Logistic Regression cocok digunakan sebagai baseline model karena cepat dan mudah diinterpretasi.

#### Tahapan pembuatan model
1. Inisialisasi Model:
Menginisialisasi model Logistic Regression tanpa parameter khusus sebagai baseline.
2. Pelatihan Model:
Model dilatih menggunakan data training (X_train dan y_train).
3. Prediksi:
Model digunakan untuk memprediksi data testing (X_test).
4. Evaluasi:
Evaluasi dilakukan menggunakan metrik akurasi dan classification report yang mencakup precision, recall, dan F1 score.

#### Parameter Utama:
* penalty: Regulasi yang digunakan untuk menghindari overfitting.
* c: Inversi dari kekuatan regulasi, dengan nilai yang lebih kecil berarti regulasi yang lebih kuat.
* solver: Algoritma yang digunakan untuk optimisasi.

2. Random Forest : 
Random Forest adalah algoritma ensemble yang terdiri dari beberapa decision tree. Setiap pohon keputusan dilatih pada subset data yang berbeda, dan hasil akhir diambil dari rata-rata prediksi semua pohon. Ini membuat Random Forest lebih robust terhadap overfitting dan sering kali lebih akurat dibandingkan model individual.

#### Tahapan pembuatan model
1. Inisialisasi Model:
   Menginisialisasi model Random Forest tanpa parameter khusus sebagai baseline.
2. Pelatihan Model:
   Model dilatih menggunakan data training (X_train dan y_train).
3. Prediksi:
   Model digunakan untuk memprediksi data testing (X_test).
4. Evaluasi:
   Evaluasi dilakukan menggunakan metrik akurasi dan classification report.

#### Parameter Utama:
* n_estimators: Jumlah pohon keputusan dalam model Random Forest.
* max_depth: Kedalaman maksimum pohon individu.
* min_samples_split: Jumlah minimum sampel yang diperlukan untuk membagi node internal.
* min_samples_leaf: Jumlah minimum sampel yang diperlukan untuk berada di node daun.

3. Hyperparameter Tuning : 
Untuk meningkatkan performa model Random Forest, dilakukan tuning terhadap beberapa hyperparameter menggunakan GridSearchCV. GridSearchCV membantu menemukan kombinasi terbaik dari hyperparameter dengan melakukan pencarian grid pada ruang parameter yang diberikan.

#### Parameter yang Dicari:
* n_estimators: Jumlah pohon keputusan dalam model Random Forest.
* max_depth: Kedalaman maksimum pohon individu.
* min_samples_split: Jumlah minimum sampel yang diperlukan untuk membagi node internal.

#### Tahapan Tuning:
1. Mendefinisikan Parameter Grid:
   Mendefinisikan parameter grid yang akan diuji.
2. Inisialisasi dan Pelatihan GridSearchCV:
   Menginisialisasi GridSearchCV dengan estimator Random Forest dan parameter grid yang telah ditentukan.
3. Model Terbaik:
   Setelah GridSearchCV selesai, lalu mengambil model terbaik yang ditemukan.
4. Evaluasi Model Terbaik:
   Mengevaluasi model terbaik menggunakan metrik akurasi dan classification report.
5. Parameter Terbaik yang Ditemukan:
   Menampilkan parameter terbaik yang ditemukan oleh GridSearchCV.
   
#### Parameter Terbaik:
* n_estimators: 100
* max_depth: 10
* min_samples_split: 2

### Kelebihan dan Kekurangan Algoritma:
* Logistic Regression: Mudah diinterpretasi, cepat, tetapi mungkin kurang akurat untuk data yang kompleks.
* Random Forest: Akurasi tinggi, robust terhadap overfitting, tetapi lebih kompleks dan membutuhkan lebih banyak waktu untuk pelatihan.

## Evaluation
Pada bagian ini, kita menggunakan beberapa metrik evaluasi untuk menilai performa model yang dikembangkan, yaitu akurasi, precision, recall, dan F1 score. Berikut penjelasan mengenai metrik yang digunakan dan hasil proyek berdasarkan metrik tersebut:

### Metrik Evaluasi yang Digunakan
Untuk kasus klasifikasi ini, digunakan empat metrik evaluasi utama:
* Akurasi (Accuracy): Akurasi adalah proporsi prediksi benar dari keseluruhan prediksi
  $$\text{Akurasi} = \frac{\text{Jumlah Prediksi Benar}}{\text{Jumlah Total Prediksi}}$$
  
- Precision: Proporsi prediksi positif yang benar dari keseluruhan prediksi positif.
  $$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$
  
* Recall: Recall adalah proporsi prediksi positif yang benar dari keseluruhan data aktual positif
  $$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$
  
* F1 Score: F1 Score adalah harmonic mean dari precision dan recall
  $$\text{F1 Score} = 2 \times \left( \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \right)$$
  
### Hasil Proyek Berdasarkan Metrik Evaluasi
1. Logistic Regression:
   * Akurasi: 0.80
   * Precision:
        * Kelas 0: 0.85
        * Kelas 1: 0.76
   * Recall
        * Kelas 0: 0.72
        * Kelas 1: 0.87
   * F1 Score
        * Kelas 0: 0.78
        * Kelas 1: 0.81
2. Random Forest
   * Akurasi: 0.99
   * Precision
        * Kelas 0: 0.97
        * Kelas 1: 1.00
   * Recall
        * Kelas 0: 1.00
        * Kelas 1: 0.97
   * F1 Score
        * Kelas 0: 0.99
        * Kelas 1: 0.99
3. Best Random Forest setelah Hyperparameter Tuning
   * Akurasi: 0.99
   * Precision
        * Kelas 0: 0.97
        * Kelas 1: 1.00
   * Recall
        * Kelas 0: 1.00
        * Kelas 1: 0.97
   * F1 Score
        * Kelas 0: 0.99
        * Kelas 1: 0.99
   
### Kesimpulan
Model Logistic Regression menunjukkan akurasi sebesar 0.80, dengan precision, recall, dan F1 score yang cukup baik untuk kedua kelas. Namun, model ini sedikit kurang dalam mendeteksi kelas normal dibandingkan kelas sakit, sebagaimana terlihat dari nilai recall yang lebih rendah pada kelas 0 (normal).

Di sisi lain, model Random Forest menunjukkan performa yang sangat baik dengan akurasi 0.99, precision, recall, dan F1 score yang hampir sempurna. Ini menunjukkan bahwa model Random Forest sangat efektif dalam mendeteksi kedua kelas (normal dan sakit).

Setelah melakukan hyperparameter tuning pada model Random Forest, performa tetap sama, yaitu akurasi sebesar 0.99 dengan nilai precision, recall, dan F1 score yang sangat tinggi. Ini menunjukkan bahwa model Random Forest sudah optimal sebelum tuning.

Dari hasil evaluasi ini, dapat disimpulkan bahwa model Random Forest, baik sebelum maupun setelah hyperparameter tuning, memberikan hasil terbaik dalam memprediksi penyakit jantung pada dataset ini. Model ini memiliki keunggulan dalam mendeteksi kedua kelas dengan sangat baik, sehingga sangat direkomendasikan untuk digunakan dalam aplikasi klinis untuk membantu deteksi dini penyakit jantung.
