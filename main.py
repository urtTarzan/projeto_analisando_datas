from datetime import datetime
from dateutil.relativedelta import relativedelta

#Calculadora de idade completa exercicio 2

def formatar_idade(anos, mes, dias):
    partes = []

    if anos > 0:
        partes.append(f"{anos} ano{'s' if anos > 1 else ''}")
    if mes > 0:
        partes.append(f"{mes} mes{'es' if mes > 1 else ''}")
    if dias > 0:
        partes.append(f"{dias} dia{'s' if dias > 1 else ''}")

    if not partes:
        return '0 dias'
    
    return ", ".join(partes)


def obter_data_nascimento():
    try:
        nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
        nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")
        return nascimento
    except ValueError:
        print("Data inválida. Use o formato dd/mm/aaaa.")
        return None

#lista dias da semana
dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"] 


nascimento = obter_data_nascimento()
if nascimento is None:
    exit()  # Encerra o programa se a data for inválida

#idade exata
hoje = datetime.now()
idade_completa = relativedelta(hoje, nascimento)
diferença = (hoje - nascimento)
idade_int = idade_completa.years

#aniversario e datas
proximo_aniversario = nascimento.replace(year= hoje.year)
if proximo_aniversario < hoje:
    proximo_aniversario = nascimento.replace(year= hoje.year + 1)
tempo_exato_faltando_aniversario = (proximo_aniversario - hoje).days



print("IDADE")
print(f"voce nasceu em {nascimento.day}, mes {nascimento.month} de {nascimento.year}")
print(f"o dia da semana que voce nasceu foi {dias_da_semana[nascimento.weekday()]}")
print(f"voce tem exatamente {formatar_idade(idade_completa.years, idade_completa.months, idade_completa.days)} de vida")
print("ANIVERSARIO  ")
print(f"seu proximo aniversario sera em {proximo_aniversario.strftime('%d/%m/%Y')}")
print(f"faltam exatos {tempo_exato_faltando_aniversario} dias para seu aniversario")
if proximo_aniversario.date == hoje.date():
    print("PARABENS SEU ANIVERSARIO É HOJEEEEEEE!")

