from zipfile import ZipFile

with ZipFile('workbook.zip') as Zip_file:
  info = Zip_file.infolist()
  k = []
  for i in info:
    if not i.is_dir():
      k.append(100-(i.compress_size/i.file_size)*100)
    else:
      k.append(0)
  index_max = k.index(max(k))
  print(info[index_max].filename.split('/')[-1])