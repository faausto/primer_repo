# quiz_git.py - Quiz sobre Git
print("=== Quiz de Git ===\n")
score = 0
r1 = input("1. ¿Git es una herramienta local o en la nube? ")
if r1.lower() == "local":
print("✅ ¡Correcto!")
score += 1
else:
print("❌ Incorrecto. Git es una herramienta LOCAL.")
r2 = input("\n2. ¿Qué comando sube los cambios a GitHub? (git ___) ")
if r2.lower() == "push":
print("✅ ¡Correcto!")
score += 1
else:
print("❌ Incorrecto. El comando es 'push'.")
r3 = input("\n3. ¿Qué comando prepara archivos para el commit? (git ___) ")
if r3.lower() == "add":
print("✅ ¡Correcto!")
score += 1
else:
print("❌ Incorrecto. El comando es 'add'.")
print(f"\n🏆 Resultado: {score}/3")
if score == 3:
print("¡Excelente! Dominás los conceptos básicos de Git.")
elif score >= 2:
print("¡Muy bien! Seguí practicando.")
else:
print("Repasá los conceptos y volvé a intentar.")