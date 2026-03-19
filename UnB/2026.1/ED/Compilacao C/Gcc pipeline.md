# Compilação C com GCC — pipeline completo

Este guia cobre cada fase da compilação de um programa C no Linux, do código fonte até o binário executável, e como inspecionar o que acontece em cada etapa.

---

## Pré-requisitos

Você precisa ter instalado:

- `gcc` — compilador
- `objdump` — inspetor de binários (geralmente já vem com o gcc)
- `nm` — leitor de tabela de símbolos

Para instalar no Ubuntu/Debian:

```bash
sudo apt install gcc binutils
```

---

## Visão geral do pipeline

```
programa.c
    │
    ▼
[Pré-processamento]  →  programa.i   (C expandido, sem diretivas)
    │
    ▼
[Compilação]         →  programa.s   (assembly x86-64)
    │
    ▼
[Montagem]           →  programa.o   (código de máquina, ainda incompleto)
    │
    ▼
[Ligação]            →  programa     (executável final)
```

---

## Etapa 1 — Pré-processamento

```bash
gcc -E programa.c -o programa.i
```

O que acontece: o pré-processador expande todos os `#include`, `#define` e macros. O resultado é um arquivo `.i` com C puro, sem nenhuma diretiva. Tudo que estava nos headers (como `stdio.h`) é colado literalmente no arquivo — por isso o `.i` costuma ter centenas ou milhares de linhas mesmo para programas pequenos.

O arquivo `.i` é a entrada real do compilador. Ele lê tudo para entender tipos, assinaturas de funções e macros, mas só gera código para o que você implementou.

---

## Etapa 2 — Compilação para assembly

```bash
gcc -S programa.c -O0 -o programa.s
```

O que acontece: o compilador transforma o C em assembly x86-64. O arquivo `.s` é texto legível com as instruções reais que o processador vai executar.

A flag `-O0` desativa otimizações, o que gera um assembly mais verboso e fácil de ler. Em produção usa-se `-O2` ou `-O3`.

Para comparar o efeito das otimizações:

```bash
gcc -S programa.c -O0 -o programa_O0.s
gcc -S programa.c -O3 -o programa_O3.s
diff programa_O0.s programa_O3.s
```

---

## Etapa 3 — Montagem (assembly para objeto)

```bash
gcc -c programa.c -o programa.o
```

O que acontece: o assembler transforma o `.s` em código de máquina binário, gerando um arquivo `.o`. Esse arquivo ainda não é executável — referências externas como `printf` estão marcadas como indefinidas e serão resolvidas na próxima etapa.

Para ver a tabela de símbolos do `.o`:

```bash
nm --format=posix programa.o
```

Os tipos mais comuns na saída são `T` (função definida), `U` (símbolo externo indefinido) e `D` (variável global).

---

## Etapa 4 — Ligação (link)

```bash
gcc programa.o -o programa
```

O que acontece: o linker junta seu `.o` com as bibliotecas do sistema (como a libc, que contém `printf`) e resolve todas as referências externas. O resultado é o executável final.

Para executar:

```bash
./programa
```

---

## Compilar e executar em um único comando

O GCC não tem um modo que compila e executa ao mesmo tempo, mas você pode encadear os dois com `&&`:

```bash
gcc programa.c -o programa && ./programa
```

O `&&` garante que o programa só executa se a compilação for bem-sucedida.

---

## Inspecionar o executável — listagem com opcodes

Para ver o assembly gerado junto com os opcodes hexadecimais (equivalente ao listfile do HLASM):

```bash
gcc -g -O0 programa.c -o programa
objdump -d -S -M intel programa
```

Flags utilizadas:

- `-g` — inclui informações de debug no binário (necessário para intercalar o código C)
- `-d` — desmonta as seções de código
- `-S` — intercala o código-fonte C com o assembly
- `-M intel` — usa sintaxe Intel (destino primeiro), em vez da sintaxe AT&T padrão do Linux

A saída mostra, para cada instrução: o endereço de memória, o opcode em hexadecimal e o mnemônico assembly.

---

## Salvar a listagem em arquivo

```bash
objdump -d -S -M intel programa > programa.lst
```

A extensão `.lst` é convencional para listfiles, por analogia com HLASM e outros montadores.

Para ver no terminal e salvar ao mesmo tempo:

```bash
objdump -d -S -M intel programa | tee programa.lst
```

---

## Flags úteis do GCC

| Flag | Efeito |
|---|---|
| `-O0` | sem otimizações (padrão, melhor para debug) |
| `-O1` | otimizações básicas |
| `-O2` | otimizações moderadas (padrão em produção) |
| `-O3` | otimizações agressivas |
| `-g` | inclui informações de debug (necessário para gdb e objdump -S) |
| `-Wall` | ativa todos os warnings |
| `-S` | para na etapa de assembly, gera `.s` |
| `-E` | para na etapa de pré-processamento, gera `.i` |
| `-c` | para na etapa de montagem, gera `.o` |

---

## Registradores principais x86-64

Os registradores de uso geral seguem a convenção System V AMD64 para passagem de argumentos:

| Registrador | Uso na chamada de função |
|---|---|
| `RDI` | 1º argumento |
| `RSI` | 2º argumento |
| `RDX` | 3º argumento |
| `RCX` | 4º argumento |
| `R8` | 5º argumento |
| `R9` | 6º argumento |
| `RAX` | valor de retorno |
| `RSP` | topo da pilha |
| `RBP` | base do stack frame |
| `RIP` | próxima instrução a executar |

A partir do 7º argumento, os valores vão para a pilha.

Os sufixos dos nomes indicam o tamanho acessado: `R` = 64 bits, `E` = 32 bits, sem prefixo = 16 bits, `L`/`H` = 8 bits. Por exemplo, `RAX`, `EAX`, `AX` e `AL` são o mesmo registrador físico, acessado em tamanhos diferentes.

---

## Referência rápida — sequência completa

```bash
gcc -E  programa.c -o programa.i          # pré-processar
gcc -S  programa.c -O0 -o programa.s      # gerar assembly
gcc -c  programa.c -o programa.o          # montar para objeto
gcc     programa.o -o programa            # linkar
./programa                                # executar

objdump -d -S -M intel programa > programa.lst   # gerar listagem com opcodes
```