# Sistem Intelijen Pelacakan Alumni (Informatika UMM)

 sistem berbasis web yang dirancang untuk membantu Program Studi Informatika UMM dalam melakukan pelacakan jejak digital alumni secara otomatis. Sistem ini mengintegrasikan otomasi bot, cloud database, dan dashboard verifikasi.

## 1. Fitur Utama
- **Automated Tracking**: Bot Python yang melakukan pencarian jejak alumni di web publik.
- **Cloud Database Integration**: Menggunakan Google Sheets API sebagai database real-time dan gratis.
- **Hybrid Tracking Mode**: Menggabungkan kecerdasan bot dengan intervensi manusia (Human-in-the-loop).
- **Manual Search Fallback**: Tombol pencarian manual cerdas yang otomatis menghasilkan query pencarian di Google jika bot otomatis mengalami kendala.
- **Responsive Dashboard**: Antarmuka Admin modern menggunakan Tailwind CSS, dideploy di Vercel.

## 2. Arsitektur Sistem
Sistem ini menggunakan arsitektur tiga lapis:
1. **Frontend**: Dashboard web statis di Vercel.
2. **Database**: Google Sheets https://docs.google.com/spreadsheets/d/1b1EZNe0Fvlg2HeOaRaNQfL3iXulhg81joU5c-hSNR2M/edit?usp=sharing (Sinkronisasi via CSV & API).
3. **Backend/Worker**: Skrip Python (`tracer_bot.py`) sebagai engine pencari otomatis.

## 3. Tabel Pengujian 

| ID | Kriteria Kualitas | Skenario Uji | Hasil yang Diharapkan | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T01** | **Konektivitas Data** | Mengambil data dari Google Sheets | Dashboard menampilkan data alumni secara real-time | **PASS** |
| **T02** | **Otomasi Backend** | Menjalankan skrip `tracer_bot.py` | Bot mengupdate link dan status ke Sheets secara otomatis | **PASS** |
| **T03** | **Fallback System** | Klik tombol "Cari Manual" di Web | Sistem membuka tab baru dengan query [Nama + UMM] yang tepat | **PASS** |
| **T04** | **Interaction Design** | Klik tombol "Validasi" | Muncul feedback instan kepada Admin setelah verifikasi | **PASS** |

## 4. Kendala Teknis & Mitigasi 
Dalam pengembangannya, sistem menghadapi tantangan berupa **IP Blocking/Rate Limiting** dari mesin pencari publik saat menjalankan bot otomatis secara beruntun.

**Solusi Rekayasa Interaksi yang diterapkan:**
1. **User-Agent Spoofing**: Bot menyamar sebagai browser untuk mengurangi risiko blokir.
2. **Smart Search Button**: Menyediakan tombol pencarian manual pada Dashboard Admin. Ini menjamin proses bisnis pelacakan tetap berjalan 100% meskipun bot otomatis diblokir oleh server pihak ketiga.

## 5. Cara Menjalankan
1. **Frontend**: Akses melalui link Vercel yang tersedia.
2. **Backend**: 
   - Instal library: `pip install gspread oauth2client ddgs`
   - Jalankan: `python tracer_bot.py`

---
