""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem da
colocação. Depois mostre: 1)Apenas os 5 primeiros colocados, 2)Os últimos 4 colocados, 3)Uma lista com os times em ordem
alfabética, 4)Em que posição na tabela está o time da Chapecoense (no momento série b, trocando para Cruzeiro)"""

times = ('Fortaleza', 'Botafogo', 'Palmeiras', 'Flamengo', 'São Paulo', 'Bahia', 'Cruzeiro', 'Vasco da Gama',
         'Atlético-MG', 'Athletico-PR', 'Internacional', 'Criciúma', 'Juventude', 'Grêmio', 'Bragantino', 'Fluminense',
         'EC Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO')

print(f'Lista de times do Brasileirão 2024: {times}')
print('=' * 40)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('=' * 40)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('=' * 40)
print(f'Times em ordem alfabética{sorted(times)}')
print('=' * 40)
print(f'O Cruzeiro está na {times.index("Cruzeiro") + 1}° posição')
