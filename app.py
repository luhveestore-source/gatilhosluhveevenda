import streamlit as st
import google.generativeai as genai

# --- 1. IDENTIDADE VISUAL (Estilo Luhvee Stores) ---
st.set_page_config(page_title="Central Luhvees Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2, h3 { color: #da70d6 !important; }
    .stButton>button { background: linear-gradient(45deg, #ff69b4, #da70d6); color: white; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA IA (Segurança via Secrets) ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
    model = genai.GenerativeModel(model_name)
except Exception as e:
    st.error(f"Erro na conexão com a IA: {e}")
    st.stop()

# --- 3. BANCO DE LINKS OFICIAIS LUHVEES ---
LINKS = {
    "Shopee": "https://collshp.com/luhveestores?view=storefront",
    "Shein": "https://onelink.shein.com/5/5ohwd5nol825",
    "Mercado Livre": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "Hub": "https://links-luhveestore.streamlit.app/",
    "Shopintegra": "https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes",
    "WhatsApp": "https://wa.me/5511948021428",
    "Instagram": "@luhveestore"
}

# --- 4. NAVEGAÇÃO LATERAL (Apenas as 3 abas principais) ---
aba = st.sidebar.radio("Selecione o que postar:", ["👠 Calçados (Shoes)", "🎁 Achadinhos", "💬 Mensagens de Grupo"])

# --- PILAR 1: CALÇADOS (Foco em Quebra de Objeções) ---
if aba == "👠 Calçados (Shoes)":
    st.subheader("👟 Gerador Luhvee Shoes - Neurocopy Ativada")
    nome_calca = st.text_input("Nome do Produto / REF.")
    valor_calca = st.text_input("Preço (R$)")
    desc_calca = st.text_area("Descrição Técnica (Cole aqui os detalhes de material, solado, etc.)")

    if st.button("🚀 GERAR POST DE CALÇADOS"):
        if nome_calca and valor_calca:
            copy_shoes = f"""😤 CANSADO DE PROCURAR?

{nome_calca.upper()} ORIGINAL está AQUI! 👈

Sem fake, sem enganação! ✅

{desc_calca}

💰 R$ {valor_calca}

Fim da busca! 🎉

🛒 COMPRE AGORA:
🏪 Catálogo: {LINKS['Shopintegra']}

💬 WhatsApp: {LINKS['WhatsApp']}

💳 Formas de Pagamento:
✅ Cartão de Crédito
✅ Link de Pagamento
✅ PIX

📲 Instagram: {LINKS['Instagram']}
🔗 Mais Links: {LINKS['Hub']}"""
            st.text_area("Pronto para copiar:", copy_shoes, height=450)
        else:
            st.warning("Preencha o Nome e o Valor.")

# --- PILAR 2: ACHADINHOS (Neurocopy de Resposta Rápida) ---
elif aba == "🎁 Achadinhos":
    st.subheader("🎁 Gerador de Achadinhos Sem Rodeios")
    prod_achado = st.text_input("Nome do Produto")
    preco_achado = st.text_input("Preço")
    loja = st.selectbox("Escolha a Loja:", ["Shopee", "Shein", "Mercado Livre"])

    if st.button("🚀 GERAR MENSAGENS"):
        if prod_achado and preco_achado:
            with st.spinner("IA aplicando gatilhos subconscientes de compra..."):
                prompt = f"""
                Atue como copywriter especialista em Neuromarketing e Neurocopy para e-commerce.
                Crie textos EXTREMAMENTE CURTOS, DIRETOS E SEM ENROLAÇÃO para: {prod_achado} por R$ {preco_achado}.
                
                Use gatilhos de:
                - Curiosidade (fazer a pessoa querer clicar para ver)
                - Ganho de oportunidade (preço exclusivo ou achado imperdível)
                - Escassez implícita (agir rápido)
                
                Forneça o texto final pronto estruturado assim:
                
                📸 **INSTAGRAM:**
                [Texto curto, focado no desejo visual e estético do produto + Emojis]
                
                💬 **WHATSAPP / TELEGRAM:**
                [Mensagem rápida de um clique, gerando urgência de estoque]
                
                📱 **STATUS / STORIES:**
                [Uma frase matadora de no máximo 2 linhas para gerar o clique por impulso]
                """
                response = model.generate_content(prompt)
                
                rodapie_links = f"\n\n🛒 **LINK PARA COMPRAR:**\n🔗 {LINKS[loja]}\n\n🌐 **VEJA TODOS OS ACHADINHOS:**\n👉 {LINKS['Hub']}\n\n🔥 **ENTRE NO GRUPO VIP:**\n📱 {LINKS['WhatsApp']}"
                
                st.text_area("Copies com Alta Conversão:", f"{response.text}{rodapie_links}", height=500)
        else:
            st.warning("Preencha o produto e o preço.")

# --- PILAR 3: MENSAGENS DE GRUPO (Combo Motivacional de Todos os Períodos) ---
elif aba == "💬 Mensagens de Grupo":
    st.subheader("💬 Máquina de Engajamento - Mensagens do Dia")
    contexto_extra = st.text_input("Gatilho ou Tema do Dia:", placeholder="Ex: Sabadou com a Shopee, friozinho gostoso, início de mês...")

    if st.button("🚀 GERAR TODAS AS MENSAGENS DO DIA"):
        with st.spinner("IA criando o combo de saudações motivacionais..."):
            tema = contexto_extra if contexto_extra else "um dia abençoado e cheio de mimos"
            prompt_grupo = f"""
            Atue como copywriter especialista em Neuromarketing e Engajamento de Comunidades para a marca 'Luhvees'.
            Crie 3 mensagens de grupo independentes, muito simples, curtas e altamente MOTIVACIONAIS baseadas no tema: '{tema}'.
            
            Regras de Neurocopy, Conexão e Praticidade:
            - Use o gatilho de Pertencimento (fazer com que se sintam acolhidas em um clube VIP).
            - Mensagens muito diretas, limpas, doces e sem NENHUMA enrolação ou textão cansativo.
            - Coloque obrigatoriamente a marcação '@todos' bem visível e destacada em cada mensagem para chamar a atenção de todos no grupo.
            
            Formate a saída EXATAMENTE com essa estrutura abaixo:
            
            🌞 **MENSAGEM DE BOM DIA (MANHÃ):**
            [Saudação super animada 'Bom dia, Luhvees! ✨' + Frase motivacional bem simples, curta e forte incluindo o tema + Convite leve para dar uma olhadinha no grupo hoje + @todos]
            
            🌆 **MENSAGEM DE BOA TARDE (TARDE):**
            [Saudação carinhosa de tarde + Mensagem rápida de incentivo e energia para o resto do dia + Lembrete rápido dos mimos + @todos]
            
            🌙 **MENSAGEM DE BOA NOITE (NOITE):**
            [Mensagem fofa de encerramento do dia + Palavra de gratidão, descanso e motivação para renovar as energias + @todos]
            """
            response = model.generate_content(prompt_grupo)
            
            rodapie_grupo = f"\n\n🛍️ **LINKS RÁPIDOS PARA COMPRAR HOJE:**\n🌐 Nosso Hub Oficial: {LINKS['Hub']}\n👟 Catálogo Shoes: {LINKS['Shopintegra']}\n🎁 Achadinhos Shopee: {LINKS['Shopee']}"
            
            st.text_area("Mensagens Prontas (Manhã, Tarde e Noite):", f"{response.text}{rodapie_grupo}", height=600)
