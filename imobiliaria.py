import csv


class Imovel:
    """Classe mãe que representa um imóvel genérico."""

    def __init__(self, tipo: str, valor_base: float):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_aluguel(self) -> float:
        return self.valor_base


class Apartamento(Imovel):
    def __init__(self, quartos=1, tem_garagem=False, tem_criancas=False, valor_base=700.0):
        super().__init__(tipo="Apartamento", valor_base=valor_base)
        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas

    def calcular_aluguel(self) -> float:
        valor = self.valor_base
        if self.quartos == 2:
            valor += 200.0
        if self.tem_garagem:
            valor += 300.0
        if not self.tem_criancas:
            valor *= 0.95
        return valor


class Casa(Imovel):
    def __init__(self, quartos=1, tem_garagem=False, valor_base=900.0):
        super().__init__(tipo="Casa", valor_base=valor_base)
        self.quartos = quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel(self) -> float:
        valor = self.valor_base
        if self.quartos == 2:
            valor += 250.0
        if self.tem_garagem:
            valor += 300.0
        return valor


class Estudio(Imovel):
    def __init__(self, qtd_vagas=0, valor_base=1200.0):
        super().__init__(tipo="Estúdio", valor_base=valor_base)
        self.qtd_vagas = qtd_vagas

    def calcular_aluguel(self) -> float:
        valor = self.valor_base
        if self.qtd_vagas >= 2:
            vagas_extras = self.qtd_vagas - 2
            valor += 250.0 + (vagas_extras * 60.0)
        return valor


class Orcamento:
    def __init__(self, imovel: Imovel, parcelas_contrato=1):
        self.imovel = imovel
        self.valor_contrato_total = 2000.0
        self.parcelas_contrato = min(max(1, parcelas_contrato), 5)

    def exibir_resumo(self):
        aluguel = self.imovel.calcular_aluguel()
        valor_parcela = self.valor_contrato_total / self.parcelas_contrato
        print(f"Imóvel: {self.imovel.tipo}")
        print(f"Aluguel mensal: R$ {aluguel:.2f}")
        print(
            f"Taxa de contrato: R$ {self.valor_contrato_total:.2f} "
            f"({self.parcelas_contrato}x de R$ {valor_parcela:.2f})"
        )

    def geracao_csv(self, nome_arquivo="orcamento_12_meses.csv"):
        aluguel = self.imovel.calcular_aluguel()
        valor_parcela = self.valor_contrato_total / self.parcelas_contrato

        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(
                ["Mes", "Valor_Aluguel", "Parcela_Contrato", "Total_Mensal"]
            )
            for mes in range(1, 13):
                parcela = valor_parcela if mes <= self.parcelas_contrato else 0.0
                escritor.writerow(
                    [mes, f"{aluguel:.2f}", f"{parcela:.2f}", f"{aluguel + parcela:.2f}"]
                )
