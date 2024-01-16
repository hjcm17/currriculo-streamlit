import streamlit as st
from pathlib import Path # Pegar informações do caminho
from PIL import Image
from streamlit_card import card

# configurações estruturais:

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
print(diretorio)
arquivo_css = diretorio / 'styles' / 'styles.css'
arquivo_pdf = diretorio / 'assets' / 'curriculo.pdf'
arquivo_image = diretorio / 'assets' / 'avatar.jpg'

Titulo = "Curriculo | Hugo Mota"
Nome = "Hugo Mota"
Descricao = """

    Profissional de TIC com mais de 4 anos de experiência técnica, buscando transição sólida para programação e desenvolvimento web.

"""

Email = "hugojcmota@gmail.com"
MidiaSocial = { "GitHub":"https://github.com/hjcm17"}

Cursos = {
    "Construindo um Sistema para um Estacionamento com C#": 'https://hermes.digitalinnovation.one/certificates/A018D22C.pdf?_gl=1*uivgtj*_ga*MTM4MjA1NzE0NC4xNzAxMzg1MzIy*_ga_7GXMH3CQ72*MTcwNTQ0NTA2MC4yLjEuMTcwNTQ0NTEwMS4xOS4wLjA.',
    "Versionamento de Código com Git e GitHub": 'https://hermes.digitalinnovation.one/certificates/16B3674F.pdf?_gl=1*19ox6s*_ga*MTM4MjA1NzE0NC4xNzAxMzg1MzIy*_ga_7GXMH3CQ72*MTcwNTQ0NTA2MC4yLjEuMTcwNTQ0NTE1Ni41OS4wLjA.'
}

# Carregando assets:
with open(arquivo_css) as c:
    st.markdown(f'<style>{c.read()}<\style>', unsafe_allow_html=True)

with open(arquivo_pdf, 'rb') as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()

image = Image.open(arquivo_image)

# Criando layout:
col1, col2 = st.columns(2, gap="small") # duas colunas
with col1:
    st.image(image,width=250)

with col2:
    st.title(Nome)
    st.write(Descricao)
    st.download_button(
        label="Download Currículo", # nome do botão
        data=pdfLeitura, # arquivo pdf que será baixado
        file_name="Hugo Mota - Curriculo.pdf", # nome do arquivo quando for baixado
        mime="application/octet-stream", # Não precis abrir no navegador

    )

st.write("✉️"+Email)

# Adicionando midias sociais:

colunas = st.columns(len(MidiaSocial))
for indice, (plataforma,link) in enumerate(MidiaSocial.items()):
    colunas[indice].write(f"[{plataforma}]({link})")

# Experiências
st.write('#')
st.subheader('Experiências')
st.write("""
        
         - ✳️Gestão de TIC;
         - ✳️Gerenciamento de conteúdo com Joomla!;
         - ✳️Gerenciamento de conteúdo com Wordpress;         
        
         """)

# Habilidades
st.write("#")
st.subheader("Habilidades")
st.write("""
        - ✳️Gerenciamento de conteúdo com Wordpress;
         """)

# Historico de Trabalho
st.write("#")
st.subheader("Histórico de Trabalho")
st.write("---")

st.write("🆙","***Texto | Aqui***")
st.write("01/2023 - Atual")
st.write("""
        - 🆙texto aqui.
""")


# Cursos:

st.write("#")
st.subheader("Cursos")
st.write("---")
for curso,link in Cursos.items():
    st.write(f'[{curso}]({link})')
