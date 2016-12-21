import csv

#takes in a list of strings -> separates into a list of lists of strings on ';' and prints to file
def printToFile(data, fileName):
	outputFile = open(fileName,'a')
	outputWriter=csv.writer(outputFile, dialect='excel')

	for i in range(len(data)):
		element = data[i].split(';')
		outputWriter.writerow(element)

	outputFile.close()	