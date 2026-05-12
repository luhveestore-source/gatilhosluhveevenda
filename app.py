import streamlit as st
import google.generativeai as genai

# --- 1. IDENTIDADE VISUAL (Luhvees) ---
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

# --- 2. CONFIGURAÇÃO DA IA (Segurança via Secrets) ---
# Explicação: Este bloco tenta buscar sua chave no painel do Streamlit.
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Busca automática do modelo disponível para evitar erros 404
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error("Erro: A GEMINI_API_KEY não foi encontrada nos Secrets do Streamlit.")

# --- 3. LINKS INEGOCIÁVEIS (Contatos Oficiais) ---
WHATSAPP = "https://wa.me/5511948021428"
INSTAGRAM = "https://instagram.com/luhveestore"
GRUPO_VIP = "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"

# --- 4. LINKS DE VENDA (Categorias) ---
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
detalhes = st.text_area("Destaques (Ex: Frete grátis, última chance)")

st.markdown("### 🔗 Selecione os Links")
selecionados = []

st.write("**🎁 Seção Achadinhos**")
col1, col2, col3 = st.columns(3)
with col1:
    if st.checkbox("Mercado Livre"): selecionados.append(("🔹 Mercado Livre", LINKS_ACHADINHOS["Mercado Livre"]))
with col2:
    if st.checkbox("Shopee"): selecionados.append(("🔸 Shopee", LINKS_ACHADINHOS["Shopee"]))
with col3:
    if st.checkbox("Shein"): selecionados.append(("👠 Shein", LINKS_ACHADINHOS["Shein"]))

st.write("**👟 Seção Shoes**")
if st.checkbox("Luhvee Shoes"): selecionados.append(("👟 Luhvee Shoes", LINK_SHOES))

# --- 6. GERAÇÃO DA MENSAGEM ---
if st.button("🚀 GERAR MENSAGEM COMPLETA"):
    if nome and preco:
        with st.spinner('A IA está preparando sua oferta...'):
            try:
                prompt = f"Atue como vendedor da Luhvee Stores. Crie uma copy curta para vender: {nome}. Preço: R$ {preco}. Detalhes: {detalhes}"
                response = model.generate_content(prompt)
                
                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                rodape = f"\n---\n🔥 **GRUPO VIP:** {GRUPO_VIP}\n📱 **WhatsApp:** {WHATSAPP}\n📸 **Instagram:** {INSTAGRAM}"
                st.success("Tudo pronto!")
                st.text_area("Resultado Final:", response.text + bloco_links + rodape, height=450)
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
