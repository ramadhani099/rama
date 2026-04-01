def client_cek_status_penerbangan_via_api(nomor_penerbangan, thread_name):
    target_url = f"{BASE_API_URL}/penerbangan/{nomor_penerbangan}/status"
    print(f"[{thread_name}] Mengecek status penerbangan: {nomor_penerbangan}")
    
    try:
        response = requests.get(target_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"[{thread_name}] Penerbangan {nomor_penerbangan} ke {data.get('tujuan')}: Status {data.get('status')}")
        elif response.status_code == 404:
            print(f"[{thread_name}] Penerbangan {nomor_penerbangan} tidak ada dalam jadwal.")
        else:
            print(f"[{thread_name}] Terjadi kesalahan saat memproses penerbangan {nomor_penerbangan} (Status code: {response.status_code})")
    except requests.exceptions.Timeout:
        print(f"[{thread_name}] Permintaan timeout saat mengecek penerbangan {nomor_penerbangan}.")
    except requests.exceptions.RequestException as e:
        print(f"[{thread_name}] Terjadi error saat melakukan permintaan: {e}")
    
    print(f"[{thread_name}] Selesai memproses penerbangan: {nomor_penerbangan}")