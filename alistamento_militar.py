import datetime
from time import sleep
from emoji import emojize
e = emojize(':arrow_forward:', use_aliases=True)
e1 = emojize(':fast_forward:', use_aliases=True)
e3 = emojize(':black_small_square:', use_aliases=True)
em = emojize(':boy:', use_aliases=True)
ef = emojize(':girl:', use_aliases=True)
esim = emojize(':heavy_check_mark:', use_aliases=True)
enao = emojize(':x:', use_aliases=True)
at = datetime.date.today().year
wi = 'ALISTAMENTO MILITAR'
print('\033[1;30m=' * 50)
print(f'{wi:^50}')
print('=' * 50)
n = str(input(f'\033[1;35m{e} Digite o seu nome completo: ')).strip().title()
print('')
print(f'\033[1;30mOlá, {n.split()[0]} {n.split()[-1]}!\033[m')
print('')
a = int(input(f'\033[1;35m{e} Digite o ano do seu nascimento: '))
s = str(input(f'''{e} Nos informe seu sexo digitando 1 ou 2:
\033[1;34m[1] Masculino {em} \n\033[1;33m[2] Feminino {ef}
\033[1;35m{e} Sua escolha: '''))
print('')
i = at - a
fri = mi = z = x = c = r = cor = cor1 = g = ge = ''
if s == '1' or s == '2':
    if s == '2':
        print(f'\033[1;30mOlá novamente, {n.split()[0]} {n.split()[-1]}!\033[m')
        print('')
        r = str(input(f'''\033[1;35m{e} Seu alistamento não é obrigatório. Deseja se alistar mesmo assim?
\033[1;32m[1] Sim {esim}
\033[1;31m[2] Não {enao}
\033[1;35m{e} Sua escolha: '''))
        print('')
    if s == '1' or r == '1':
        if i == 18:
            fri = f'\033[1;33m{e3} Você está no ano de alistamento!\033[m'
            mi = f'\033[1;33m{e3} Você precisa se alistar imediatamente.\033[m'
            cor = '\033[1;33m'
        elif i > 18:
            z = i - 18
            c = at - z
            if z > 1:
                x = 'anos'
            else:
                x = 'ano'
            fri = f'\033[1;31m{e3} Você passou do ano de alistamento!\033[m'
            mi = f'\033[1;31m{e3} Você deveria ter se alistado no ano de {c} a {z} {x} atrás.\033[m'
            cor = '\033[1;31m'
        elif i < 18:
            z = 18 - i
            c = at + z
            if z > 1:
                x = 'anos'
            else:
                x = 'ano'
            fri = f'\033[1;32m{e3} Você ainda irá se alistar para o serviço militar.\033[m'
            mi = f'\033[1;32m{e3} Faltam {z} {x} para o seu alistamento em {c}.\033[m'
            cor = '\033[1;32m'
        if s == '1':
            cor1 = '\033[1;34m'
            ge = 'Masculino'
            g = em
        elif s == '2':
            cor1 = '\033[1;33m'
            ge = 'Feminino'
            g = ef
        print('\033[1;30mAnalisando...\033[m')
        sleep(1.7)
        print('')
        print('\033[1;30m¨' * 70)
        print(f'{e1} Nome Completo: {n}')
        print(f'{e1} Gênero: {cor1}{ge} {g}\033[m')
        print(f'\033[1;30m{e1} Idade: {cor}{i} anos\033[m')
        print('')
        print(f'{fri}')
        print(f'{mi}')
        print('\033[1;30m¨' * 70)
    elif r == '2':
        print('')
        print('\033[1;30mEncerrando...\033[m')
        sleep(1.2)
        print('')
        print('\033[1;32mCadastro do serviço militar obrigatório encerrado com sucesso!\033[m')
    elif r != '1' or r != '2':
        print('\033[1;31mDado inválido, tente novamente.\033[m')
else:
    print('\033[1;31mDado inválido, tente novamente.\033[m')
