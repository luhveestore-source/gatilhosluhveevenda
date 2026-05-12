import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURAÇÃO VISUAL (Identidade Luhvee Stores) ---
st.set_page_config(page_title="Luhvee Stores - Gerador Pro", layout="centered")

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
        <p>Copywriting Inteligente (Versão 1.5 Flash Corrigida)</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Google Gemini - Atualizado) ---
# A chave que você forneceu anteriormente já está configurada aqui
try:
    genai.configure(api_key="AIzaSyAVZqC28ZpVJkSAJxY64jyDOwp035lSiX4")
    # CORREÇÃO: O modelo 'gemini-1.5-flash' é o substituto estável para o antigo 'gemini-pro'
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro na configuração da IA: {e}")

# --- 3. BANCO DE LINKS (Configurações Inegociáveis) ---
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

# --- 4. INTERFACE DE USUÁRIO ---
st.markdown("### 📝 Informações do Produto")
nome = st.text_input("Nome do Produto")
preco = st.text_input("Preço (R$)")
detalhes = st.text_area("Destaques (Ex: Retira até os mais difíceis)")

st.markdown("### 🔗 Escolha os Links de Venda")
selecionados = []
col1, col2 = st.columns(2)
with col1:
    if st.checkbox("Mercado Livre"): selecionados.append(("🔹 Mercado Livre", LINKS_VENDA["Mercado Livre"]))
    if st.checkbox("Shopee"): selecionados.append(("🔸 Shopee", LINKS_VENDA["Shopee"]))
with col2:
    if st.checkbox("Shopintegra (Shoes)"): selecionados.append(("👟 Luhvee Shoes", LINKS_VENDA["Shopintegra (Shoes)"]))
    if st.checkbox("Hub de Links"): selecionados.append(("🌐 Todos os Links", HUB_LINKS))

# --- 5. LÓGICA DE GERAÇÃO ---
if st.button("🚀 GERAR MENSAGEM AGORA"):
    if nome and preco:
        with st.spinner('Gerando sua copy irresistível...'):
            try:
                # Prompt para a IA focado em gatilhos mentais da marca Luhvees
                prompt = f"Atue como vendedor da Luhvee Stores. Crie uma copy curta e urgente para: {nome}. Preço: R$ {preco}. Gatilhos: Escassez e Urgência. Detalhes: {detalhes}"
                response = model.generate_content(prompt)
                
                # Montagem do bloco de links de venda
                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                # Rodapé Inegociável (WhatsApp, Insta e Grupo VIP)
                rodape = f"\n---\n🔥 **GRUPO VIP:** {GRUPO_VIP}\n📱 **WhatsApp:** {WHATSAPP}\n📸 **Instagram:** {INSTAGRAM}"
                
                st.success("Tudo pronto!")
                st.text_area("Copie e poste:", response.text + bloco_links + rodape, height=400)
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
    else:
        st.warning("Preencha o nome e o preço!")
