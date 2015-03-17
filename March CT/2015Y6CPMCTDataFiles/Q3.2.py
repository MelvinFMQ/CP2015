#Q3.2

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



def display_sales(ql): #ql is a queue linked list
    not_empty = True
    purchases = []
    while not_empty:
        purchase = ql.pop()
        if purchases = None:#reached the end
            not_empty = False
        else:
            purchases.append(purchase)
    dates = {}
    for purchase in purchases:
        date = purchase[0] #date is in the 0 index
        cost = purchase[2]
        if date not in dates.keys():
            dates[date] = cost
        else:
            dates[date] += cost
    print('Date               Sales')
    for date in dates.keys():
        print('{0}{1:>10.2f}'.format(date, dates[date])
        

l = open_files('TRANSACTIONS.dat')
q = queue()
for line in l:
    q.enqueue(line)
display_sales(q)
      
    
