import http.server
import socketserver
import os
import threading
import time
import subprocess

PORT = 8000
REPO_DIR = "/home/umang/ObsidianProjects/prep/prep"
FILE_PATH = os.path.join(REPO_DIR, "Private & Shared", "DSA Notes e10781b84fab4e28bfc9f108e7a81c07.html")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            html_content = post_data.decode('utf-8')
            if not html_content.strip().lower().startswith('<!doctype'):
                html_content = '<!DOCTYPE html>\n' + html_content
            
            with open(FILE_PATH, 'w', encoding='utf-8') as f:
                f.write(html_content)
                
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Saved')
        else:
            self.send_response(404)
            self.end_headers()

def auto_sync():
    while True:
        time.sleep(300) # 5 minutes
        print("Running Git sync...")
        subprocess.run(["git", "add", "."], cwd=REPO_DIR)
        res = subprocess.run(["git", "commit", "-m", "Auto sync from browser"], cwd=REPO_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0:
            subprocess.run(["git", "push"], cwd=REPO_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

os.chdir(REPO_DIR)

# Start auto sync in a daemon thread
threading.Thread(target=auto_sync, daemon=True).start()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Open: http://localhost:{PORT}/Private%20%26%20Shared/DSA%20Notes%20e10781b84fab4e28bfc9f108e7a81c07.html")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
