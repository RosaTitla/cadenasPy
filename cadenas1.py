
unaLst=["omicron", "pi", "rho"]

# Demostración del método join()
print(",".join(["omicron", "pi", "rho"]))

print(",".join(unaLst))
cad=' '.join(unaLst)
#cad.join(unaLst)
print('cad',cad)

# Demostración del método lower()
print("SiGmA=60".lower())

t="     tia"
print(t)
r=t.lstrip()
print(r)
# Demostración del método the lstrip()
print("[" + "    tau ".lstrip() + "]")

print("pythoninstitute.org".lstrip(".org"))
print("www.cisco.com".lstrip("w."))

# Demostración del método replace()
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# Demostración del método rfind()
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demostración del método rstrip()
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demostración del método split()
print("Rosario Titla Flores".split())
# Demostración del método startswith()
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demostración del método strip()
print("[" + "   aleph   ".strip() + "]")

# Demostración del método startswith()
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()
# Demostración del método swapcase()
print("Yo sé que no sé nada.".swapcase())

print()

# Demostración del método title()
print("Yo sé que no sé nada. Parte 1.".title())
print()
# Demostración del método upper()
print("Yo sé que no sé nada. Parte 2.".upper())


