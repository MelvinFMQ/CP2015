#Q3

def import_records(name):
    try:
        file = open(name, 'r')
        lines = file.readlines()
        file.close()
        new_lines = []
        for line in lines:
            line = line.rstrip()
            date = line[:8]
            cust_id = line[8:14]
            price = float(line[15:].lstrip())
            new_lines.append([date, cust_id, price])
            
        return new_lines

    except IOError:
        print('Unable to open file')

l = open_files('TRANSACTIONS.dat')

q = queue()
for line in l:
    q.enqueue(line)
print(open_files('TRANSACTIONS.dat'))
