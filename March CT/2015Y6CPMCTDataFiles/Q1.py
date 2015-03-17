def open_files(name):
    try:
        file = open(name, 'r')
        lines = file.readlines()
        file.close()
        new_lines = []
        for line in lines:
            line = line.rstrip()
            runner_id = line[:4]
            hour = int(line[4:5]) * 3600
            minute = int(line[6:8]) * 60
            sec = int(line[9:])
            new_lines.append([runner_id , hour+minute + sec])
            
        return new_lines

    except IOError:
        print('Unable to open file')

def insertion_sort(a):#insertion sort
    a_to_return = [a[0]]
    for runner in a[1:]: #skip first
        j = 0 #index to track
        while j < (len(a_to_return)):
            if a_to_return[j][1] > runner[1]: #timing will be at the second index
                break
            j += 1
        a_to_return.insert(j, runner)
    return a_to_return

            
        
swim = open_files('SWIM.dat')
cycle = open_files('CYCLE.dat')
run = open_files('RUN.dat')

all_competitors = []

for competitors in swim:
    all_competitors.append(competitors[0])

for competitors in cycle:
    all_competitors.append(competitors[0])

for competitors in run:
    all_competitors.append(competitors[0])

valid = []
for competitor in all_competitors:
    if all_competitors.count(competitor) == 3: #finish all 3 stages
        if competitor not in valid: #not already added
            valid.append(competitor)


timing = {}
for competitor in swim:
    if competitor[0] in valid:
        timing[competitor[0]] = competitor[1]

for competitor in cycle:
    if competitor[0] in valid:
        timing[competitor[0]] += competitor[1]

for competitor in run:
    if competitor[0] in valid:
        timing[competitor[0]] += competitor[1]


a_to_sort = []
for key in timing.keys():
    a_to_sort.append([key, timing[key]])
sorted_ = insertion_sort(a_to_sort)
print(sorted_)


timings = []
for competitor in sorted_:
    timing = competitor[1]
    timings.append(timing)


f= open('RESULTS.dat', 'w+')

for i in range(len(sorted_)-1):
    name = sorted_[i][0]
    hour = sorted_[i][1] // 3600
    minute = (sorted_[i][1] % 3600) // 60
    sec = (sorted_[i][1])  % 60
    for competitor in swim:
        if competitor[0] == name:
            swim_timing = competitor[1]
    for competitor in cycle:
        if competitor[0] == name:
            cycle_timing = competitor[1]
    for competitor in run:
        if competitor[0] == name:
            run_timing = competitor[1]
    string 
    print('{0:2>}  {1} {2}:{3}:{4}'.format(i+1, sorted_[i][0], hour, minute, sec), file = f)

f.close()

        
        
