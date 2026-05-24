import http.server
import socketserver
import os
import threading
import time
import subprocess
import urllib.request
import json

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

def get_github_token():
    res = subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=REPO_DIR, capture_output=True, text=True)
    url = res.stdout.strip()
    if "ghp_" in url:
        return "ghp_" + url.split("ghp_")[1].split("@")[0]
    return None

def auto_sync():
    while True:
        time.sleep(300) # 5 minutes
        print("Running Git sync...")
        subprocess.run(["git", "add", "."], cwd=REPO_DIR)
        
        status_res = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_DIR, capture_output=True, text=True)
        if not status_res.stdout.strip():
            print("No changes to sync.")
            continue
            
        timestamp = int(time.time())
        branch_name = f"scratch_sync_{timestamp}"
        
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=REPO_DIR)
        res = subprocess.run(["git", "commit", "-m", "fixes"], cwd=REPO_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if res.returncode == 0:
            subprocess.run(["git", "push", "-u", "origin", branch_name], cwd=REPO_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            token = get_github_token()
            if token:
                try:
                    remote_res = subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=REPO_DIR, capture_output=True, text=True)
                    remote_url = remote_res.stdout.strip()
                    repo = "GroundNG/Realtime-Server"
                    if "github.com/" in remote_url:
                        repo_part = remote_url.split("github.com/")[1]
                        if repo_part.endswith(".git"):
                            repo_part = repo_part[:-4]
                        repo = repo_part
                    
                    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/pulls", 
                        data=json.dumps({
                            "title": "fixes",
                            "head": branch_name,
                            "base": "main",
                            "body": "PR for fixes"
                        }).encode("utf-8"),
                        headers={
                            "Authorization": f"Bearer {token}",
                            "Accept": "application/vnd.github.v3+json",
                            "Content-Type": "application/json"
                        },
                        method="POST"
                    )
                    with urllib.request.urlopen(req) as response:
                        pr_data = json.loads(response.read().decode())
                        pr_number = pr_data["number"]
                        print(f"Created PR #{pr_number}")
                        
                        time.sleep(1)
                        
                        merge_req = urllib.request.Request(f"https://api.github.com/repos/{repo}/pulls/{pr_number}/merge",
                            data=json.dumps({
                                "commit_title": f"Merge {branch_name} into main"
                            }).encode("utf-8"),
                            headers={
                                "Authorization": f"Bearer {token}",
                                "Accept": "application/vnd.github.v3+json",
                                "Content-Type": "application/json"
                            },
                            method="PUT"
                        )
                        with urllib.request.urlopen(merge_req) as merge_response:
                            print(f"Merged PR #{pr_number}")
                except Exception as e:
                    print(f"Failed to create/merge PR: {e}")
                    if hasattr(e, 'read'):
                        print(e.read().decode())
            else:
                print("No GitHub token found, couldn't create PR.")
                
            subprocess.run(["git", "checkout", "main"], cwd=REPO_DIR)
            subprocess.run(["git", "branch", "-D", branch_name], cwd=REPO_DIR)
            subprocess.run(["git", "pull", "origin", "main"], cwd=REPO_DIR)

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
