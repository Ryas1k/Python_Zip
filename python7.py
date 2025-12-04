from zipfile import ZipFile

def bait(in_bytes: int):
    table = {1: "B", 1024: "KB", 1048576: "MB", 1073741824: "GB"}
    for key, val in sorted(table.items(), reverse=True):
        if in_bytes > key:
            return f"{round(in_bytes/key)} {val}"

def bait1(in_bytes, k=0):
    return (
        f"{round(in_bytes)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}"
        if in_bytes < 1024
        else bait1(in_bytes / 1024, k + 1)
    )

with ZipFile("desktop.zip", mode="r") as files_zip:
    info = files_zip.infolist()
    for i in info:
        i1 = i.filename.strip("/").split("/")
        if not i.is_dir():
            a = bait(i.file_size)
        else:
            a = ""
        print(f'{"  "*(len(i1)-1)}{i1[-1]} {a}')
