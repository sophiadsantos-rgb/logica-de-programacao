brutos= [
    " MARIA DA SILVA ",
    'joao.souza@EMAIL.COM',
    " RUA DAS FLORES, No 123 ",
    " 000.111.222-33",
    "CARLLOS>ROCHA@ESCOLA.ORG",
    " AV. CENTRAL, No 450 "
]

dados_limpos = []

for item in brutos:
    texto= item.strip()
    if "@" in texto:
        texto=texto.lower()
    else:
        texto=texto.replace("No", "Número")
        texto=texto.replace(".", "").replace("-","")
    dados_limpos.append(texto)
print("   BASE DE DADOS TRATADA E SANITIZADA    ")
for i, elemento in enumerate(dados_limpos,start=1):
    print(f"{i:02d}.{elemento}")