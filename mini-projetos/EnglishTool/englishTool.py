import json
import random

# Carregar ou criar arquivo JSON de vocabulário
def load_vocabulary():
    try:
        with open('vocabulary.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_vocabulary(vocab):
    with open('vocabulary.json', 'w') as f:
        json.dump(vocab, f, indent=4)

# Adicionar nova palavra
def add_word(vocab):
    word = input("Digite a palavra em inglês: ").strip().lower()
    meaning = input("Digite o significado ou exemplo da palavra: ").strip()
    vocab[word] = meaning
    print(f"'{word}' foi adicionada com sucesso!")
    save_vocabulary(vocab)

# Revisar vocabulário
def review_words(vocab):
    if not vocab:
        print("Nenhuma palavra para revisar.")
    else:
        print("\n--- Seu Vocabulário ---")
        for word, meaning in vocab.items():
            print(f"{word}: {meaning}")
        print("\n")

# Teste rápido
def quiz(vocab):
    if not vocab:
        print("Nenhuma palavra no vocabulário para testar.")
    else:
        word = random.choice(list(vocab.keys()))
        answer = input(f"O que significa '{word}'? ").strip().lower()
        if answer == vocab[word].lower():
            print("Correto!")
        else:
            print(f"Errado! O significado correto é: {vocab[word]}")

# Menu principal
def main():
    vocab = load_vocabulary()
    
    while True:
        print("\n1. Adicionar nova palavra")
        print("\n2. Revisar vocabulário")
        print("\n3. Fazer um teste rápido")
        print("\n4. Sair")
        
        choice = input("\nEscolha uma opção: ")
        
        if choice == '1':
            add_word(vocab)
        elif choice == '2':
            review_words(vocab)
        elif choice == '3':
            quiz(vocab)
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
