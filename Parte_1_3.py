from cplex import Cplex, infinity
from cplex.exceptions import CplexError

# Angle Caleb Guerrero Luna
# Mario Eduardo Lara Loredo

problem = Cplex()

problem.objective.set_sense(problem.objective.sense.maximize)

constraints_matrix = [
  [6.0, 4.0],
  [1.0, 2.0],
  [-1.0, 1.0]
]

col_names = ["x1", "x2"]

constraints = []

for i in constraints_matrix:
  new_item = [col_names]
  new_item.append(i)
  constraints.append(new_item)

problem.variables.add(
  obj = [5.0, 4.0],
  ub = [infinity, 2],
  names =  col_names
)

problem.linear_constraints.add(
  lin_expr = constraints,
  senses = ["L", "L", "L"],
  rhs = [24.0, 6.0, 1.0],
  names = ["c1", "c2", "c3"]
)

problem.solve()

print(f"Objective value: {problem.solution.get_objective_value()}")
print(list(zip(["y1", "y2"], problem.solution.get_dual_values())))
print(list(zip(col_names, problem.solution.get_values())))