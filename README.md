# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias _dropout_.

Jumlah _dropout_ yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan _dropout_ sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
1. Tingginya jumlah siswa yang _dropout_
2. Tidak adanya perangkat atau sistem yang dapat memonitor situasi dan kondisi siswanya

### Cakupan Proyek
1. Mengidentifikasi faktor apa saja yang mendukung siswa untuk _dropout_
2. Mengembangkan sebuah model yang dapat memprediksi apakah siswa tersebut akan _dropout_ atau tidak

### Persiapan

Sumber data: [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

1. Unduh _file_ **submission.zip** dan dataset di link di atas kemudian ekstrak pada sebuah direktori
2. Buka dan jalankan **Anaconda Prompt**
3. pindah ke direktori tempat menyimpan _files_ yang telah diekstrak tadi
 
```
cd (nama direktori/folder yang memiliki file-file yang telah diunduh)
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
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

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

Sedangkan untuk menjalankannya melalui link, bisa diakses dengan klik link berikut: 

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
