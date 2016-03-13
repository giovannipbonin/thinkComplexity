import matplotlib.pylab as pylab
import random
import Cdf


def plot_ccdf(values, prob):
    pylab.yscale('log')
    compProb = [1 - e for e in prob] 
    pylab.plot(values, compProb)
    pylab.show()
    

values = [random.expovariate(100) for i in range(10000)]
cdf = Cdf.MakeCdfFromList(values)
y, p = cdf.Render()

plot_ccdf(y, p)
