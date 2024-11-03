# Projeto de Algoritmos de Troca de Páginas

Este projeto implementa três algoritmos de troca de páginas para sistemas operacionais: FIFO, Optimal e LRU.

## Requisitos

- Python 3.x instalado.

## Como Executar

Cada algoritmo possui um script específico:

- FIFO: `python fifo.py <page_frames> <page_sequence>`
- Optimal: `python optimal.py <page_frames> <page_sequence>`
- LRU: `python lru.py <page_frames> <page_sequence>`

### Parâmetros

- `<page_frames>`: Número de quadros de página (exemplo: 3).
- `<page_sequence>`: Sequência de páginas, separadas por vírgula (exemplo: 1,3,5,4,2,4,2,3,2).

### Exemplo

Para executar o algoritmo FIFO com 3 quadros de página e sequência `1,3,5,4,2,4,2,3,2`:
