from funcoes import *

while True: 
    os.system('cls')
    print("\nACERTE A PALAVRA DE 5 LETRAS EM 5 TENTATIVAS\n")
    print_chutes()
    print(f"Tentativas restantes: {tentativas_max-tentativa_inicio+1}")
    for t in teclado(): print(t, end="  ")
    print("\n")

    i = input_do_jogador()
    chutes.append(i)

    if i == palavra_sorteada:
        os.system('cls')
        print("\nACERTE A PALAVRA DE 5 LETRAS EM 5 TENTATIVAS\n")
        print_chutes()
        for t in teclado(): print(t, end="  ")
        print("\n")
        print(f"{colors.GREEN}PARABÉNS{colors.END}")
        print(f"Acertou '{i}' em {tentativa_inicio} tentativas\n")
        break

    if tentativa_inicio==tentativas_max:
        os.system('cls')
        print("\nACERTE A PALAVRA DE 5 LETRAS EM 5 TENTATIVAS\n")
        print_chutes()
        for t in teclado(): print(t, end="  ")
        print("\n")
        print(f"{colors.FAIL}FIM{colors.END}")
        print(f"Palavra correta: '{palavra_sorteada}'\n")
        break

    tentativa_inicio+=1
