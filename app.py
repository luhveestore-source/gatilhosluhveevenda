import streamlit as st
import google.generativeai as genai

# --- 1. IDENTIDADE VISUAL (Luhvee Stores) ---
st.set_page_config(page_title="Luhvee Stores Pro", layout="centered")

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

# --- 2. CONFIGURAÇÃO DA IA (Solução Automática para Erro 404) ---
try:
    genai.configure(api_key="AIzaSyAVZqC28ZpVJkSAJxY64jyDOwp035lSiX4")
    
    # Método educativo: Listamos os modelos e pegamos o primeiro que suporta geração de conteúdo
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # Prioridade para o Flash, senão pega o primeiro disponível
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro na inicialização: {e}")

# --- 3. LINKS INEGOCIÁVEIS (Restaurados) ---
WHATSAPP = "https://wa.me/5511948021428"
INSTAGRAM = "https://instagram.com/luhveestore"
GRUPO_VIP = "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
HUB_LINKS = "https://links-luhveestore.streamlit.app/"

# --- 4. LINKS DE VENDA (Organizados) ---
LINKS_ACHADINHOS = {
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825"
}
LINK_SHOES = "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes"

# --- 5. INTERFACE DE USUÁRIO ---
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

# --- 6. GERAÇÃO DA MENSAGEM ---
if st.button("🚀 GERAR MENSAGEM COMPLETA"):
    if nome and preco:
        with st.spinner('A IA está criando sua oferta...'):
            try:
                prompt = f"Atue como vendedor da Luhvee Stores. Crie uma copy curta e urgente para: {nome}. Preço: R$ {preco}. Use gatilhos de Escassez. Detalhes: {detalhes}"
                response = model.generate_content(prompt)
                
                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                # Rodapé Inegociável (Blindado)
                rodape = f"""
---
🔥 **PARTICIPE DO GRUPO VIP:** {GRUPO_VIP}
📱 **WhatsApp:** {WHATSAPP}
📸 **Instagram:** {INSTAGRAM}
"""
                st.success("Cópia gerada com sucesso!")
                st.text_area("Resultado final:", response.text + bloco_links + rodape, height=450)
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
    else:
        st.warning("Preencha o nome e o preço!")
