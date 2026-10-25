import json
import os
from datetime import datetime
from urllib.parse import quote
import webbrowser

RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

FILE = "reports.json"

def banner():
    os.system("clear")
    print(RED + r"""
╔══════════════════════════════════╗
║       ZEN WA REPORT TOOL         ║
║       MANUAL REPORT SYSTEM       ║
╚══════════════════════════════════╝
""" + RESET)

def load_reports():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

def save_report():
    banner()
    number = input("Nomor terkait (+kode negara): ").strip()
    print("\nKategori:")
    categories = [
        "Spam",
        "Penipuan",
        "Pelecehan",
        "Akun mencurigakan",
        "Lainnya"
    ]

    for i, category in enumerate(categories, 1):
        print(f"[{i}] {category}")

    try:
        choice = int(input("\nPilih kategori: "))
        if choice not in range(1, len(categories) + 1):
            raise ValueError
    except ValueError:
        print("Pilihan tidak valid.")
        input("Enter untuk kembali...")
        return

    details = input("Jelaskan kejadian berdasarkan fakta: ").strip()

    if not number or not details:
        print("Nomor dan keterangan wajib diisi.")
        input("Enter untuk kembali...")
        return

    report = {
        "waktu": datetime.now().isoformat(timespec="seconds"),
        "nomor": number,
        "kategori": categories[choice - 1],
        "keterangan": details,
        "status": "Draft - belum dikirim"
    }

    reports = load_reports()
    reports.append(report)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(reports, f, ensure_ascii=False, indent=2)

    print("\nLaporan disimpan secara lokal.")
    print("Status: Draft - belum dikirim.")
    input("\nTekan Enter untuk kembali...")

def view_reports():
    banner()
    reports = load_reports()

    if not reports:
        print("Belum ada draft laporan.")
    else:
        for i, report in enumerate(reports, 1):
            print(f"\n--- Draft {i} ---")
            print("Waktu:", report["waktu"])
            print("Nomor:", report["nomor"])
            print("Kategori:", report["kategori"])
            print("Keterangan:", report["keterangan"])
            print("Status:", report["status"])

    input("\nTekan Enter untuk kembali...")

def official_help():
    banner()
    url = "https://www.whatsapp.com/contact/"
    print("Membuka halaman kontak resmi WhatsApp...")
    print("Kirim laporan melalui kanal resmi dan jelaskan fakta.")
    webbrowser.open(url)
    input("\nJika halaman tidak terbuka, akses URL di atas manual.\nEnter untuk kembali...")

def main():
    while True:
        banner()
        print("[1] Buat draft laporan")
        print("[2] Lihat draft tersimpan")
        print("[3] Buka kontak resmi WhatsApp")
        print("[0] Keluar")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            save_report()
        elif choice == "2":
            view_reports()
        elif choice == "3":
            official_help()
        elif choice == "0":
            print("ZEN WA REPORT TOOL ditutup.")
            break
        else:
            input("Pilihan tidak valid. Enter untuk lanjut...")

if __name__ == "__main__":
    main()
