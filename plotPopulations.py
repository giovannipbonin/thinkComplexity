import plotCcdf
import populations
import matplotlib.pylab as pylab
import sys


def main(script, *args):
    pops = populations.ReadData()
    pylab.figure(0)
    pylab.subplot(3,1,1)
    pylab.title("CDF")
    pylab.xlabel("Population")
    pylab.ylabel("Probability")
    plotCcdf.plot_cdf(pops, 'linear', 'linear')
    pylab.subplot(3,1,2)
    pylab.title("CDF")
    plotCcdf.plot_cdf(pops, 'log', 'linear')
    pylab.ylabel("Probability")
    pylab.xlabel("Population")
    pylab.subplot(3,1,3)
    pylab.title("CDF")
    pylab.ylabel("Probability")
    pylab.xlabel("Population")
    plotCcdf.plot_cdf(pops, 'log', 'log')
    pylab.figure(1)
    pylab.subplot(3,1,1)
    pylab.title("CCDF")
    pylab.xlabel("Population")
    pylab.ylabel("Probability")
    plotCcdf.plot_ccdf(pops, 'linear', 'linear')
    pylab.subplot(3,1,2)
    pylab.title("CCDF")
    plotCcdf.plot_ccdf(pops, 'log', 'linear')
    pylab.ylabel("Probability")
    pylab.xlabel("Population")
    pylab.subplot(3,1,3)
    pylab.title("CCDF")
    pylab.ylabel("Probability")
    pylab.xlabel("Population")
    plotCcdf.plot_ccdf(pops, 'log', 'log')
    pylab.show()

    


if __name__ == '__main__':
    main(*sys.argv)
