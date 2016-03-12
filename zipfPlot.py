import countWords
import matplotlib.pylab as pylab

f = open('pg1661.txt', 'r')
s = f.read()
wordFreq = countWords.countFreqs(s)
freqs = wordFreq.values()
freqs = sorted(freqs)
freqs.reverse()
wordNumber = len(freqs)

pylab.xscale('log')
pylab.yscale('log')
pylab.plot(range(1, wordNumber + 1), freqs)
pylab.show()



