# 4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
# • Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
# • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
# • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Os três primeiros itens da lista são: ")
for player in players[:3]:
    print(player.title() + ".")

print("Os três itens do meio da lista são: ")
for player in players[2:]:
    print(player.title() +".")

print("Os três últimos itens da lista são:")
for player in players[-3:]:
    print(player.title() + ".")