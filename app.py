import streamlit as st
import google.generativeai as genai

# 1. IDENTIDADE VISUAL E CONFIGURAÇÃO (Mantendo seu design)
st.set_page_config(page_title="Luhvee Stores - Gerador Grátis", layout="centered")

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
        <p>Sistema de Vendas (Versão Gratuita)</p>
    </div>
    """, unsafe_allow_html=True)

# 2. CONFIGURAÇÃO DO GOOGLE GEMINI (GRATUITO)
# No Streamlit Cloud, mude o nome do Secret para GEMINI_API_KEY
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("Erro: Configure sua GEMINI_API_KEY nos Secrets do Streamlit.")

# --- SEUS LINKS (CONSERVADOS) ---
WHATSAPP = "https://wa.me/5511948021428"
INSTAGRAM = "https://instagram.com/luhveestore"
GRUPO_VIP = "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
HUB_LINKS = "https://links-luhveestore.streamlit.app/"

LINKS_VENDA = {
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Shopintegra (Shoes)": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes"
}

# --- INTERFACE ---
st.markdown("### 📝 Informações do Produto")
nome = st.text_input("Qual o nome do produto?")
preco = st.text_input("Qual o preço?")
detalhes = st.text_area("Detalhes (Ex: Retira até os mais difíceis)")

st.markdown("### 🔗 Selecionar Links")
selecionados = []
col1, col2 = st.columns(2)
with col1:
    if st.checkbox("Mercado Livre"): selecionados.append(("🔹 Mercado Livre", LINKS_VENDA["Mercado Livre"]))
    if st.checkbox("Shopee"): selecionados.append(("🔸 Shopee", LINKS_VENDA["Shopee"]))
with col2:
    if st.checkbox("Shopintegra (Shoes)"): selecionados.append(("👟 Luhvee Shoes", LINKS_VENDA["Shopintegra (Shoes)"]))
    if st.checkbox("Hub de Links"): selecionados.append(("🌐 Todos os Links", HUB_LINKS))

# --- GERAÇÃO ---
if st.button("🚀 GERAR MENSAGEM GRÁTIS"):
    if nome and preco:
        with st.spinner('A IA gratuita está criando sua copy...'):
            try:
                prompt = f"Crie uma copy de venda curta para {nome}, preço R$ {preco}. Use gatilhos de urgência e escassez. Detalhes: {detalhes}"
                response = model.generate_content(prompt)
                copy_gerada = response.text

                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                rodape_fixo = f"\n---\n🔥 **GRUPO VIP:** {GRUPO_VIP}\n📱 **Whats:** {WHATSAPP}\n📸 **Insta:** {INSTAGRAM}"
                
                st.text_area("Cópia Pronta:", copy_gerada + bloco_links + rodape_fixo, height=400)
            except Exception as e:
                st.error(f"Erro ao gerar: {e}")
