import compcluster
import matplotlib.pyplot as plt

def histp(compn):
    data = compcluster.cat(compn)
    ndata = []
    for comp in data:
        comp[1] = float(comp[1])
        ndata.append(comp[1])
    plt.hist(ndata, ec="black")
    plt.title(("Hsitogram of all " + compn))
    plt.xlabel("Price ($)")
    plt.ylabel("Frequency")
    plt.savefig("image.png")
    plt.clf()