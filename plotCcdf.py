import matplotlib.pylab as pylab
import random
import Cdf


def plot_ccdf(values, prob, xscale, yscale):
    pylab.yscale(yscale)
    pylab.xscale(xscale)
    compProb = [1 - e for e in prob] 
    pylab.plot(values, compProb)
    

values = [random.expovariate(10) for i in range(1000)]
cdfExpo = Cdf.MakeCdfFromList(values)
y1, p1 = cdfExpo.Render()
values = [random.paretovariate(1) for i in range(1000)]
cdfPareto = Cdf.MakeCdfFromList(values)
y2, p2 = cdfPareto.Render()

pylab.subplot(2, 1, 1)
plot_ccdf(y1, p1, 'linear', 'log')
pylab.subplot(2, 1, 2)
plot_ccdf(y2, p2, 'log', 'log')
pylab.show()
