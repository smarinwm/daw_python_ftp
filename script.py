import os
from ftplib import FTP

HOST = "192.168.1.50"
USER = "webdev"
PASS = "daw123"
LOCAL_PATH = r"C:\Users\Alumno\Desktop\ProyectoWeb"
REMOTE_PATH = "/mi_sitio"

ftp = FTP(HOST)
ftp.login(USER, PASS)

for root, dirs, files in os.walk(LOCAL_PATH):
    rel_path = os.path.relpath(root, LOCAL_PATH)
    
    if rel_path == ".":
        current_remote_dir = REMOTE_PATH
    else:
        current_remote_dir = f"{REMOTE_PATH}/{rel_path.replace(os.sep, '/')}"
        try:
            ftp.mkd(current_remote_dir)
        except:
            pass

    for filename in files:
        local_file = os.path.join(root, filename)
        remote_file = f"{current_remote_dir}/{filename}"
        
        with open(local_file, "rb") as f:
            ftp.storbinary(f"STOR {remote_file}", f)

ftp.quit()