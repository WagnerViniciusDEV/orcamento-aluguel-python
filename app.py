import csv
import io

from flask import Flask, make_response, render_template, request

from imobiliaria import Apartamento, Casa, Estudio, Orcamento


app = Flask(__name__)


def criar_imovel(dados):
    tipo = dados.get("tipo", "apartamento")
    quartos = int(dados.get("quartos", 1))
    tem_garagem = dados.get("garagem") == "on"
    tem_criancas = dados.get("tem_criancas") == "on"
    qtd_vagas = int(dados.get("qtd_vagas", 0))

    if tipo == "apartamento":
        return Apartamento(quartos, tem_garagem, tem_criancas)

    if tipo == "casa":
        return Casa(quartos, tem_garagem)

    return Estudio(qtd_vagas)


@app.route("/", methods=["GET", "POST"])
def pagina_inicial():
    resultado = None

    if request.method == "POST":
        imovel = criar_imovel(request.form)
        parcelas = int(request.form.get("parcelas", 1))
        orcamento = Orcamento(imovel, parcelas)

        aluguel = imovel.calcular_aluguel()
        parcela_contrato = (
            orcamento.valor_contrato_total / orcamento.parcelas_contrato
        )

        resultado = {
            "tipo": imovel.tipo,
            "aluguel": aluguel,
            "contrato": orcamento.valor_contrato_total,
            "parcelas": orcamento.parcelas_contrato,
            "parcela_contrato": parcela_contrato,
            "formulario": request.form.to_dict(),
        }

    return render_template("index.html", resultado=resultado)


@app.route("/baixar-csv", methods=["POST"])
def baixar_csv():
    imovel = criar_imovel(request.form)
    parcelas = int(request.form.get("parcelas", 1))
    orcamento = Orcamento(imovel, parcelas)

    aluguel = imovel.calcular_aluguel()
    valor_parcela = orcamento.valor_contrato_total / orcamento.parcelas_contrato

    arquivo = io.StringIO()
    escritor = csv.writer(arquivo)
    escritor.writerow(
        ["Mes", "Valor_Aluguel", "Parcela_Contrato", "Total_Mensal"]
    )

    for mes in range(1, 13):
        parcela = valor_parcela if mes <= orcamento.parcelas_contrato else 0.0
        escritor.writerow(
            [mes, f"{aluguel:.2f}", f"{parcela:.2f}", f"{aluguel + parcela:.2f}"]
        )

    resposta = make_response("\ufeff" + arquivo.getvalue())
    resposta.headers["Content-Type"] = "text/csv; charset=utf-8"
    resposta.headers["Content-Disposition"] = (
        "attachment; filename=orcamento_12_meses.csv"
    )
    return resposta


if __name__ == "__main__":
    app.run(debug=True)
