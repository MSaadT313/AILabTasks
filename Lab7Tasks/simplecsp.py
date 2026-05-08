from ortools.sat.python import cp_model

def simple_sat_program():
    model = cp_model.CpModel()
    num_var = 3
    x = model.new_int_var(0,num_var-1,"x")
    y = model.new_int_var(0,num_var-1,"y")
    z = model.new_int_var(0,num_var-1,"z")

    model.add( x!=y )
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"X = {solver.value(x)}")
        print(f"Y = {solver.value(y)}")
        print(f"Z = {solver.value(z)}")
    else:
        print("No solution")

simple_sat_program()

# 1. The simplest possible callback class
class EasyPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        super().__init__() # Initializes the parent class easily
        self.vars = variables
        self.count = 0

    def on_solution_callback(self):
        self.count += 1
        # Print the values as a simple list
        print([self.value(v) for v in self.vars])

model = cp_model.CpModel()
x, y, z = [model.new_int_var(0, 2, name) for name in ['x', 'y', 'z']]
model.add(x != y)

# 3. Solve
solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True
printer = EasyPrinter([x, y, z])

solver.solve(model, printer)
print(f"Total solutions: {printer.count}")