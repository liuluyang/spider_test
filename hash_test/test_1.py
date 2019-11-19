import hashlib


list_new = ['1180540275', '1560257495', 'lly888123']
hashstr = ''.join(list_new)
hashstr = hashlib.sha1(hashstr.encode()).hexdigest()

print(hashstr)