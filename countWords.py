import string 

def countFreqs(text):
    exclude = set(string.punctuation)
    exclude.add('\n')
    exclude.add('\r')
    text = ''.join(ch if ch not in exclude else " " for ch in text)
    counts = {}
    words = text.split()
    for w in words:
       counts.setdefault(w, 0)
       counts[w] += 1
    return counts


