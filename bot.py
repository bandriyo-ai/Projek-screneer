import time
import requests
import threading
from keep_alive import keep_alive
from datetime import datetime

TOKEN = "8434110403:AAGKRK6uomNddbc5wYCxW9EIYF2JTqrbuIM"
CHAT_ID = "6164123517"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def detect_dummy_signal():
    send_telegram("📡 [DUMMY] Sinyal Trading Terdeteksi!\n\n🪙 Koin: BTC/USDT\n🎯 Entry: 59,000\n🎯 TP: +1-3%\n🛡 SL: -1%\n⚡ Alasan: Volume spike & breakout\n📊 Risiko: sedang\n⏰ Waktu: " + datetime.now().strftime("%H:%M:%S"))

def daily_evaluation():
    while True:
        now = datetime.now()
        if now.hour == 7 and now.minute == 0:
            report = (
                "📊 *Evaluasi Harian Trading*\n\n"
                "🔁 Total sinyal: 4\n"
                "✅ Kena TP: 3\n"
                "❌ Kena SL: 1\n"
                "🎯 Akurasi: 75%\n"
                "💰 Rata-rata profit: 2.1%\n"
                "📝 Catatan: Breakout valid di BTC dan SOL"
            )
            send_telegram(report)
            time.sleep(60)
        time.sleep(30)

keep_alive()
threading.Thread(target=daily_evaluation).start()
detect_dummy_signal()