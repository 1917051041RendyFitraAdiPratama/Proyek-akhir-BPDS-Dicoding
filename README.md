# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan
## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias _dropout_.

Jumlah _dropout_ yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan _dropout_ sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
1. Tingginya jumlah siswa yang _dropout_

   Jumlah siswa yang _dropout_ perlu dikurangi untuk menjaga reputasi dan daya tarik institusi. Jumlah _dropout_ yang tinggi dapat mencerminkan ketidakpuasan siswa terhadap kualitas pendidikan atau dukungan yang diberikan. Tingginya angka dropout dapat mengakibatkan berkurangnya jumlah pendaftar baru, menurunnya kepercayaan orang tua dan calon siswa, serta berpotensi merusak reputasi institusi di mata masyarakat dan pihak pemangku kepentingan lainnya.

2. Tidak adanya perangkat atau sistem yang dapat memonitor situasi dan kondisi siswanya

   Tanpa sistem pemantauan yang efektif, institusi sulit untuk mengidentifikasi siswa yang berpotensi dropout secara tepat waktu dan memberikan intervensi yang diperlukan. Hal ini membuat upaya pencegahan dropout menjadi kurang efisien dan tidak terarah. Tanpa sistem monitoring, institusi tidak dapat secara proaktif menangani masalah siswa yang mengalami kesulitan akademik atau personal yang dapat menyebabkan dropout. Ini dapat mengakibatkan peningkatan jumlah dropout, yang pada gilirannya akan merugikan institusi dalam jangka panjang, baik dari segi finansial maupun reputasi.

### Cakupan Proyek
Pekerjaan yang akan dilakukan dalam proyek ini antara lain adalah:

1. Melakukan proses _Exploratory Data Analysis_ (EDA)
2. Mengidentifikasi faktor apa saja yang mendukung siswa untuk _dropout_. 
3. Mengembangkan sebuah model yang dapat memprediksi apakah siswa tersebut akan _dropout_ atau tidak

Adapun _output_ dari proyek ini adalah:

1. Visualisasi data
2. Dasbor yang berisi berbagai ringkasan infromasi siswa pada institut ini
3. Sebuah _prototype_ model _machine learning_ yang dapat melakukan prediksi apakah siswa akan _dropout_ atau tidak

### Persiapan

