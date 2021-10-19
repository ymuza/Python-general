g = {
                'physicists': {'albert': '64258709',
                               'godfried': '3513875490',
                               'isaac': '296789456',
                               'alhazen': '696324512'},



                'mathematicians': {'carl': '523234553',
                                   'leonhard': '723235023',
                                   'david': '65734345'},

}

h = 'albert'
for n in g['physicists']:
    if h == n:
        print(g.popitem())





