names: list[str] = ["David", "Peter", "Natalia"]
salaries: list[int] = [1000, 2000, 1500]
bonuses: list[str] = ["10.5%", "1.5%", "21.5%"]

print({name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salaries, bonuses)})
