def main():
    vetor = []

    while True:
        try:
            comando = input().strip()

            if comando == 'sair':
                break

            elif comando.startswith('insere'):
                _, valor = comando.split()
                vetor.append(int(valor))
                print(vetor)

            elif comando.startswith('troca'):
                _, i, j = comando.split()
                i, j = int(i), int(j)
                vetor[i], vetor[j] = vetor[j], vetor[i]
                print(vetor)

            elif comando.startswith('remove'):
                _, i = comando.split()
                i = int(i)
                del vetor[i]
                print(vetor)

            elif comando.startswith('presente'):
                _, valor = comando.split()
                valor = int(valor)
                if valor in vetor:
                    print(f'Valor {valor} esta presente no vetor')
                else:
                    print(f'Valor {valor} esta ausente no vetor')

        except Exception:
            continue

if __name__ == '__main__':
    main()
