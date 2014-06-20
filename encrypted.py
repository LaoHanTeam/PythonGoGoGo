from Crypto.Hash import SHA256
hash = SHA256.new()
hash.update('message')
dig = hash.digest()
print dig
