"""Peluncur SafeTalk: jalankan file ini, aplikasi langsung terbuka di browser."""
import http.server, socketserver, threading, webbrowser, os, sys

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))   # selalu pakai folder tempat run.py berada
URL = f"http://localhost:{PORT}/index.html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

socketserver.ThreadingTCPServer.allow_reuse_address = True
try:
    server = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), Handler)
except OSError:
    print(f"Server sudah berjalan di port {PORT}. Membuka aplikasi...")
    webbrowser.open(URL)
    sys.exit()

print(f"SafeTalk berjalan di {URL}")
print("Tekan Ctrl+C di terminal ini untuk berhenti.")
threading.Timer(0.5, lambda: webbrowser.open(URL)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nBerhenti.")
