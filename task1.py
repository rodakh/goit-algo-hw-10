from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

model = LpProblem(name="optimal-production", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')

model += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint")
model += (1 * lemonade <= 50, "Sugar_Constraint")
model += (1 * lemonade <= 30, "Lemon_Juice_Constraint")
model += (2 * fruit_juice <= 40, "Fruit_Puree_Constraint")

model += lpSum([lemonade, fruit_juice])

status = model.solve()

print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Lemonade production: {lemonade.value()}")
print(f"Fruit Juice production: {fruit_juice.value()}")
