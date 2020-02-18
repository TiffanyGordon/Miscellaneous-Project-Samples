import hashlib

dict = open("dic-0294.txt", "r")
wordlist = dict.readlines()

terms = []
for item in wordlist:
    word = item[:-1]
    terms.append(word)

pw1hex = "44afbc26b785d9c5cfce73aa06dd0711f2e290d5"
pw1b = bytearray.fromhex(pw1hex)

for term in terms:
    bentry = hashlib.sha1(term.encode())
    termhex = bentry.hexdigest()
    if termhex == pw1hex:
        print(term)
        break
    else:
        continue

pw2hex = "d2e7560d96b0f6ceac88ac8d94f0fdc39d36252d2432ecb1ab510450a93b3c2c"
pw2b = bytearray.fromhex(pw2hex)

for term in terms:
    bentry = hashlib.sha256(term.encode())
    termhex = bentry.hexdigest()
    if termhex == pw2hex:
        print(term)
        break
    else:
        continue

pw3hex = "95d19ab48d18d4232b87bb086319998c"
pw3b = bytearray.fromhex(pw3hex)

for term in terms:
    bentry = hashlib.md5(term.encode())
    termhex = bentry.hexdigest()
    if termhex == pw3hex:
        print(term)
        break
    else:
        continue

salthex = "d41d8cd98f00b204e9800998ecf8427e"
saltb = bytearray.fromhex(salthex)

spw1hex = "955597a308bd22402bf841f19d393526a15396cf49e9477af9f21f45fcfe13c8"
spw1b = bytearray.fromhex(spw1hex)

for term in terms:
    bentrys = hashlib.sha256(term.encode()+saltb)
    termshex = bentrys.hexdigest()
    sbentry = hashlib.sha256(saltb+term.encode())
    stermhex = sbentry.hexdigest()
    if stermhex == spw1hex:
        print(term)
        break
    elif termshex == spw1hex:
        print(term)
        break
    else:
        continue

spw2hex = "00b961e20655b8cb16fb7aff3d3a28a3"
spw2b = bytearray.fromhex(spw2hex)

for term in terms:
    bentrys = hashlib.md5(term.encode()+saltb)
    termshex = bentrys.hexdigest()
    sbentry = hashlib.md5(saltb+term.encode())
    stermhex = sbentry.hexdigest()
    if stermhex == spw2hex:
        print(term)
        break
    elif termshex == spw2hex:
        print(term)
        break
    else:
        continue

spw3hex = "bbdefeaebc9ac07b9ad47fd8f9e1b7bf3170bcfc"
spw3b = bytearray.fromhex(spw3hex)

for term in terms:
    bentrys = hashlib.sha1(term.encode()+saltb)
    termshex = bentrys.hexdigest()
    sbentry = hashlib.sha1(saltb+term.encode())
    stermhex = sbentry.hexdigest()
    if stermhex == spw3hex:
        print(term)
        break
    elif termshex == spw3hex:
        print(term)
        break
    else:
        continue
