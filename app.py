import spacy

# Carregar o modelo de linguagem para português
nlp = spacy.load('pt_core_news_sm')

def extrator_de_entidades(texto):
    doc = nlp(texto)

    pessoas = []
    lugares = []
    
    for ent in doc.ents:
        if ent.label_ == "PER":
            pessoas.append(ent.text)
        elif ent.label_ == "GPE" or ent.label_ == "LOC":
            lugares.append(ent.text)
    
    return {'Pessoas': pessoas, 'Lugares': lugares,
            'Qtd. de pessoas encontrados': len(pessoas),
            'Qtd. de lugares encontrados': len(lugares)}

# Texto de exemplo
texto = 'Carlos foi com Isabelle para a Europa, passaram 8 dias lá, após isso foram para Itália'

print(extrator_de_entidades(texto))