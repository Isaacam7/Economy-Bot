import csv

def load(ifile):
    data = []
    with open(ifile, 'r',newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def export(ofile, data):
    with open(ofile, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)