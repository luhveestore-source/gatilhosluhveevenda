import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="Luhvees - Gerador Pro", layout="centered")

st.markdown("""
    <style>
    .header-luhvee {
        background: linear-gradient(90deg, #8e2de2, #4a00e0);
        padding: 25px; border-radius: 15px; color: white; text-align: center; margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%; border-radius: 10px; background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white; font-weight: bold;
    }
    </style>
    <div class="header-luhvee">
        <h1>🛍️ Luhvee Stores</h1>
        <p>Sistema de Vendas e Neuro-Copywriting</p>
    </div>
    """, unsafe_allow_html=True)

# --- CONFIGURAÇÃO DA IA (Correção do Erro 404) ---
try:
    # Usando o identificador de modelo completo para evitar erro 404
    genai.configure(api_key="AIzaSyAVZqC28ZpVJkSAJxY64jyDOwp035lSiX4")
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro na configuração da IA: {e}")

# --- LINKS INEGOCIÁVEIS (Restaurados) ---
WHATSAPP = "https://wa.me/5511948021428"
INSTAGRAM = "https://instagram.com/luhveestore"
GRUPO_VIP = "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
HUB_LINKS = "https://links-luhveestore.streamlit.app/"

# --- LINKS DE VENDA ---
LINKS_ACHADINHOS = {
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825"
}
LINK_SHOES = "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes"

# --- INTERFACE DE USUÁRIO ---
st.markdown("### 📝 Informações do Produto")
nome = st.text_input("Nome do Produto/Achadinho")
preco = st.text_input("Preço (R$)")
detalhes = st.text_area("Detalhes (Ex: Retira até os mais difíceis)")

st.markdown("### 🔗 Selecione onde Postar")
selecionados = []

# Divisão Achadinhos
st.write("**🎁 Achadinhos**")
col1, col2, col3 = st.columns(3)
with col1:
    if st.checkbox("Mercado Livre"): selecionados.append(("🔹 Mercado Livre", LINKS_ACHADINHOS["Mercado Livre"]))
with col2:
    if st.checkbox("Shopee"): selecionados.append(("🔸 Shopee", LINKS_ACHADINHOS["Shopee"]))
with col3:
    if st.checkbox("Shein"): selecionados.append(("👠 Shein", LINKS_ACHADINHOS["Shein"]))

# Divisão Shoes e Hub
st.write("**👟 Especializado**")
col4, col5 = st.columns(2)
with col4:
    if st.checkbox("Shoes (Shopintegra)"): selecionados.append(("👟 Luhvee Shoes", LINK_SHOES))
with col5:
    if st.checkbox("Hub de Links"): selecionados.append(("🌐 Todos os Links", HUB_LINKS))

# --- GERAÇÃO DA MENSAGEM ---
if st.button("🚀 GERAR MENSAGEM COMPLETA"):
    if nome and preco:
        with st.spinner('Gerando copy com gatilhos mentais...'):
            try:
                prompt = f"Atue como vendedor da Luhvee Stores. Crie uma copy curta e urgente para: {nome}. Preço: R$ {preco}. Use gatilhos de Escassez e Urgência. Detalhes: {detalhes}"
                response = model.generate_content(prompt)
                
                # Montagem do bloco de links
                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                # Rodapé Inegociável (Restaurado conforme solicitado)
                rodape = f"""
---
🔥 **PARTICIPE DO GRUPO VIP:** {GRUPO_VIP}
📱 **WhatsApp:** {WHATSAPP}
📸 **Instagram:** {INSTAGRAM}
"""
                st.success("Tudo pronto!")
                st.text_area("Copie e poste:", response.text + bloco_links + rodape, height=400)
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
    else:
        st.warning("Preencha o nome e o preço!")
