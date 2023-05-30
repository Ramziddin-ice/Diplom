def create_shingles(text, k):
    # text: Matn
    # k: Shingle uzunligi

    shingles = set()
    for i in range(len(text) - k + 1):
        shingle = text[i:i + k]
        shingles.add(shingle)
    return shingles

import hashlib

def hash_shingles(shingles):
    hashes = []
    for shingle in shingles:
        # Hash qilish
        hash = hashlib.md5(shingle.encode()).hexdigest()
        hashes.append(hash)
    return hashes

