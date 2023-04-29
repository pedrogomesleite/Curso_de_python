salario = float(input('salário:'))
emp = float(input('emprestimo:'))
if emp > salario*0.2:
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')
