import matplotlib.pylab as pylab
import random
import Cdf
import sys


def plot_ccdf(values, xscale, yscale):
    pylab.yscale(yscale)
    cdf = Cdf.MakeCdfFromList(values)
    values, prob = cdf.Render()
    pylab.xscale(xscale)
    compProb = [1 - e for e in prob] 
    pylab.plot(values, compProb)

def plot_cdf(values, xscale, yscale):
    pylab.yscale(yscale)
    cdf = Cdf.MakeCdfFromList(values)
    values, prob = cdf.Render()
    pylab.xscale(xscale)
    pylab.plot(values, prob)
    

def main(script, *args):
    values = [random.expovariate(10) for i in range(1000)]
    pylab.subplot(2, 1, 1)
    plot_ccdf(values, 'linear', 'log')
    pylab.subplot(2, 1, 2)
    values = [random.paretovariate(1) for i in range(1000)]
    plot_ccdf(values, 'log', 'log')
    pylab.show()

if __name__ == '__main__':
    main(*sys.argv)
