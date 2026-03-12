import gspread
from oauth2client.service_account import ServiceAccountCredentials
from duckduckgo_search import DDGS 
import time
import random 


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

try:
    sheet = client.open("Tracer_Alumni_Umm").sheet1
    print(" Koneksi Sheets Berhasil.")
except Exception as e:
    print(f" Gagal buka Sheets: {e}")
    exit()


def run_tracker():
    print(" Menjalankan Job Pelacakan (Mode Penyamaran Browser)...")
    data = sheet.get_all_records()
    
    
    header_human = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    with DDGS(headers=header_human) as ddgs:
        for i, row in enumerate(data, start=2): 
            if row['Status'] == 'Belum Dilacak' or not row['Link_Temuan']:
                nama = row['Nama']
                print(f"\n Mencari: {nama}...")
                
                
                query = f"{nama} UMM Informatika"
                
                try:
                    
                    results = list(ddgs.text(query, max_results=1))
                    
                    if results:
                        link_ketemu = results[0]['href']
                        sheet.update_cell(i, 3, link_ketemu) 
                        sheet.update_cell(i, 4, 'PENDING')
                        print(f" BERHASIL: {link_ketemu}")
                    else:
                        print(f" Tidak ditemukan hasil untuk {nama}")
                
                except Exception as e:
                    print(f" Terjadi kendala teknis: {e}")
                
                
                jeda = random.randint(3, 7)
                print(f" Menunggu {jeda} detik sebelum pencarian berikutnya...")
                time.sleep(jeda)
            else:
                print(f"⏭ {nama} sudah ada data, skip.")

if __name__ == "__main__":
    run_tracker()
    print("\n Selesai. Silakan cek dashboard kamu!")