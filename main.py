import sys
import csv
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

dataset = 'SINGGALANG.tsv'
data = pd.read_csv(dataset, sep='\t', error_bad_lines=False, engine="python", names=['word', 'tag'], quoting=csv.QUOTE_NONE)
print(data.head())