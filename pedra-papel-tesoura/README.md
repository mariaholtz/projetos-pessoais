# ✂️ Pedra, Papel e Tesoura

## 📖 Sobre

Este projeto consiste em uma versão simples do clássico jogo **Pedra, Papel e Tesoura**, desenvolvido em Python.
O jogador disputa contra o computador, que realiza uma escolha aleatória entre as três opções disponíveis.

O projeto foi desenvolvido com o objetivo de praticar estruturas condicionais, entrada e saída de dados, manipulação de dicionários e geração de valores aleatórios utilizando a biblioteca `random`.

Além disso, foi utilizada a biblioteca `emoji` para tornar a experiência do jogo mais visual e interativa através da representação das escolhas com emojis.

---

## 🚀 Tecnologias

- Python 3

---

## 📚 Bibliotecas utilizadas

- **random** — utilizada para gerar a escolha aleatória do computador.
- **emoji** — utilizada para exibir as opções escolhidas através de emojis.

---

## 🧠 Conceitos praticados

- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`while`)
- Entrada e saída de dados (`input` e `print`)
- Manipulação de dicionários
- Variáveis de controle e contadores
- Geração de valores aleatórios
- Comparação de valores
- Formatação de strings (`f-strings`)

---

## 🎮 Como funciona

1. O usuário informa se deseja iniciar o jogo.
2. O jogador escolhe uma das opções:
   - Pedra (`p`)
   - Papel (`pl`)
   - Tesoura (`t`)
3. O computador realiza uma escolha aleatória.
4. O programa compara as escolhas e informa o resultado da rodada.
5. Ao final, o jogador recebe um placar com:
   - Vitórias
   - Derrotas
   - Empates

### Regras do jogo

| Jogador | Computador | Resultado |
| ------- | ---------- | --------- |
| Pedra   | Tesoura    | Vitória   |
| Papel   | Pedra      | Vitória   |
| Tesoura | Papel      | Vitória   |
| Pedra   | Papel      | Derrota   |
| Papel   | Tesoura    | Derrota   |
| Tesoura | Pedra      | Derrota   |
| Igual   | Igual      | Empate    |

---

## ▶️ Como executar

Antes de executar, instale a biblioteca necessária:

```bash
pip install emoji
```

Depois, execute o arquivo:

```bash
python pedra_papel_tesoura.py
```

---

## 💡 Exemplo de uso

```text
Quer jogar um jogo? (sim/nao) sim

Escolha entre pedra (p), papel (pl) e tesoura (t): p

Você escolheu 🧱
O computador escolheu ✂️
Você ganhou!

Quer jogar novamente? (sim/nao) sim

Escolha entre pedra (p), papel (pl) e tesoura (t): pl

Você escolheu 📜
O computador escolheu 🧱
Você ganhou!

Fim de jogo! Foi muito legal, nos vemos na próxima!

Você tem 2 vitórias, 0 derrotas e 0 empates.
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei lógica de programação através da criação de um jogo interativo, utilizando estruturas condicionais e de repetição.

Também explorei a geração de escolhas aleatórias com a biblioteca `random`, a organização de informações utilizando dicionários e a utilização de bibliotecas externas 
para melhorar a experiência do usuário.

---
