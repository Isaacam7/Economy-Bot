import useful
def cat(keyn):
    idata = useful.load(r"market\market.csv")[1:]

    clusters = []
    for i in range(len(idata)):
        idata[i][0] = idata[i][0].split()

        if idata[i][0][-1] in clusters:
            pass
        else:
            clusters.append(str(idata[i][0][-1]))

    clusters = {clustern: [] for clustern in clusters}

    for j in range(len(idata)):
        for key in clusters:
            if idata[j][0][-1] == key:
                idata[j][0] = ' '.join(idata[j][0])
                clusters[key].append(idata[j])
    return(clusters[keyn])
