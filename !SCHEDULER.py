#PY2
# SCHEDULE TASKS FROM THE DEPENDENCY MAP
# TO BE RUN FOR THE CURRENT TASK TO BE FREE

def task2complete(task, startkey) :
    assert startkey in task, "can't find key"
    result = list()
    taskList = list(task[startkey]);
    for x in taskList :
        if x in task :    result.extend(task2complete(task, x));
        result.append(x)

    return result

# assume N = leaf node if it is not in the dependency map
Task = dict()
Task['A'] = ('B', 'C')
Task['B'] = ('D', 'E')
Task['C'] = ('G', 'H')
Task['D'] = ('X', 'Y', 'Z')

startKey = 'A'
completionSchedule = task2complete(Task, startKey) + list(startKey)
print completionSchedule

# THE RUN ON MY UBUNTU:
# $python main.py:
# ['X', 'Y', 'Z', 'D', 'E', 'B', 'G', 'H', 'C', 'A']

