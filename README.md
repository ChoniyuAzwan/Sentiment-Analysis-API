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
- simpan model kedalam `pickle` untuk kemudian digunakan sebagai `API`
### use of api
- terdapat suatu program yang bertugas sebagai server
- teks yang dimasukkan melalui url akan di kirim ke server
- teks tersebut akan di preprocessing, kemudian di lakukan feature extraction untuk kemudian dapat dilakukan prediksi menggunakan model yang telah dibuat sebelumnya, prediksi dihasilkan dalam bentuk format json

![akurasi](https://raw.githubusercontent.com/ChoniyuAzwan/Sentiment-Analysis-API/master/akurasi.PNG)

### analisa
- tingkat akurasi kedua algoritma tersebut masih sangat buruk, hal tersebut mungkin dikarenakan jumlah dataset yang kurang banyak serta feature extraction dan hyperparameter tuning yang kurang optimal
- random forest menghasilkan tingkat akurasi yang lebih tinggi dibandingkan decision tree karena decision tree dapat menimbulkan overfitting serta variansi yang tinggi, maka untuk menurunkan tingkat variansi digunakanlah random forest
- random forest merupakan sekumpulan koleksi feature secara random/acak dari decision tree untuk membangun beberapa decision tree baru dengna feature yang lebih beragam, lalu kemudian merata-ratakan hasilnya yang berupa vote terbanyak dari jenis klasifikasi yang dihasilkan.
