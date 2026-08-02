# 🔐 Gerador de Senhas Aleatórias

## 📖 Sobre

Este projeto consiste em um gerador de senhas aleatórias desenvolvido em Python. O usuário pode personalizar o nível de complexidade da senha (fraca, média ou forte) e 
definir a quantidade de caracteres desejada.

O projeto foi desenvolvido com o objetivo de praticar manipulação de strings, geração de caracteres aleatórios e criação de funções, além de explorar a biblioteca `secrets`, 
recomendada para geração de senhas seguras.

---

## 🚀 Tecnologias

- Python 3

---

## 📚 Bibliotecas utilizadas

- **string** — fornece conjuntos de caracteres, como letras, números e símbolos.
- **secrets** — utilizada para gerar caracteres aleatórios de forma criptograficamente segura.

---

## 🧠 Conceitos praticados

- Funções
- Estruturas condicionais (`if`, `elif`, `else`)
- Manipulação de strings
- Entrada e saída de dados (`input` e `print`)
- Geração de números aleatórios seguros
- Concatenação de caracteres
- Compreensão de listas (Generator Expression)

---

## 🎮 Como funciona

1. O usuário escolhe o nível de segurança da senha:
   - Fraca
   - Média
   - Forte
2. Informa a quantidade de caracteres desejada.
3. O programa gera uma senha aleatória de acordo com os critérios selecionados.

### Critérios de geração

| Nível | Caracteres utilizados |
|-------|-----------------------|
| Fraca | Letras maiúsculas e minúsculas |
| Média | Letras e números |
| Forte | Letras, números e símbolos |

---

## ▶️ Como executar

```bash
python gerador_senhas.py
```

---

## 💡 Exemplo de uso

```text
Olá! Seja bem-vindo ao gerador de senhas aleatórias!

Por favor, informe quão forte você quer que a senha seja (forte, media ou fraca): forte

Por favor, informe o tamanho que você deseja para sua senha: 16

Sua nova senha é: K$7w!aP9#Lm2@QxR
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei a criação de funções, manipulação de strings, estruturas condicionais e geração de caracteres aleatórios. 
Também conheci a biblioteca `secrets`, utilizada para criar senhas de forma mais segura do que métodos tradicionais de geração aleatória.

---

## 🔄 Possíveis melhorias

- [ ] Garantir que senhas fortes contenham obrigatoriamente pelo menos uma letra, um número e um símbolo.
- [ ] Validar as entradas do usuário.
- [ ] Permitir gerar múltiplas senhas em uma única execução.
- [ ] Copiar automaticamente a senha para a área de transferência.
- [ ] Criar uma interface gráfica utilizando Tkinter ou CustomTkinter.

---
