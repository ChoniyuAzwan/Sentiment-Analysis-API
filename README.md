# Sentiment-Analysis-API
- ini adalah program membuat API untuk sentiment analysis. 
- menggunakan dataset teks dengan sentimen positif dan negatif masing-masing sebanyak 1000 baris.
- menggunakan 2 jenis algoritma yaitu decision tree dan random forest

## cara running
- jalankan sintaks `python app.py`
- buka browser, masukkan url `http://localhost:8900/?query=`, isi url setelah tanda `=` dengan suatu teks, lalu tekan enter, maka akan tampil sentimen dari teks tersebut

![url](https://raw.githubusercontent.com/ChoniyuAzwan/Sentiment-Analysis-API/master/url.PNG)

## cara kerja
### preprocessing
- dataset akan di stemming terlebih dahulu menggunakan library Sastrawi
### feature extraction
- ekstrak fitur dataset tersebut menjadi vektor menggunakan `CountVectorizer`, dihasilkan vektor dengan ukuran (2000, 4792)
- buat label target sentimen yaitu positif dan negatif sebagai angka 1 dan 0, biasanya menggunakan `LabelEncoder`
### model building
- split dataset menjadi 2 bagian yaitu sebagai data train dan data test dengan porsi 80:20
- lakukan proses fitting/training terhadap data train dengan algoritma decision tree dan random forest
- setelah itu cek tingkat akurasi terhadap data test, dihasilkan akurasi decision tree dan random forest secara berurut yaitu

![akurasi](https://raw.githubusercontent.com/ChoniyuAzwan/Sentiment-Analysis-API/master/akurasi.PNG)

### analisa
- tingkat akurasi kedua algoritma tersebut masih sangat buruk, hal tersebut mungkin dikarenakan jumlah dataset yang kurang bannyak dan kurangnya hyperparameter tuning
- random forest menghasilkan tingkat akurasi yang lebih tinggi dibandingkan decision tree karena
