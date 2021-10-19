my_dictionary1 = {'name': 'yamil', 'course': 'python', 'hours': '14'}

phone_book = {'albert': '4258709',
              'godfried': '3513875490',
              'isaac': '296789456',
              'alhazen': '696324512'}

phone_book2 = {
                'physicists': {'albert': '64258709',
                               'godfried': '3513875490',
                               'isaac': '296789456',
                               'alhazen': '696324512'},



                'mathematicians': {'carl': '523234553',
                                   'leonhard': '723235023',
                                   'david': '65734345'},
}


print(my_dictionary1['course']) #imprime el dato del elemento 'course', en este caso 'python'
print("\n")
print(phone_book['alhazen'])
print("\n")
print(phone_book2['mathematicians']['david'])
print("\n")
print(phone_book2.get('mathematicians'))  #trae los valores de 'mathematicians' con el 'get'
