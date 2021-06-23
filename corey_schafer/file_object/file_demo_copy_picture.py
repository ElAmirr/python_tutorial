# File objects

with open('qr_couple.jpeg', 'rb') as rf:
    with open('qr_couple_copy.jpeg', 'wb') as wf:
        for line in rf:
            wf.write(line)

print('second copy with more controle')
with open('qr_couple.jpeg', 'rb') as rf:
    with open('qr_couple_controle_copy.jpeg', 'wb') as wf:
        chink_size = 4096
        rf_chunk = rf.read(chink_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chink_size)
