# Analisador de Dados de Meteorologia

Este projeto permite analisar dados meteorológicos, como temperatura, umidade e pressão atmosférica, utilizando a biblioteca `Pandas` para processamento de dados e `Matplotlib`/`Seaborn` para visualização. O programa exibe gráficos para analisar a variação dessas variáveis ao longo do tempo e suas correlações.

## Funcionalidades

- Exibição de resumo estatístico dos dados.
- Gráficos de linha para variação de temperatura, umidade e pressão.
- Visualização de correlação entre as variáveis meteorológicas.

## Requisitos

- Python 3.x
- Bibliotecas: `pandas`, `matplotlib`, `seaborn`

## Como Usar

1. Clone o repositório:

```bash
   git clone https://github.com/LuiSilvak/weather_analyzer.git
   cd weather_analyzer
```

2. Instale as bibliotecas necessárias:

```bash
    pip install pandas matplotlib seaborn
```

3. Execute o programa:

```bash
    python weather_analyzer.py
```

4. O programa irá exibir os gráficos e o resumo estatístico.


## Exemplo de Execução
### Entrada:

```bash
    Resumo Estatístico dos Dados Meteorológicos:
            Temperatura    Umidade     Pressao
    count     10.000000   10.000000   10.000000
    mean      27.000000   60.000000  1013.300000
    std        4.105412    4.409803     2.000000
    min       21.000000   50.000000  1010.000000
    25%       23.000000   55.000000  1012.000000
    50%       26.000000   59.500000  1013.000000
    75%       30.000000   61.500000  1014.000000
    max       33.000000   65.000000  1016.000000
```

### Saída:

- Gráficos gerados de temperatura, umidade e pressão.
- Gráfico de correlação entre as variáveis.

## Melhorias Futuras

- Adicionar mais variáveis meteorológicas, como vento e radiação solar.
- Implementar análise de séries temporais.
- Integrar com APIs de dados meteorológicos reais.

## Licença

Este projeto está licenciado sob a MIT License.
