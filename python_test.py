from zipfile import ZipFile
def cal(in_bytes: int):
  table = {1:'B',1024:'KB',1048576: 'MB', 1073741824: 'GB'}
  for key,val in sorted(table.items(),reverse=True):
    if in_bytes > key:
      return round(in_bytes/key), val