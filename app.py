import streamlit as st
from openai import OpenAI

# 1. IDENTIDADE VISUAL E CONFIGURAÇÃO
st.set_page_config(page_title="Luhvee Stores - Gerador Pro", layout="centered")

st.markdown("""
    <style>
    .header-luhvee {
        background: linear-gradient(90deg, #8e2de2, #4a00e0);
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white;
        font-weight: bold;
    }
    </style>
    <div class="header-luhvee">
        <h1>🛍️ Luhvee Stores</h1>
        <p>Sistema Inteligente de Vendas e Copywriting</p>
    </div>
    """, unsafe_allow_html=True)

# Documentação: Conexão segura com OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- BANCO DE LINKS FIXOS (INEGOCIÁVEIS) ---
WHATSAPP = "https://wa.me/5511948021428"
INSTAGRAM = "https://instagram.com/luhveestore"
GRUPO_VIP = "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj"
HUB_LINKS = "https://links-luhveestore.streamlit.app/"

# --- BANCO DE LINKS DE VENDA ---
LINKS_VENDA = {
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Shopintegra (Shoes)": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes"
}

# --- INTERFACE DE ENTRADA ---
st.markdown("### 📝 Informações do Produto")
nome = st.text_input("Qual o nome do produto/achadinho?")
preco = st.text_input("Qual o preço? (Ex: 99,90)")
detalhes = st.text_area("Algum detalhe especial? (Ex: Frete grátis, cores novas)")

st.markdown("### 🔗 Quais links deseja incluir nesta postagem?")
selecionados = []
col1, col2 = st.columns(2)

with col1:
    if st.checkbox("Mercado Livre"): selecionados.append(("🔹 Mercado Livre", LINKS_VENDA["Mercado Livre"]))
    if st.checkbox("Shopee"): selecionados.append(("🔸 Shopee", LINKS_VENDA["Shopee"]))
    if st.checkbox("Shein"): selecionados.append(("👠 Shein", LINKS_VENDA["Shein"]))

with col2:
    if st.checkbox("Shopintegra (Shoes)"): selecionados.append(("👟 Luhvee Shoes", LINKS_VENDA["Shopintegra (Shoes)"]))
    if st.checkbox("Hub de Links"): selecionados.append(("🌐 Todos os Links", HUB_LINKS))

# --- GERAÇÃO DA MENSAGEM ---
if st.button("🚀 GERAR MENSAGEM PARA WHATSAPP/INSTAGRAM"):
    if nome and preco:
        with st.spinner('A IA está preparando sua oferta matadora...'):
            try:
                # Prompt focado em necessidade e gatilhos mentais
                prompt_vendas = f"""
                Crie uma copy curta e poderosa para vender: {nome}.
                Preço: R$ {preco}. Detalhes: {detalhes}.
                Use gatilhos de ESCASSEZ e URGÊNCIA. 
                O objetivo é fazer o cliente clicar agora.
                """
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "Você é um especialista em vendas da Luhvee Stores."},
                              {"role": "user", "content": prompt_vendas}]
                )
                
                copy_gerada = response.choices[0].message.content

                # Montagem do bloco de links
                bloco_links = "\n\n📌 **ADQUIRA AQUI:**\n"
                for label, url in selecionados:
                    bloco_links += f"{label}: {url}\n"
                
                # Rodapé Fixo (Inegociável)
                rodape_fixo = f"""
---
🔥 **PARTICIPE DO GRUPO VIP:** {GRUPO_VIP}
📱 **Dúvidas no WhatsApp:** {WHATSAPP}
📸 **Siga no Instagram:** {INSTAGRAM}
"""

                mensagem_final = copy_gerada + bloco_links + rodape_fixo
                
                st.success("Cópia gerada com sucesso!")
                st.text_area("Pronto para copiar e colar:", mensagem_final, height=400)
                
            except Exception as e:
                st.error(f"Erro técnico: {e}")
    else:
        st.warning("Por favor, preencha o nome e o preço do produto.")
