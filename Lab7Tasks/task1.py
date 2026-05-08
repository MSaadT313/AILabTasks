from ortools.sat.python import cp_model
#declaring an emplty model object
model = cp_model.CpModel()
# decalring an empty dictionart
shiftoptions = {}
# pre defined values
workers = 5
shifts = 3
days = 7
maxshiftsperday = 1
maxdifference = 1

# looping through all data and adding data in the dictionary
# boolean variable to tell if a given worker works on a day on a shift or  not
# all are tuples and keys

for x in range(workers):
    for y in range(days):
        for z in range(shifts):
            shiftoptions[(x,y,z)] = model.NewBoolVar("shift with id " + str(x) + " " + str(y) + " " + str(z)+"\n")

#after this we have now put all the values in the shift option ditionary with keys of x,y,z like a powerset
# now we will add a constraint which we will add constraint to reduce this data set


# now adding a shift variable to only one worker
# after this we will loop through only days and shifts for workers only for each worker only one shift

for y in range(days):
    for z in range(shifts):
        model.Add(sum(shiftoptions[(x, y, z)] for x in range(workers)) == 1)


# now we add a constraint that the worker could cover only one shift per day 0 or 1

for x in range(workers):
    for y in range(days):
        model.Add(sum(shiftoptions[(x,y,z)] for z in range(shifts)) <= 1)
print(shiftoptions)

# now we want to add a constriant that all workers should get equal shifts and working days
# for it we define minimum shit for each worker

minshiftsperworker = (shifts * days) // workers
print(minshiftsperworker)

# also we define the max shift for each worker maxdiff is predefined in the question

maxshiftsperworker = minshiftsperworker + maxdifference

# now we loop through each worker and add these max and min values of shift assign to a specific worker

for x in range(workers):
    shiftsassigned = 0
    for y in range(days):
        for z in range(shifts):
            shiftsassigned += shiftoptions[(x,y,z)]
    model.Add(minshiftsperworker <= shiftsassigned)
    model.Add(shiftsassigned <= maxshiftsperworker)


# solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    for y in range(days):
        print("day " + str(y))
        for x in range(workers):
            is_working = False
            for z in range(shifts):
                if solver.Value(shiftoptions[(x,y,z)]):
                    is_working = True
                    print("worker " +str(x) +" works day " + str(y) +" shift " + str(z))
            if not is_working:
                print('  Worker {} does not work'.format(x))
        print()