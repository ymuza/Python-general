print("ingrese 5 notas")
suma = 0
for f in range(5):
    nota = float(input())
    suma = suma + nota

promedio = suma / 5
print("El promedio es:")
print(promedio)

# ------------------------------------
print("\n")

print("ingresar cantidad de hombres : ")
ch = float(input())

print("ingresar cantidad de mujeres : ")
cm = float(input())

total_alumnos = cm + ch

porcentaje_hombres = ch * 100 / total_alumnos
porcentaje_mujeres = cm * 100 / total_alumnos

print(f"la cantidad de alumnos es {total_alumnos}")
print("\n")
print(f"el porcentaje de mujeres es es del {porcentaje_mujeres}% ")
print("\n")
print(f"el porcentaje de hombres es del {porcentaje_hombres}% ")
