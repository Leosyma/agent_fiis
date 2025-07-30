import streamlit as st
from main import run_fiis_assistant

st.title("🤖 Assistente IA de Recomendação de FIIs")
st.write(
    "Esta IA auxilia você com **recomendações de FIIs** com base nos relatórios gerenciais."
)

# Barra lateral para seleção do usuário
with st.sidebar:
    st.header("Selecione uma tarefa:")
    tipo_tarefa = "Responder Pergunta sobre FIIs"  # Apenas uma tarefa disponível, por enquanto

# Campo de entrada para pergunta do usuário
pergunta_usuario = st.text_area("Digite sua pergunta sobre FIIs:")

# Executa o Assistente IA de FIIs ao clicar no botão
if st.button("Executar Verificação de FIIs"):
    if not pergunta_usuario.strip():
        st.warning("⚠️ Por favor, digite sua pergunta antes de executar.")
    else:
        st.write("⏳ Processando sua solicitação... Aguarde, por favor.")

        # Chama a função do arquivo main.py
        resultado = run_fiis_assistant(pergunta_usuario)

        # Exibe a resposta da IA
        st.subheader("✅ Resposta da IA sobre FIIs:")
        st.write(resultado)
