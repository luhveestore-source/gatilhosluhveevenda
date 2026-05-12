import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO VISUAL ---
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

# --- CONFIGURAÇÃO DA IA (Correção Definitiva do Erro 404) ---
try:
    # Chave fornecida pelo usuário
    genai.configure(api_key="AIzaSyAVZqC28ZpVJkSAJxY64jyDOwp035lSiX4")
    # Usando o sufixo -latest para garantir compatibilidade
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Erro na configuração da IA: {e}")

# --- LINKS INEGOCIÁVEIS ---
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
nome = st.text_input("Nome do Produto")
preco = st.text_input("Preço (R$)")
detalhes = st.text_area("Detalhes Extras")

st.markdown("### 🔗 Selecione os Canais de Venda")
selecionados = []

# Seção Achadinhos
st.write("**🎁 Achadinhos (ML, Shopee, Shein)**")
c1, c2, c3 = st.columns(3)
with c1:
    if st.checkbox("Mercado Livre"): selecionados.append(("🔹 Mercado Livre", LINKS_ACHADINHOS["Mercado Livre"]))
with c2:
    if st.checkbox("Shopee"): selecionados.append(("🔸 Shopee", LINKS_ACHADINHOS["Shopee"]))
with c3:
    if st.checkbox("Shein"): selecionados.append(("👠 Shein", LINKS_ACHADINHOS["Shein"]))

# Seção Especializada
st.write("**👟 Especializado (Shoes e Site)**")
c4, c5 = st.columns(2)
with c4:
    if st.checkbox("Luhvee Shoes"): selecionados.append(("👟 Luhvee Shoes", LINK_SHOES))
with c5:
    if st.checkbox("Hub de Links"): selecionados.append(("🌐 Todos os Links", HUB_LINKS))

# --- GERAÇÃO ---
if st.button("🚀 GERAR MENSAGEM COMPLETA"):
    if nome and preco:
        with st.spinner('Gerando copy persuasiva...'):
            try:
                # Prompt focado em gatilhos de venda da Luhvee
                prompt = f"Crie uma copy curta para vender {nome} por R$ {preco}. Use gatilhos de urgência e escassez. Detalhes: {detalhes}"
                response = model.generate_content(prompt)
                
                # Montagem do bloco de links
                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                # Rodapé Inegociável
                rodape = f"\n---\n🔥 **GRUPO VIP:** {GRUPO_VIP}\n📱 **WhatsApp:** {WHATSAPP}\n📸 **Instagram:** {INSTAGRAM}"
                
                st.success("Tudo pronto!")
                st.text_area("Resultado:", response.text + bloco_links + rodape, height=400)
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
    else:
        st.warning("Preencha o nome e o preço!")
