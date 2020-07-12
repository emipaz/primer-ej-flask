from flask import Flask
app = Flask(__name__)


def primo():
    contador = 1
    listaPrimos = []
    while True:
        contador += 1
        esPrimo = True
        for primo in listaPrimos:
            if contador % primo == 0:
                esPrimo = False
                break
        if esPrimo:
            listaPrimos.append(contador)
            yield contador


numeros = primo()
nombres = "Dado un list de nombre mostrarlo en una ruta de flask como lista HTML".split()



@app.route("/")
def home():
    resultado = ""
    for i in nombres:
        resultado+=f"<li><p>{i}</p></li>"
    return f"""<!DOCTYPE html><html><meta charset="UTF-8">
               <title>Mi primer HTML</title>
               <ul>{resultado}</ul>
               <a href='/primos'>Ver numeros primos</a></html>"""
n = 1
@app.route("/primos")
def ver_primos():
    global n
    resultado = f"""<!DOCTYPE html><html><meta charset="UTF-8">
    <title>Numeros Primos</title><p>Del {(n-1)*10}º al {n*10}º Numeros Primos </p><ul>"""
    for i in range(10):
        resultado+=f"<li><p>{next(numeros)}</p></li>"
    resultado+="</ul><a href='/primos'>Proximos 10  numeros primos</a></html>"
    n += 1
    return resultado


app.run(host="0.0.0", port=8080, debug=False)