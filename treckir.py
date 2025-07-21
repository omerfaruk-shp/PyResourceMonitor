import psutil           # Sistem süreçlerini ve donanım bilgilerini izlemek için kullanılır
import subprocess       # Harici programları çalıştırmak için kullanılır
import time             # Zamanla ilgili işlemler için (örneğin uyku)

# Çalıştırılacak Python dosyasının adı
target_script = "voskdenemeekran.py"  # Burayı kendi scriptinle değiştir

# Scripti başlat ve bir süreç (process) oluştur
process = subprocess.Popen(["python", target_script])

# Başlatılan sürecin PID (Process ID) numarasını al
pid = process.pid
print(f"🔍 İzlenen PID: {pid}")

try:
    # Script çalıştığı sürece döngü devam eder
    while process.poll() is None:
        proc = psutil.Process(pid)  # Süreç nesnesi oluştur (psutil ile takip edilecek)
        
        # RAM kullanımı: rss = Resident Set Size (MB cinsinden)
        mem = proc.memory_info().rss / (1024 ** 2)
        
        # CPU kullanımı (% cinsinden) – 1 saniyelik aralıkla ölçülür
        cpu = proc.cpu_percent(interval=1)
        
        # RAM ve CPU bilgilerini terminale yazdır
        print(f"💾 RAM: {mem:.2f} MB | ⚙️ CPU: {cpu:.2f}%")
        
        # Her ölçümden sonra 1 saniye beklenir (zaten cpu_percent bunu bekliyor)
        time.sleep(1)

# Eğer süreç aniden kapanırsa, hata alınmaz – yakalanır ve bilgi verilir
except psutil.NoSuchProcess:
    print("❌ Süreç sonlandı.")
