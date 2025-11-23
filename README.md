# KyuAr

KyuAr adalah alat simpel buat bikin QRIS (Quick Response Code Indonesian Standard) dengan nominal yang udah ditentukan. Cocok banget buat kamu yang jualan atau siapa aja yang mau bikin QRIS biar pembeli tinggal scan, nggak perlu ngetik nominal lagi.

## Fitur
- Bikin QRIS dengan nominal tetap (dynamic QRIS)
- Pakai string merchant QRIS kamu sendiri
- Setting gampang lewat file `.env`

## Syarat
- Python 3.6 ke atas
- Library `qrcode`
- Library `python-dotenv`

## Cara Pakai

### 1. Clone Repo Ini
```
git clone <url-repo-ini>
cd KyuAr
```

### 2. Install Library yang Dibutuhin
```
pip install qrcode[pil] python-dotenv
```

### 3. Atur Data QRIS Kamu
Buka file `.env`, terus isi:
- `QRIS_BASE` dengan string merchant QRIS kamu (screenshot qris kamu, dan gunakan qr scanner untuk mendapatkan string merchant QRIS)
- `AMOUNT` dengan nominal default (dalam rupiah, tanpa titik/koma)

Contoh isi `.env`:
```
QRIS_BASE=00020131021126610014COM.GO-JEK.WWW011893600914389369521641210G8936952160303UMI51440014ID.CO.QRIS.WWW0215ID10243317644480303UMI5204581653033605802ID5907600661055577262070703A0163046ACB
AMOUNT=12000
```

### 4. Bikin QRIS-nya
Jalankan script ini:
```
python main.py
```
Nanti bakal muncul file PNG (misal: `qris_12000.png`) yang isinya QRIS sesuai nominal yang kamu atur.

### 5. Ganti Nominal (Opsional)
Kalau mau nominal lain, tinggal ubah `AMOUNT` di `.env` lalu jalankan lagi script-nya.

## Catatan
- Pastikan string merchant QRIS kamu bener dan masih aktif.
- QR code yang dihasilkan bisa discan sama aplikasi pembayaran apapun yang support QRIS.

## Lisensi
MIT