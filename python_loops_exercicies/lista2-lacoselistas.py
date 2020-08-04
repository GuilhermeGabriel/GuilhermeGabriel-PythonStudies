import random
import datetime
from math import sqrt


# input_value = int(input('Digite o número de termos: '))
# 01 Série de fibonacci
def fib(n):
    fib_list = []
    atual = 1
    anterior = 1

    while n > 0:
        fib_list.append(anterior)
        atual, anterior = atual + anterior, atual
        n = n - 1

    return fib_list


# print(fib(input_value))

# fibonacci recursivo
def fibo(n):
    return fiboaux(n, 1, 1)


def fiboaux(n, a, b):
    if n == 0:
        return a
    else:
        return fiboaux(n - 1, a + b, a)


# print(fibo(input_value))


# 02
def fib_value_500():
    fib_list = [1]
    atual = 1
    anterior = 0

    while atual < 500:
        novo = atual + anterior
        fib_list.append(novo)

        anterior = atual
        atual = novo

    return fib_list


# print(fib_value_500())


# 03
def is_primo(v):
    dv_list = []
    for i in range(v):
        if v % (i + 1) == 0:
            dv_list.append(i)
    return len(dv_list) == 2


# print(is_primo(31))

def is_p(n):
    return nr_div(n) == 2


def nr_div(n):
    div = 2

    if n == 1:
        return 1
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            if i == sqrt(n):
                div += 1
            else:
                div += 2
    return div


# print(is_p(17))


# 04


def number_invert(n):
    ls = str(n)
    inv = list(reversed(ls))
    return int(''.join(inv))


# print(number_invert(1589))


# print(number_invert(5))


# 05
def serie1(n):
    base = 1
    itens = []
    sum = 0
    for i in range(0, n):
        itens.append(str(i + 1) + '/' + str(base))
        itens.append(' + ')
        sum += (i + 1) / base
        base += 2

    itens.pop(len(itens) - 1)
    itens.append(' = ' + str(sum))

    return ''.join(map(str, itens))


# print(serie1(15))

# 06
def par_impar(list_number):
    list_par = []
    list_impar = []

    for item in list_number:
        if item % 2 == 0:
            list_par.append(item)
        else:
            list_impar.append(item)

    return list_par, list_impar


# print(par_impar([1, 2, 3, 4, 5, 6, 7, 8]))


# 07
def quadrado_list(list_number):
    return list(map(lambda x: x * x, list_number))


# print(quadrado_list([1, 2, 3, 4, 5, 6, 7, 8]))

# 08
def intercala_listas(l1, l2):
    if len(l1) != len(l2):
        return 'Error, listas de tamanho diferente'

    lr = []
    for i in range(len(l1)):
        lr.append(l1[i])
        lr.append(l2[i])
    return lr


# print(intercala_listas([1, 2, 3, 4], [4, 5, 6, 7]))

# 09
def lanca_dados(n):
    lr = []

    random.seed(datetime.datetime.now().timestamp())

    for i in range(n):
        lr.append(random.randint(1, 6))
    return lr


# print(lanca_dados(10))

# 10
def triangle1(n):
    for i in range(n):
        print((str(i + 1) + ' ') * (i + 1))
    return True


# print(triangle1(5))


# 11
def triangle2(n):
    for i in range(n):
        for j in range(i + 1):
            print(str(j + 1) + ' ', end='')
        print('')


# print(triangle2(33))

# 12
def quadrados_magicos(n):
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # gera_lista(n)
    q = permutations(l)
    r = []
    for quad in q:
        if is_list_magic(quad):
            r.append(quad)
    return r


def permutations(l):
    if not l:
        return [[]]
    res = []
    for e in l:
        temp = l[:]
        temp.remove(e)
        res.extend([[e] + r for r in permutations(temp)])
    return res


def is_list_magic(l):
    l1 = l[0] + l[1] + l[2]
    l2 = l[3] + l[4] + l[5]
    l3 = l[6] + l[7] + l[8]

    c1 = l[0] + l[3] + l[6]
    c2 = l[1] + l[4] + l[7]
    c3 = l[2] + l[5] + l[8]

    d1 = l[0] + l[4] + l[8]
    d2 = l[2] + l[4] + l[6]

    return l1 == l2 == l3 == c1 == c2 == c3 == d1 == d2


print(quadrados_magicos(9))


# 13
def quant_alg(n):
    return len(str(n))


# print(quant_alg(123456))


# 14
def getMes(param):
    meses = ['janeiro', 'fevereiro', 'março', 'abril',
             'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
             'novembro', 'dezembro']

    m_s_index = int(''.join(map(str, param))) - 1

    return meses[m_s_index]


