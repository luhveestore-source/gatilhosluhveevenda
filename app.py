import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO VISUAL (Identidade Luhvee Stores)
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
        <p>Sistema Inteligente de Vendas (Versão Gratuita)</p>
    </div>
    """, unsafe_allow_html=True)

# CONFIGURAÇÃO DA IA (Google Gemini Gratuito)
# Usando a chave que você forneceu diretamente para facilitar o seu teste agora
try:
    genai.configure(api_key="AIzaSyAVZqC28ZpVJkSAJxY64jyDOwp035lSiX4")
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Erro na configuração da IA: {e}")

# BANCO DE LINKS (Configurações Inegociáveis)
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

# INTERFACE DE USUÁRIO
st.markdown("### 📝 Informações do Produto")
nome = st.text_input("Nome do Produto", placeholder="Ex: Tênis Confort Plus")
preco = st.text_input("Preço (R$)", placeholder="Ex: 129,90")
detalhes = st.text_area("Detalhes/Destaques", placeholder="Ex: Frete grátis para SP")

st.markdown("### 🔗 Selecione os Links para a Copy")
selecionados = []
col1, col2 = st.columns(2)

with col1:
    if st.checkbox("Mercado Livre"): selecionados.append(("🔹 Mercado Livre", LINKS_VENDA["Mercado Livre"]))
    if st.checkbox("Shopee"): selecionados.append(("🔸 Shopee", LINKS_VENDA["Shopee"]))
    if st.checkbox("Shein"): selecionados.append(("👠 Shein", LINKS_VENDA["Shein"]))

with col2:
    if st.checkbox("Shopintegra (Shoes)"): selecionados.append(("👟 Luhvee Shoes", LINKS_VENDA["Shopintegra (Shoes)"]))
    if st.checkbox("Hub de Links"): selecionados.append(("🌐 Todos os Links", HUB_LINKS))

# GERAÇÃO DA MENSAGEM
if st.button("🚀 GERAR MENSAGEM (GRATUITO)"):
    if nome and preco:
        with st.spinner('O Gemini está criando sua copy de vendas...'):
            try:
                # Prompt otimizado para Neuro-Copywriting
                prompt = f"""
                Atue como especialista em vendas da Luhvee Stores. 
                Crie uma copy curta e urgente para: {nome}. 
                Preço: R$ {preco}. Detalhes: {detalhes}. 
                Use gatilhos de escassez e exclusividade.
                """
                response = model.generate_content(prompt)
                texto_ia = response.text

                # Montagem do bloco de links de venda
                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                # Rodapé Fixo (WhatsApp, Insta e Grupo VIP)
                rodape = f"\n---\n🔥 **GRUPO VIP:** {GRUPO_VIP}\n📱 **WhatsApp:** {WHATSAPP}\n📸 **Instagram:** {INSTAGRAM}"

                st.success("Cópia gerada!")
                st.text_area("Copie e poste:", texto_ia + bloco_links + rodape, height=400)
                
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
    else:
        st.warning("Preencha o nome e o preço!")
