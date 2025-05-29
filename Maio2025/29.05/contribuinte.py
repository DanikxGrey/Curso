salario_contribuinte = float(input("Digite o salário: "))

if salario_contribuinte <= 1692.72:
    contribuicao_inss = salario_contribuinte * 0.08
    
elif salario_contribuinte >= 1692.75 and salario_contribuinte <= 2822.90:
    contribuicao_inss = salario_contribuinte * 0.09
    
elif salario_contribuinte >= 2822.90 and salario_contribuinte <= 5645.90:
    contribuicao_inss = salario_contribuinte * 0.11

salario_liquido = salario_contribuinte - contribuicao_inss

print (f"A contribuição do INSS: R${contribuicao_inss:.2f} ")
print (f"O salário bruto é: {salario_contribuinte:.2f}")
print (f"O salário líquido é {salario_liquido:.2f}")
