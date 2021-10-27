print("Introduza a nota do teste 1.")
t1=float(input())
print("Introduza a nota do teste 2.")
t2=float(input())
print("Introduza a nota do teste 3")
t3= float(input())
print("Introduza a nota do teste 4")
t4= float(input())
medTestes=(t1+t2+t3+t4)/4
if (medTestes>=10):
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")