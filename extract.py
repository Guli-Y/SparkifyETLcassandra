import os
import csv

def collect_files():
    """
    collect the path of all the data files into a list
    """
    datapath = os.path.join(os.getcwd(), 'data')
    file_path_list = []
    for root, dirs, files in os.walk(datapath):
        for file in files:
            file_path = os.path.join(root, file)
            file_path_list.append(file_path)
    return file_path_list

def extract_data():
    """
    reads all the data files and create a merged csv file called processed_data.csv
    """
    files = collect_files()

    # read all the files and add all the rows into data list
    data = []
    for file in files:
        with open(file, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            for line in reader:
                data.append(line)
    print(len(data), 'rows of data\n')

    # write all the rows into process_data.csv
    with open('processed_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['artist','firstName','gender','itemInSession','lastName',
                         'length', 'level','location','sessionId','song','userId'])
        for line in data:
            if line[0]=='':
                continue
            writer.writerow([line[i] for i in [0, 2, 3, 4, 5, 6, 7, 8, 12, 13, -1]])
    with open('processed_data.csv', 'r', newline='') as f:
        print(len(data)-sum(1 for line in f), 'rows of data were dropped due to missing artist\n')
