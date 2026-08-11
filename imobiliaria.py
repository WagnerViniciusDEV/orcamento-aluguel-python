import csv

class Imovel:
    """Classe mãe que representa um imóvel genérico."""

    def __init__(self, tipo: str, valor_base: float):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_aluguel(self) -> float:
        return self.valor_base


class Apartamento(Imovel):
    """Apartamento: R$ 700 base (1 quarto). +R$ 200 para 2 quartos. Desconto de 5% se não tiver crianças."""

    def __init__(self, quartos: int = 1, tem_garagem: bool = False, tem_criancas: bool = False, valor_base: float = 700.0):
        super().__init__(tipo="Apartamento", valor_base=valor_base)
        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas

    def calcular_aluguel(self) -> float:
        valor = self.valor_base

        # Adicional de quarto
        if self.quartos == 2:
            valor += 200.0

        # Adicional de garagem
        if self.tem_garagem:
            valor += 300.0

        # Desconto de 5% se NÃO tiver crianças
        if not self.tem_criancas:
            valor *= 0.95

        return valor


class Casa(Imovel):
    """Casa: R$ 900 base (1 quarto). +R$ 250 para 2 quartos."""

    def __init__(self, quartos: int = 1, tem_garagem: bool = False, valor_base: float = 900.0):
        super().__init__(tipo="Casa", valor_base=valor_base)
        self.quartos = quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel(self) -> float:
        valor = self.valor_base

        # Adicional de quarto
        if self.quartos == 2:
            valor += 250.0

        # Adicional de garagem
        if self.tem_garagem:
            valor += 300.0

        return valor


class Estudio(Imovel):
    """Estúdio: R$ 1200 base. 2 vagas = R$ 250, + R$ 60 por vaga extra."""

    def __init__(self, qtd_vagas: int = 0, valor_base: float = 1200.0):
        super().__init__(tipo="Estúdio", valor_base=valor_base)
        self.qtd_vagas = qtd_vagas

    def calcular_aluguel(self) -> float:
        valor = self.valor_base

        if self.qtd_vagas >= 2:
            vagas_extras = self.qtd_vagas - 2
            valor += 250.0 + (vagas_extras * 60.0)
        elif self.qtd_vagas == 1:
            valor += 125.0  # Opcional para 1 vaga

        return valor


class Orcamento:
    """Classe que gerencia o cálculo do contrato, exibe o resumo e gera o CSV."""

    def __init__(self, imovel: Imovel, parcelas_contrato: int = 1):
        self.imovel = imovel
        self.valor_contrato_total = 2000.0  # R$ 2.000,00
        self.parcelas_contrato = min(max(1, parcelas_contrato), 5)

    def exibir_resumo(self):
        aluguel = self.imovel.calcular_aluguel()
        valor_parcela_contrato = self.valor_contrato_total / self.parcelas_contrato

        print("\n" + "=" * 45)
        print("        ORÇAMENTO DE ALUGUEL - R.M         ")
        print("=" * 45)
        print(f"Imóvel selecionado : {self.imovel.tipo}")
        print(f"Aluguel Mensal      : R$ {aluguel:.2f}")
        print(f"Taxa de Contrato    : R$ {self.valor_contrato_total:.2f} ({self.parcelas_contrato}x de R$ {valor_parcela_contrato:.2f})")
        print("=" * 45)

    def geracao_csv(self, nome_arquivo: str = "orcamento_12_meses.csv"):
        """Gera um arquivo .csv com a simulação das 12 parcelas mensais."""
        aluguel_mensal = self.imovel.calcular_aluguel()
        valor_parcela_contrato = self.valor_contrato_total / self.parcelas_contrato

        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Mes", "Valor_Aluguel", "Parcela_Contrato", "Total_Mensal"])

            for mes in range(1, 13):
                parcela_contrato = valor_parcela_contrato if mes <= self.parcelas_contrato else 0.0
                total_mes = aluguel_mensal + parcela_contrato
                escritor.writerow([mes, f"{aluguel_mensal:.2f}", f"{parcela_contrato:.2f}", f"{total_mes:.2f}"])

        print(f"Arquivo CSV '{nome_arquivo}' gerado com sucesso!")


if __name__ == "__main__":
    # Exemplo: Apartamento de 2 quartos, com garagem e sem crianças (recebe 5% de desconto)
    ap = Apartamento(quartos=2, tem_garagem=True, tem_criancas=False)
    orc1 = Orcamento(imovel=ap, parcelas_contrato=4)
    orc1.exibir_resumo()
    orc1.geracao_csv("orcamento_apartamento.csv")

    # Exemplo: Casa de 2 quartos com garagem
    casa = Casa(quartos=2, tem_garagem=True)
    orc2 = Orcamento(imovel=casa, parcelas_contrato=5)
    orc2.exibir_resumo()