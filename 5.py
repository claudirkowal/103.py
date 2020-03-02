palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

testador=palindrome_one.lower()
testador=testador.replace(' ','')
inverter=testador[::-1]
if inverter==testador:
    print(inverter, 'é uma Palindrome')
else:
    print('Não é Palindrome')

testador = palindrome_two.lower()
testador = testador.replace(' ', '')
inverter = testador[::-1]
if inverter == testador:
    print(inverter, 'é uma Palindrome')
else:
    print('Não é Palindrome')

testador=palindrome_three.lower()
testador=testador.replace(' ','')
inverter=testador[::-1]
if inverter==testador:
    print(inverter, 'é uma Palindrome')
else:
    print('Não é Palindrome')

testador=palindrome_four.lower()
testador=testador.replace(' ','')
inverter=testador[::-1]
if inverter==testador:
    print(inverter, 'é uma Palindrome')
else:
    print(testador,'não é Palindrome')