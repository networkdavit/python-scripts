import hashlib

def hash_md5(word):
    hash_object = hashlib.md5(f"{word}".encode('utf-8'))
    hashed = hash_object.hexdigest()
    print(hashed)
hash_md5("test")