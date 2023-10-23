
print ('Vamos olhar seu peso?')

Nome = input('Seu nome é?: ')
Peso =float(input('Seu peso é?: '))
Altura =float( input('Sua altura é?: '))
total = Peso/Altura

if ( total > 24.99):
    print ( 'Olá ' ,Nome, ' seu IMC é %.2f .Cuidado você esá acima do peso.' %total)
else:
    print(' Olá' ,Nome, 'seu IMC é %.2f .Parabéns você está dentro do peso ideal.' %total) 


