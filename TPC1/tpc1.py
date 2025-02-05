import sys

def process_input(data):

    linhas = data.splitlines()
    vista = set()
    linhas_unicas = []
    n_linhas_repetidas = 0 
    n_palavras_repetidas = 0 
    n_caracteres_repetidos = 0 
    for linha in linhas: 
        if linha not in vista: 
            vista.add(linha)
            linhas_unicas.append(linha)
        else: 
            n_linhas_repetidas += 1 
            n_palavras_repetidas += len(linha.split())
            n_caracteres_repetidos += len(linha)


    return "\n".join(linhas_unicas), n_linhas_repetidas,n_palavras_repetidas, n_caracteres_repetidos

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            print(f"Erro: O arquivo '{filename}' não foi encontrado.")
            sys.exit(1)
    else:
        print("Digite o texto (pressione Ctrl+D para finalizar):")
        data = sys.stdin.read()

    output, linhas_repetidas, palavras, caracteres = process_input(data)
    
    print("\nResultados:")
    print(output)
    print(f"\nLinhas Removidas: {linhas_repetidas}\nNumero de Palavras Removidas: {palavras}\nNumero Caracteres removidos: {caracteres}")

if __name__ == "__main__":
    main()
