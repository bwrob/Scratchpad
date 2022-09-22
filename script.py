import helpers
import csv
import ast
if __name__ == '__main__':
    with open("./run.csv", 'r') as file:
        csvreader = csv.reader(file,delimiter=';')
        for row in csvreader:
            inputs = ast.literal_eval(row[1])
            print(inputs)
            callable = getattr(helpers,row[0])
            output = callable(*inputs)
            print(output)