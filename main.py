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
               <a href='/primos'>Ver numeros primos</a></br>
               <a href='/paises'>Ver Poblacion por paises</a>
               </html>"""
n = 1
@app.route("/primos")
def ver_primos():
    global n
    resultado = f"""<!DOCTYPE html><html><meta charset="UTF-8">
    <title>Numeros Primos</title><p>Del {(n-1)*10}º al {n*10}º Numeros Primos </p><ul>"""
    for i in range(10):
        resultado+=f"<li><p>{next(numeros)}</p></li>"
    resultado+="</ul><a href='/primos'>Proximos 10  numeros primos</a></br><a href='/'>Volver al inicio</a></html>"
    n += 1
    return resultado


POBLACION = {
    "China"                            : 1_395_261_000 ,
    "India"                            : 1_375_898_000 ,
    "Estados Unidos"                   : 329_071_000   ,
    "Indonesia"                        : 266_614_000   ,
    "Pakistán"                         : 216_823_000   ,
    "Brasil"                           : 210_461_000   ,
    "Nigeria"                          : 209_058_000   ,
    "Bangladés"                        : 176_198_000   ,
    "Rusia"                            : 147_043_000   ,
    "Japón"                            : 126_398_000   ,
    "México"                           : 125_357_000   ,
    "Etiopía"                          : 109_392_000   ,
    "Filipinas"                        : 107_041_000   ,
    "Egipto"                           : 99_149_000    ,
    "Vietnam"                          : 94_827_000    ,
    "República Democrática del Congo"  : 84_833_000    ,
    "Alemania"                         : 83_082_000    ,
    "Irán"                             : 82_231_000    ,
    "Turquía"                          : 81_821_000    ,
    "Tailandia"                        : 69_398_000    ,
    "Reino Unido"                      : 66_636_000    ,
    "Francia"                          : 65_236_000    ,
    "Italia"                           : 60_466_000    ,
    "Sudáfrica"                        : 58_198_000    ,
    "Tanzania"                         : 55_082_000    ,
    "Myanmar"                          : 54_189_000    ,
    "Kenia"                            : 52_051_000    ,
    "Corea del Sur"                    : 51_843_000    ,
    "España"                           : 46_791_000    ,
    "Colombia"                         : 45_878_000    ,
    "Argentina"                        : 44_723_000    ,
    "Argelia"                          : 42_993_000    ,
    "Sudán"                            : 42_604_000    ,
    "Ucrania"                          : 42_169_000    ,
    "Uganda"                           : 39_416_000    ,
    "Polonia"                          : 38_447_000    ,
    "Irak"                             : 38_328_000    ,
    "Canadá"                           : 37_346_000    ,
    "Marruecos"                        : 35_165_000    ,
    "Arabia Saudita"                   : 34_200_000    ,
    "Uzbekistán"                       : 33_217_000    ,
    "Malasia"                          : 32_659_000    ,
    "Perú"                             : 32_362_000    ,
    "Venezuela"                        : 32_030_000    ,
    "Afganistán"                       : 31_936_000    ,
    "Mozambique"                       : 30_368_000    ,
    "Ghana"                            : 29_952_000    ,
    "Angola"                           : 29_703_000    ,
    "Nepal"                            : 29_419_000    ,
    "Yemen"                            : 29_332_000    ,
    "Madagascar"                       : 26_755_000    ,
    "Costa de Marfil"                  : 25_825_000    ,
    "Corea del Norte"                  : 25_694_000    ,
    "Australia"                        : 25_150_000    ,
    "Camerún"                          : 24_089_000    ,
    "Níger"                            : 21_890_000    ,
    "Sri Lanka"                        : 21_789_000    ,
    "Burkina Faso"                     : 20_571_000    ,
    "Rumanía"                          : 19_413_000    ,
    "Malí"                             : 19_395_000    ,
    "Chile"                            : 18_880_000    ,
    "Kazajistán"                       : 18_400_000    ,
    "Siria"                            : 18_298_000    ,
    "Malaui"                           : 18_217_000    ,
    "Guatemala"                        : 17_545_000    ,
    "Países Bajos"                     : 17_290_000    ,
    "Ecuador"                          : 17_170_000    ,
    "Zambia"                           : 17_136_000    ,
    "Camboya"                          : 16_206_000    ,
    "Senegal"                          : 15_969_000    ,
    "Chad"                             : 15_630_000    ,
    "Somalia"                          : 15_368_000    ,
    "Zimbabue"                         : 14_964_000    ,
    "Sudán del Sur"                    : 12_570_000    ,
    "Ruanda"                           : 12_150_000    ,
    "Guinea"                           : 12_025_000    ,
    "Túnez"                            : 11_671_000    ,
    "Benín"                            : 11_545_000    ,
    "Bélgica"                          : 11_459_000    ,
    "Bolivia"                          : 11_390_000    ,
    "Grecia"                           : 11_314_000    ,
    "Haití"                            : 11_220_000    ,
    "Cuba"                             : 11_212_000    ,
    "Jordania"                         : 10_900_000    ,
    "Burundi"                          : 10_836_000    ,
    "República Checa"                  : 10_640_000    ,
    "República Dominicana"             : 10_315_000    ,
    "Portugal"                         : 10_252_000    ,
    "Suecia"                           : 10_236_000    ,
    "Azerbaiyán"                       : 9_984_00      ,
    "Hungría"                          : 9_759_000     ,
    "Emiratos Árabes Unidos"           : 9_654_000     ,
    "Bielorrusia"                      : 9_478_000     ,
    "Tayikistán"                       : 9_129_000     ,
    "Honduras"                         : 9_087_000     ,
    "Israel"                           : 8_969_000     ,
    "Austria"                          : 8_875_000     ,
    "Papúa Nueva Guinea"               : 8_660_000     ,
    "Suiza"                            : 8_549_000     ,
    "Sierra Leona"                     : 7_847_000     ,
    "Togo"                             : 7_453_000     ,
    "Paraguay"                         : 7_104_000     ,
    "Laos"                             : 7_018_000     ,
    "Bulgaria"                         : 7_004_000     ,
    "Serbia"                           : 6_971_000     ,
    "El Salvador"                      : 6_675_000     ,
    "Libia"                            : 6_507_000     ,
    "Nicaragua"                        : 6_494_000     ,
    "Kirguistán"                       : 6_379_000     ,
    "Líbano"                           : 6_236_000     ,
    "Turkmenistán"                     : 5_902_000     ,
    "Dinamarca"                        : 5_814_000     ,
    "Singapur"                         : 5_652_000     ,
    "Finlandia"                        : 5_523_000     ,
    "República del Congo"              : 5_493_000     ,
    "Eslovaquia"                       : 5_449_000     ,
    "Noruega"                          : 5_333_000     ,
    "Eritrea"                          : 5_273_000     ,
    "Costa Rica"                       : 5_032_000     ,
    "Nueva Zelanda"                    : 4_915_000     ,
    "Irlanda"                          : 4_902_000     ,
    "República Centroafricana"         : 4_770_000     ,
    "Omán"                             : 4_649_000     ,
    "Liberia"                          : 4_432_000     ,
    "Kuwait"                           : 4_244_000     ,
    "Panamá"                           : 4_190_000     ,
    "Croacia"                          : 4_080_000     ,
    "Mauritania"                       : 4_030_000     ,
    "Georgia"                          : 3_733_000     ,
    "Moldavia"                         : 3_560_000     ,
    "Uruguay"                          : 3_512_000     ,
    "Bosnia y Herzegovina"             : 3_436_000     ,
    "Mongolia"                         : 3_271_000     ,
    "Armenia"                          : 2_967_000     ,
    "Albania"                          : 2_875_000     ,
    "Lituania"                         : 2_792_000     ,
    "Catar"                            : 2_767_000     ,
    "Jamaica"                          : 2_729_000     ,
    "Namibia"                          : 2_437_000     ,
    "Botsuana"                         : 2_318_000     ,
    "Gambia"                           : 2_197_000     ,
    "Gabón"                            : 2_090_000     ,
    "Macedonia"                        : 2_077_000     ,
    "Eslovenia"                        : 2_071_000     ,
    "Lesoto"                           : 2_044_000     ,
    "Letonia"                          : 1_920_000     ,
    "Baréin"                           : 1_608_000     ,
    "Guinea-Bisáu"                     : 1_599_000     ,
    "Guinea Ecuatorial"                : 1_382_000     ,
    "Trinidad y Tobago"                : 1_361_000     ,
    "Estonia"                          : 1_323_000     ,
    "Timor Oriental"                   : 1_275_000     ,
    "Mauricio"                         : 1_268_000     ,
    "Suazilandia"                      : 1_106_000     ,
    "Yibuti"                           : 1_064_000     ,
    "Fiyi"                             : 891_000       ,
    "Chipre"                           : 872_000       ,
    "Comoras"                          : 862_000       ,
    "Guyana"                           : 783_000       ,
    "Bután"                            : 740_000       ,
    "Islas Salomón"                    : 681_000       ,
    "Montenegro"                       : 623_000       ,
    "Luxemburgo"                       : 615_000       ,
    "Surinam"                          : 571_000       ,
    "Cabo Verde"                       : 548_000       ,
    "Malta"                            : 492_000       ,
    "Brunéi"                           : 429_000       ,
    "Belice"                           : 403_000       ,
    "Maldivas"                         : 386_000       ,
    "Bahamas"                          : 383_000       ,
    "Islandia"                         : 357_000       ,
    "Vanuatu"                          : 309_000       ,
    "Barbados"                         : 287_000       ,
    "Santo Tomé y Príncipe"            : 205_000       ,
    "Samoa"                            : 200_000       ,
    "Santa Lucía"                      : 180_000       ,
    "Kiribati"                         : 121_000       ,
    "San Vicente y las Granadinas"     : 110_000       ,
    "Granada"                          : 108_000       ,
    "Micronesia"                       : 105_000       ,
    "Antigua y Barbuda"                : 104_000       ,
    "Tonga"                            : 100_000       ,
    "Seychelles"                       : 97_000        ,
    "Dominica"                         : 74_000        ,
    "Andorra"                          : 73_000        ,
    "Islas Marshall"                   : 56_000        ,
    "San Cristóbal y Nieves"           : 56_000        ,
    "Mónaco"                           : 39_000        ,
    "Liechtenstein"                    : 38_000        ,
    "San Marino"                       : 33_000        ,
    "Palaos"                           : 18_000        ,
    "Wallis y Futuna"                  : 13_484        ,
    "Nauru"                            : 11_000        ,
    "Tuvalu"                           : 10_000        ,
    "Isla de Navidad"                  : 1402          ,
    "Islas Cook"                       : 14_153        ,
    "Islas Pitcairn"                   : 47            ,
    "Estados Federados de Micronesia"  : 111_000       ,
    "Guam"                             : 162_742       ,
    "Niue"                             : 1612          ,
    "Isla Norfolk"                     : 2182          ,
    "Polinesia Francesa"               : 245_405       ,
    'Acrotiri y Dhekelia'              : 14_000        ,
    "Kosovo"                           : 1_900_000     ,
    "Macedonia del Norte"              : 700_000       ,
    "Rumania"                          : 21_848_000    ,
    "Aruba"                            : 106_113       ,
    "Islas Caiman"                     : 69_000        ,
    "Puerto Rico"                      : 3_725_789     ,
    "Groenlandia"                      : 61_100        ,
    'Guayana Francesa'                 : 259_500       ,
    "Birmania"                         : 53_700_000    ,
    "Palestina"                        : 3_935_249     ,
    "Ciudad del Vaticano"              : 800           }

AMERICA_DEL_NORTE = [
    "Canadá","Estados Unidos","Groenlandia","México",]

AMERICA_CENTRAL= [
                "Belice","Costa Rica","El Salvador","Guatemala","Honduras","Nicaragua","Panamá",
                "Antigua y Barbuda","Aruba","Bahamas","Barbados","Cuba","Dominica","Granada",
                "Haití","Islas Caiman","Jamaica","Puerto Rico","República Dominicana",
                "San Cristóbal y Nieves","San Vicente y las Granadinas","Santa Lucía","Trinidad y Tobago"]

AMÉRICA_DEL_SUR = [
                    "Argentina","Bolivia","Brasil","Chile","Colombia","Ecuador","Guayana Francesa",
                  "Guyana","Paraguay","Perú","Surinam","Uruguay","Venezuela"]

ASIA = [
        "Afganistán","Arabia Saudita","Armenia","Azerbaiyán","Baréin","Bangladés","Birmania","Bután",
        "Brunéi","Camboya","Catar","China","Corea del Norte" , "Corea del Sur", "Emiratos Árabes Unidos",
        "Filipinas","India","Indonesia",
        "Irak","Irán","Israel","Japón","Jordania","Kazajistán","Kirguistán","Kuwait","Laos","Líbano",
        "Malasia","Maldivas","Mongolia","Nepal","Omán","Pakistán","Palestina","Singapur","Siria","Sri Lanka",
        "Tailandia","Tayikistán","Turkmenistán","Turquía","Uzbekistán","Vietnam","Yemen"]

EUROPA = [ 
          "Acrotiri y Dhekelia", "Albania", "Alemania", "Andorra","Austria", "Bielorrusia", "Bélgica", "Bosnia y Herzegovina",
        "Bulgaria", "Ciudad del Vaticano","Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia",
        "Finlandia", "Francia", "Georgia", "Grecia", "Hungría", "Irlanda", "Islandia", "Italia",
        "Kosovo", "Letonia", "Lituania", "Luxemburgo", "Malta", "Macedonia del Norte", "Moldavia", "Noruega", "Países Bajos",
        "Polonia", "Portugal", "Reino Unido","República Checa", "Rumania", "Rusia", "San Marino", "Serbia", "Suecia", "Suiza",
        "Ucrania"]

OCEANIA = [
    "Australia", "Islas Cook","Isla de Navidad","Islas Marshall","Islas Pitcairn","Islas Salomón",
            "Estados Federados de Micronesia","Fiyi","Guam","Kiribati","Nauru","Niue","Isla Norfolk",
            "Nueva Zelanda","Palaos","Papúa Nueva Guinea","Islas Pitcairn","Polinesia Francesa","Samoa",
            "Tonga","Tuvalu","Vanuatu","Wallis y Futuna"]

TOTAL = sum( [ POBLACION[i] for continente in (AMERICA_CENTRAL,AMERICA_DEL_NORTE,AMÉRICA_DEL_SUR,EUROPA,ASIA,OCEANIA) for i in continente])


@app.route("/paises")
def paises():
    
    tabla=f"<table><tr><th>{'PAIS':25}</th><th>{'POBLACION'}</th></tr><tr>"
    for continente in (AMÉRICA_DEL_SUR,AMERICA_DEL_NORTE,AMERICA_CENTRAL,ASIA,EUROPA,OCEANIA):
        for pais in continente:
            tabla+=f"<th>{pais:40}</th><th>{POBLACION[pais]:>13}</th></tr><tr>"
    tabla+="</td>"
    return f"""<!DOCTYPE html><html><meta charset="UTF-8">
                <title>Poblacion</title><p>Tabla de paises</p>
                {tabla}<tr>
                <th>{'TOTAL':40}</th><th>{TOTAL:>13}</th></tr></table>
                <a href='/'>Volver al inicio</a></html>
                </html>  
    """













app.run(host="0.0.0", port=8080, debug=False)