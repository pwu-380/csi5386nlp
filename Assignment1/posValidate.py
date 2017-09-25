ORACLE_FILE = 'data/POS_tagger_output.txt'
RESULTS_FILE = 'out/POS_results.txt'
SAVEFILE = 'out/POS_diff.txt'
NUMLINES = 10

file_oracle = open(ORACLE_FILE, 'r')
file_results = open(RESULTS_FILE, 'r')
file_diff = open(SAVEFILE, 'w')

error = 0
total = 0
count = 1

while True:
    line1 = file_oracle.readline()

    if not line1: break

    list1 = line1.split()
    line2 = file_results.readline()

    if (line1 != line2):
        list2 = line2.split()
        for j in range(len(list1)):
            if list1[j] != list2[j]:
                error += 1

        file_diff.write("Line " + str(count) + ":\n")
        file_diff.write(line1)
        file_diff.write(line2)

    total += len(list1)
    count += 1

print "Accuracy:", 1 - (error+0.0)/total
