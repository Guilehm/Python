import webbrowser
from urllib.request import Request, urlopen
import xml.etree.cElementTree as ET


def calcula_frete (cep_origem='14409652', cep_destino='04110021', peso='1', tipo_frete='04014',
                   altura = '10', largura = '20', comprimento = '20'):
    url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?'
    url += '&nCdEmpresa='
    url += '&sDsSenha='
    url += '&nCdServico=' + tipo_frete
    url += '&sCepOrigem=' + cep_origem
    url += '&sCepDestino=' + cep_destino
    url += '&nVlPeso=' + peso
    url += '&nCdFormato=1'
    url += '&nVlComprimento=' + comprimento
    url += '&nVlAltura=' + altura
    url += '&nVlLargura=' + largura
    url += '&nVlDiametro=0'
    url += '&sCdMaoPropria=n'
    url += '&nVlValorDeclarado=0'
    url += '&sCdAvisoRecebimento=n'
    url += '&StrRetorno=xml'
    url += '&nIndicaCalculo=3'

    return url

url = calcula_frete()


request = Request(url)
result = urlopen(request).read()

result = result.decode('ISO-8859-1')
find_valor = ('<Valor>')
find_prazo = ('<PrazoEntrega>')
pos_valor = result.index(find_valor) + len(find_valor)
valor = result[pos_valor : pos_valor + 5]
print(valor)