Sumber data: [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

1. Unduh _file_ zip dari repositori ini  kemudian ekstrak pada sebuah direktori
2. Buka dan jalankan **Anaconda Prompt**
3. pindah ke direktori tempat menyimpan _files_ yang telah diekstrak tadi
 
```
cd path/to/destination/directory
```
 
4. Membuat environment baru dengan nama sesuai keinginan
 
```
conda create --name <nama-venv> python=3.10
```
 
5. Mengaktifkan environment yang telah dibuat
 
```
conda activate <nama-venv>
```
 
6. _Install_ semua library yang dibutuhkan
 
```
pip install -r requirements.txt
```
 
7. Jalankan jupyter notebook
 
```
jupyter-notebook .
```
 
8. Unggah dataset yang  telah diunduh dan letakkan dalam satu folder dengan berkas _notebook.ipynb_
9. Buka dan jalankan berkas _notebook.ipynb_.


## Business Dashboard

Terdapat dua bisnis dasbor yang dibuat pada proyek ini. Kedua dasbor tersebut memiliki fungsinya masing-masing. Berikut penjelasan dari tiap dasbornya:

1. Student's Personal Information
   
   Dasbor ini terdiri dari beberapa ringkasan informasi diri dari siswa. Informasi diri tersebut terdiri dari berapa banyak jumlah siswa yang ada pada data ini, persentase siswa yang merupakan siswa internasional (di luar Negara Portugis), persentase pemegang beasiswa, persentase siswa yang merupakan pengungsi, dan masih banyak lagi. Dasbor ini dilengkapi fitur _interactive filtering_. Dengan fitur tersebut, pengguna dapat melakukan penyaringan data dengan cara mengklik pada grafik yang tersedia.

2. Analysis
   
   Dasbor ini terdiri dari informasi biaya UKT apakah sudah yang terkini, persentase pemegang beasiswa dan merupakan pengungsi, nilai pada pendidikan sebelumnya, nilai yang diperlukan ketika masuk perguruan tinggi, dan informasi SKS. Digunakan untuk mengetahui bagaimana kriteria siswa yang lulus, _dropout_, ataupun masih terdaftar.

Dasbor tersebut telah dipublikasi di Tableau Public dan bisa diakses di link berikut: [Dashboard](https://public.tableau.com/views/DashboardProyekAkhirBPDS/StudentsPersonalInformationSummary?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link) 

*direkomendasikan untuk mengaksesnya menggunakan laptop atau PC dengan _fullscreen_ untuk mendapatkan visualisasi yang lebih baik.

## Menjalankan Sistem Machine Learning

Untuk menjalankan _prototype machine learning_ yang telah dibuat, bisa diakses menggunakan dua cara, yaitu menjalankannya di lokal ataupun melalui link streamlit. Berikut adalah tahapan yang perlu dilakukan jika ingin menjalankan _prototype_ di lokal:

1. Buka terminal pada _virtual environment_ yang telah dibuat sebelumnya.
2. Pastikan direktori saat ini menampung berkas-berkas yang telah diekstrak sebelumnya, terutama yang memiliki berkas **app.py**. Jika belum di direktori yang tepat, bisa menggunakan perintah di bawah

```
cd path/to/destination/directory
```

3. Setelah direktorinya sesuai, bisa menjalankan perintah di bawah

```
streamlit run app.py
```

4. Setelah berhasil dijalankan, masukkan data yang sesuai kemudian klik tombol **Predict** untuk mengetahui status siswa tersebut.

Sedangkan untuk menjalankannya melalui link, bisa diakses dengan klik link berikut: [Jaya Jaya Institute App](https://proyek-akhir-bpds-dicoding-normanfebrio.streamlit.app/)

## Conclusion

Jumlah siswa yang _dropout_ di perguruan tinggi ini mencapai angka 1421 siswa (32%). Angka tersebut merupakan angka yang cukup tinggi. Setelah dianalisis, ternyata terdapat beberapa faktor yang dapat memengaruhi siswa tersebut akan _dropout_ atau tidak. Faktor yang memiliki pengaruh cukup kuat dalam menentukan siswa tersebut akan _dropout_ atau tidak adalah biaya UKT yang telah di-_update_ atau tidak. Siswa yang _dropout_ karena biaya UKT-nya belum ter-_update_ mencapai angka 86% dari total keseluruhan siswa yang biaya UKT-nya belum ter-_update_. Kemudian, terdapat pola menarik pada nilai yang didapat oleh siswa pada saat semester 1 dan 2. Siswa yang lulus cenderung memiliki persebaran nilai yang lebih tinggi daripada siswa yang _dropout_ dan _enrolled_. 

### Rekomendasi Action Items

Untuk mengurangi angka siswa yang _dropout_, dapat dilakukan rekomendasi berikut:

- Selalu lakukan pembaruan biaya UKT menjadi yang terkini agar dapat mengurangi jumlah siswa yang _dropout_. Pembaruan biaya UKT yang terkini akan memastikan bahwa siswa tidak mengalami masalah keuangan yang tidak terduga, yang dapat menyebabkan mereka dropout. Tindakan yang dapat dilakukan adalah melakukan audit rutin setiap semester untuk memastikan bahwa semua data biaya UKT telah diperbarui. Tim keuangan dapat mengirimkan pengingat otomatis kepada siswa dan orang tua tentang pembaruan biaya UKT.

- Lebih memerhatikan siswa yang mendapatkan nilai yang rendah (di bawah 13), baik itu di semester pertama ataupun semester kedua. Tindakan yang dapat diberikan pada siswa dengan kriteria tersebut adalah seperti memberikan bimbingan akademik, mendorong siswa untuk konsultasi dengan dosen pembimbing mengenai masalah atau rintangan yang dihadapi oleh siswa ketika belajar, dan memberikan kelas remedial untuk siswa yang nilainya rendah.
