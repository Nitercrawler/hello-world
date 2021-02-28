import csv

# user input for the file
fileName = input()

wordsFrequency = {}

with open(fileName, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for word in row:
            if word not in wordsFrequency.keys():
                wordsFrequency[word] = 1
            else:
                wordsFrequency[word] += 1

    for key in wordsFrequency.keys():
        print(key + " " + str(wordsFrequency[key]))
