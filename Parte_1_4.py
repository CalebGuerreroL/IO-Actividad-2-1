from cplex import Cplex, infinity
from cplex.exceptions import CplexError

# Angle Caleb Guerrero Luna
# Mario Eduardo Lara Loredo

problem = Cplex()

problem.objective.set_sense(problem.objective.sense.minimize)

constraints_matrix = [
  [1.0, 1.0, 2.0, 1.0, 3.0],
  [2.0, -1.0, 3.0, 1.0, 1.0]
]

col_names = ["x1", "x2", "x3", "x4", "x5"]

constraints = []

for i in constraints_matrix:
  new_item = [col_names]
  new_item.append(i)
  constraints.append(new_item)

problem.variables.add(
  obj = [2.0, 3.0, 5.0, 2.0, 3.0],
  names =  col_names
)

problem.linear_constraints.add(
  lin_expr = constraints,
  senses = ["G", "G"],
  rhs = [4.0, 3.0],
  names = ["c1", "c2"]
)

problem.solve()

print(f"Objective value: {problem.solution.get_objective_value()}")
print(list(zip(col_names, problem.solution.get_values())))