def data_extenso(s):
    l_s = list(s)
    if len(l_s) != 10 or l_s[2] != '/' or l_s[5] != '/':
        return 'Error, entrada inválida'
    else:
        return ''.join(map(str, l_s[0:2])) + \
               ' de ' + getMes(l_s[3:5]) + \
               ' de ' + \
               ''.join(map(str, l_s[6:11]))


# print(data_extenso('01/08/2000'))


# 15
def n_empty_n_vogais(s):
    n_e = 0
    n_v = 0
    for i in range(len(s)):
        if s[i] == ' ':
            n_e += 1
        elif s[i] in ['a', 'e', 'i', 'o', 'u']:
            n_v += 1
    return n_e, n_v


# print(n_empty_n_vogais('asdfae1 sdfafsadf   '))

# 16

def isPalindrome(s):
    st_joined = ''.join(s.split())
    st_inverted = ''.join(list(reversed(st_joined)))
    return st_joined == st_inverted


# print(isPalindrome('subi no onibus'))

# 17
def get_digit_1(cpf_l):
    s1 = 0
    r1 = 0
    mult_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    for i in range(len(cpf_l)):
        s1 += int(cpf_l[i]) * mult_1[i]

    r1 = s1 % 11

    if r1 < 2:
        d1 = 0
    else:
        d1 = 11 - r1

    return d1


def get_digit_2(cpf_l):
    mult_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    cpf_l = list(cpf_l)
    s2 = 0
    r2 = 0

    for i in range(len(cpf_l)):
        s2 += int(cpf_l[i]) * mult_2[i]

    r2 = s2 % 11

    if r2 < 2:
        d2 = 0
    else:
        d2 = 11 - r2

    return d2


def is_valid_cpf(cpf):
    cpf_r = []
    for s in cpf:
        if s.isdigit():
            cpf_r.append(s)

    d1 = get_digit_1(cpf_r[0:9])

    cpf_aux = cpf_r.copy()
    cpf_aux.append(d1)
    d2 = get_digit_2(cpf_aux[0:10])

    return cpf_r[9:11] == [str(d1), str(d2)]


# print(is_valid_cpf('111.444.777-35'))

# 18
def n_extenso(n):
    un = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    de = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'secenta', 'setenta', 'oitenta', 'novento']
    ce = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos',
          'novecentos']

    n_l = list(str(n))
    if len(n_l) == 1:
        return un[int(n_l[0])]
    elif len(n_l) == 2:
        return de[int(n_l[0]) - 1] + ' e ' + un[int(n_l[1])]
    else:
        return ce[int(n_l[0]) - 1] + ' e ' + de[int(n_l[1]) - 1] + ' e ' + un[int(n_l[2])]


# print(n_extenso(756))


# 19


def valid_ips(s):
    arr_ips = s.split()
    l_v = []
    l_inv = []

    for i in range(len(arr_ips)):
        valid = True
        ip = arr_ips[i].split(' ')
        numbers = ip[0].split('.')

        # print(numbers)

        for j in range(len(numbers)):
            # print(int(numbers[j]))
            if int(numbers[j]) > 255:
                valid = False

        if valid:
            l_v.append(ip)
        else:
            l_inv.append(ip)

    return 'Enderecos válidos: ' + str(l_v) + '\n' + 'Endereços inválidos: ' + str(l_inv)

# print(valid_ips("200.135.80.9 192.168.1.1 8.35.67.74 257.32.4.5 85.345.1.2 1.2.3.4 9.8.234.5 192.168.0.256"))


# 20
def get_percent_use(bytes):
    t_s = 2468645000
    return (bytes / t_s) * 100


def bytes_megabytes(bytes):
    return bytes / 1000000


def gera_rel():
    es_ocup = 0
    es_m_ocup = 0
    n_usuarios = 0
    fi = open("arquivo.txt", "r")
    fo = open("relatorio.txt", "w")
    lines = fi.readlines()

    s_r = "Nr.   Usuario      Espaco utilizado    % do uso"

    for i in range(len(lines)):
        b_used = int(lines[i].split(" ")[1])

        s_r += '\n' + str(i + 1) + "     " + lines[i].split(" ")[0] + \
               "       " + str(round(bytes_megabytes(b_used), 2)) + " MB" + \
               "       " + str(round(get_percent_use(b_used), 2)) + "%"
        es_ocup += b_used
        n_usuarios += 1

    s_r += "\n\nEspaco total ocupado: " + str(round(bytes_megabytes(es_ocup), 2)) + " MB" \
                                                                                    "\nEspaco medio ocupado: " + str(
        round(bytes_megabytes(es_ocup) / n_usuarios, 2)) + " MB"
    fo.write(s_r)


# gera_rel()

