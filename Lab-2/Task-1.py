from csv import reader
from math import sqrt,exp,pi
def load_csv(filename):
 dataset = list()
 with open(filename, 'r') as file:
 csv_reader = reader(file)
 for row in csv_reader:
 if not row:
 continue
 dataset.append(row)
 return dataset 
def str_column_to_int(dataset, column):
 class_values = [row[column] for row in dataset]
 unique = set(class_values)
 lookup = dict()
 for i, value in enumerate(unique):
 lookup[value] = i
 for row in dataset:
 row[column] = lookup[row[column]]
 return lookup
def separate_by_class(dataset):
 separated = dict()
 for i in range(len(dataset)):
 vector = dataset[i]
 class_value = vector[-1]
 if (class_value not in separated):
 separated[class_value] = list()
 separated[class_value].append(vector[0:-1])
 return separated
def mean(numbers):
 return sum(numbers)/float(len(numbers))
def stdev(numbers): 
 avg = mean(numbers)
 variance = sum([(x-avg)**2 for x in numbers]) /
float(len(numbers)-1)
 return sqrt(variance)
def summarize_dataset(dataset):
 summaries = [(mean(column), stdev(column), len(column)) for
column in zip(*dataset)]
 del(summaries[-1])
 #print(summaries)
 return summaries
def summarize_by_class(dataset):
 separated = separate_by_class(dataset)
 for i,j in separated.items():
 print(i,":",j)
 summaries = dict()
 for class_value, rows in separated.items():
 summaries[class_value] = summarize_dataset(rows)
 return summaries
def calculate_probability(x, mean, stdev):
 try:
 exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
 return (1 / (sqrt(2 * pi) * stdev)) * exponent 
 except ZeroDivisionError:
 return 0.5

def calculate_class_probabilities(summaries, row):
 total_rows = sum([summaries[label][0][2] for label in summaries])
 probabilities = dict()
 for class_value, class_summaries in summaries.items():
 probabilities[class_value] = summaries[class_value][0][2]/
float(total_rows)
 for i in range(len(class_summaries)):
 mean, stdev, _ = class_summaries[i]
 probabilities[class_value] *= calculate_probability(row[i],
mean, stdev)
 return probabilities
def predict(summaries, row):
 probabilities = calculate_class_probabilities(summaries, row)
 #print(probabilities)
 best_label, best_prob = None, -1
 for class_value, probability in probabilities.items():
 if best_label is None or probability > best_prob:
 best_prob = probability
 best_label = class_value
 return best_label 
filename = 'data.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
 str_column_to_int(dataset, i)
#str_column_to_int(dataset, len(dataset[0])-1)
model = summarize_by_class(dataset)
#print(model)
#input - data
row = [0,3,0,2,6,0,2,1]
label = predict(model, row)
print('\n\nData=%s, Predicted: %s' % (row, label)) 
