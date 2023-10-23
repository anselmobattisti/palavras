from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(words, file_name):
    c = canvas.Canvas(file_name, pagesize=letter)

    # Tamanho da página
    width, height = letter

    # Divisão da página
    middle = height / 2

    for word_pair in words:

        # Configurações da fonte
        c.setFont("Helvetica", 120)

        word1, word2 = word_pair

        # Primeira palavra na parte superior da linha
        c.drawCentredString(width / 2, middle + 190, word1)

        # Segunda palavra na parte inferior da linha
        c.drawCentredString(width / 2, middle - 250, word2)

        # Configurações da linha tracejada
        c.setDash(1, 10) 

        # Desenhar a linha tracejada
        c.line(50, middle, width - 50, middle)

        # Nova página
        c.showPage()

    # Salvar o arquivo PDF
    c.save()

palavras_familia = [    
    ("pai", "mãe"), 
    ("vó", "tio"), 
    ("tia", "vô"), 
    ("primo", "irmão"), 
]

palavras_banho = [
    ("sabão", "água"), 
    ("toalha", "bucha"), 
    ("quente", "frio"), 
    ("espuma", "seco"), 
    ("molhado", "sujo"), 
    ("limpo", "perfume"),
    ("creme", "cheiroso"),    
    ("fedido", "macio"),
    ("pente", "macio"),
]

palavras_cropo = [    
    ("mão", "pé"), 
    ("perna", "dedo"), 
    ("boca", "orelha"), 
    ("cabeça", "braço"), 
    ("nariz", "olho"), 
    ("língua", "lábio"),    
    ("joelho", "cotovelo"),
    ("bochecha", "peito"),
    ("cabelo", "umbigo"),    
    ("unha", "pele"),    
    ("pescoço", "testa"),
    ("bumbum", "coxa"),
]

create_pdf(palavras_cropo, "output.pdf")