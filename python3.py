from zipfile import ZipFile
from datetime import datetime

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    for item in sorted(info, key=lambda x: x.filename.split("/")[-1]):
        if item.is_dir():
            continue
        print(
            f"{item.filename.split('/')[-1]}\n  Дата модификации файла: {datetime(*item.date_time)}\n  Объем исходного файла: {item.file_size} байт(а)\n  Объем сжатого файла: {item.compress_size} байт(а)\n"
        )
