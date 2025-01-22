# Analisador de Dados de Meteorologia

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalisadorMeteorologia:
    def __init__(self, dados):
        self.dados = pd.DataFrame(dados)

    def resumo_dos_dados(self):
        """Exibe o resumo estatístico dos dados meteorológicos."""
        return self.dados.describe()
    
    def grafico_temperatura(self):
        """Plota um gráfico de linha da temperatura ao longo do tempo."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.dados['Data'], self.dados['Temperatura'], marker='o', color='tab:red', label='Temperatura (ºC)')
        plt.xlabel('Data')
        plt.ylabel('Temperatura (ºC)')
        plt.title('Variação de Temperatura ao Longo do Tempo')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def grafico_umidade(self):
        """Plota um gráfico de linha da umidade ao longo do tempo."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.dados['Data'], self.dados['Umidade'], marker='o', color='tab:blue', label='Umidade (%)')
        plt.xlabel('Data')
        plt.ylabel('Umidade (%)')
        plt.title('Variação de Umidade ao Longo do Tempo')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def grafico_pressao(self):
        """Plota um gráfico de linha da pressão ao longo do tempo."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.dados['Data'], self.dados['Pressão'], marker='o', color='tab:green', label='Pressão (hPa)')
        plt.xlabel('Data')
        plt.ylabel('Pressão (hPa)')
        plt.title('Variação de Pressão ao Longo do Tempo')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def correlacao(self):
        """Exibe a matriz de correlação entre as variáveis meteorológicas."""
        cor = self.dados[['Temperatura', 'Umidade', 'Pressão']].corr()
        sns.heatmap(cor, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlação entre Temperatura, Umidade e Pressão')
        plt.show()

def main():
    # Simulação de dados meteorológicos
    dados = {
        'Data': pd.date_range(start='2022-01-01', periods=10, freq='D'),
        'Temperatura':[22, 24, 25, 23, 21, 26, 28, 30, 32, 33],
        'Umidade': [60, 62, 58, 65, 64, 59, 57, 53, 50, 52],
        'Pressão': [1013, 1012, 1014, 1011, 1010, 1015, 1016, 1012, 1013, 1014]
    }

    # Criação da instância do analisador de meteorologia
    analisador = AnalisadorMeteorologia(dados)

    # Exibição do resumo dos dados
    print("Resumo Estatístico dos Dados Meteorológicos: ")
    print(analisador.resumo_dos_dados())

    # Exibição dos gráficos
    analisador.grafico_temperatura()
    analisador.grafico_umidade() 
    analisador.grafico_pressao()
    analisador.correlacao()


if __name__ == "__main__":
    main()                     
