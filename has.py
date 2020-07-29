import hashlib
password = 'https://superuser.com/questions/339997/how-to-open-a-terminal-quicklyhttps://superuser.com/questions/339997/how-to-open-a-terminal-quickly-from-a-file-explorer-at-a-folder-in-windows-7-from-a-file-explorer-at-a-folder-in-windows-7'
h = hashlib.md5(password.encode())
print(h.hexdigest())
