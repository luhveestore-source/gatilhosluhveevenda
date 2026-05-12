import streamlit as st
from openai import OpenAI

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Luhvees - Neuro Copy", page_icon="🛍️", layout="centered")

# 2. ESTILIZAÇÃO VISUAL (CSS)
# Aqui definimos as cores rosa, lilás e preto conforme a identidade da marca.
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stApp { background-color: #ffffff; }
    
    /* Cabeçalho com Gradiente Lilás/Roxo */
    .header-container {
        background: linear-gradient(90deg, #8e2de2, #4a00e0);
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Botões Principais */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: none;
        height: 3em;
        background: #f0f2f6;
        color: #31333F;
        transition: 0.3s;
    }
    
    /* Botão de Geração com destaque */
    div.stButton > button:first-child[kind="primary"] {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        border: none;
    }
    
    /* Caixas de entrada */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONEXÃO COM A INTELIGÊNCIA ARTIFICIAL
# Certifique-se de adicionar sua OPENAI_API_KEY nos Secrets do Streamlit Cloud
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("Erro: Chave API não configurada nos Secrets do Streamlit.")

# --- INTERFACE DO USUÁRIO ---

# Cabeçalho (Baseado na imagem 1000448882.png)
st.markdown("""
    <div class="header-container">
        <h1 style='margin:0;'>🛍️ Luhvees</h1>
        <p style='margin:0; opacity: 0.9;'>Gerador Multi-Seção com Neuro-Copywriting</p>
    </div>
    """, unsafe_allow_html=True)

# Botões de Categoria
col1, col2 = st.columns(2)
with col1:
    st.button("👟 Shoes")
with col2:
    st.button("🎁 Achadinhos")

st.button("🏪 Minha Loja")

st.markdown("---")

# Seção de Dados do Produto
st.markdown("### 📝 Dados do Produto")
with st.expander("Clique para preencher as informações", expanded=True):
    nome_produto = st.text_input("Nome do Produto", placeholder="Ex: Tênis Premium")
    preco = st.text_input("Preço (R$)", placeholder="Ex: 199.90")
    descricao = st.text_area("Descrição", placeholder="Ex: Conforto extremo e design exclusivo...")

    st.write("**Selecione os Links:**")
    c1, c2, c3 = st.columns(3)
    with c1: st.checkbox("HubLinks", value=True)
    with c2: st.checkbox("Mercado Livre", value=True)
    with c3: st.checkbox("Shopee", value=True)
    
    c4, c5 = st.columns(2)
    with c4: st.checkbox("Shein", value=True)
    with c5: st.checkbox("Shopintegra", value=True)

# 4. LÓGICA DE GERAÇÃO COM GATILHOS MENTAIS
if st.button("🚀 Gerar 5 Mensagens Irresistíveis", type="primary"):
    if not nome_produto or not preco:
        st.warning("Por favor, preencha o nome e o preço para continuar.")
    else:
        with st.spinner('A IA está criando a necessidade de compra agora...'):
            prompt_vendas = f"""
            Atue como um mestre em Neuro-Copywriting. 
            Crie 5 variações de textos para vender o produto: {nome_produto}.
            Preço: R$ {preco}.
            Características: {descricao}.

            REQUISITOS DE ALTA CONVERSÃO:
            - Use o Gatilho da ESCASSEZ (ex: 'Restam poucos pares').
            - Use o Gatilho da URGÊNCIA (ex: 'O cupom expira em breve').
            - Use o Gatilho da EXCLUSIVIDADE (ex: 'Feito para quem exige o melhor').
            - Foque na NECESSIDADE de ter o produto agora para resolver um desejo ou dor.
            - Linguagem direta, com emojis e CTA (Chamada para Ação) clara.
            """
            
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "Você é um especialista em vendas psicológicas."},
                              {"role": "user", "content": prompt_vendas}]
                )
                
                output = response.choices[0].message.content
                st.markdown("### 💬 Mensagens Geradas")
                st.info("Copie e cole nos seus grupos ou stories!")
                st.write(output)
                
            except Exception as e:
                st.error(f"Erro ao gerar: {e}")

# Rodapé
st.markdown("<br><hr><center>✨ Luhvees - Neuro-Copywriting Generator <br> 📱 @luhveestore</center>", unsafe_allow_html=True)
