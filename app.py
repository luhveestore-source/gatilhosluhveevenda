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

# --- 4. NAVEGAÇÃO LATERAL (Apenas as 3 abas desejadas) ---
aba = st.sidebar.radio("Selecione o que postar:", ["👠 Calçados (Shoes)", "🎁 Achadinhos", "💬 Mensagens de Grupo"])

# --- PILAR 1: CALÇADOS ---
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

# --- PILAR 2: ACHADINHOS ---
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

# --- PILAR 3: MENSAGENS DE GRUPO (Design Premium & Motivacional) ---
elif aba == "💬 Mensagens de Grupo":
    st.subheader("💬 Máquina de Engajamento - Mensagens Premium")
    
    # Nova função para você escolher qual link padrão vai querer embutido na mensagem
    link_destino = st.selectbox("Escolha para onde mandar o cliente nessa mensagem:", ["Shopee", "Shein", "Mercado Livre", "Hub", "Shopintegra"])
    contexto_extra = st.text_input("Tema de Motivação do Dia:", placeholder="Ex: Foco no sucesso, Sabadou de conquistas, Superar limites...")

    if st.button("🚀 GERAR COMBO DE MENSAGENS ESTILIZADAS"):
        with st.spinner("IA aplicando design visual de alta conversão..."):
            tema = contexto_extra if contexto_extra else "paz, conquistas e muito amor próprio"
            link_selecionado = LINKS[link_destino]

            prompt_grupo = f"""
            Atue como copywriter especialista em Neuromarketing e Design de Mensagens para WhatsApp.
            Crie 3 blocos de mensagens separados (MANHÃ, TARDE, NOITE). Elas devem ser curtas, altamente MOTIVACIONAIS baseadas no tema: '{tema}'.
            
            Regra Crucial de Formatação Visual (Deixe idêntico a um catálogo elegante de vendas):
            - Use títulos principais em CAIXA ALTA acompanhados de emojis temáticos fortes.
            - Apresente os benefícios motivacionais ou listas usando tópicos limpos com o marcador '✨' ou '✔️'.
            - Deixe espaçamentos organizados (pule linhas entre blocos para não virar textão).
            - Insira de forma muito natural a chamada de urgência/escassez no final do texto (ex: '🔥 Oportunidades exclusivas aguardando você!', '⚠️ Estoque atualizado por tempo limitado!').
            - O marcador '@todos' deve ficar isolado e bem visível no final de cada período.
            
            Retorne EXATAMENTE esta estrutura para que eu mostre na tela:
            
            🌞 **MENSAGEM DE BOM DIA (MANHÃ):**
            [Título em Caixa Alta com Emoji]
            [Mensagem motivacional curta sobre o tema]
            ✨ Mensagem de inspiração 1
            ✨ Mensagem de inspiração 2
            🔥 Mimos imperdíveis prontos para você!
            👉 Link para acessar: {link_selecionado}
            @todos
            
            🌆 **MENSAGEM DE BOA TARDE (TARDE):**
            [Título em Caixa Alta com Emoji]
            [Incentivo rápido para a tarde render]
            ✔️ Foco e energia renovada
            ✔️ Dê uma espiadinha nas novidades de hoje
            ⚡ Clique antes que acabe!
            👉 Link oficial: {link_selecionado}
            @todos
            
            🌙 **MENSAGEM DE BOA NOITE (NOITE):**
            [Título em Caixa Alta com Emoji]
            [Frase de gratidão e descanso]
            ✨ O amanhã reserva coisas incríveis
            🛌 Descanse com a certeza de dever cumprido
            ❤️ Amanhã tem reposição especial!
            👉 Veja tudo aqui: {link_selecionado}
            @todos
            """
            response = model.generate_content(prompt_grupo)
            
            st.text_area("Copie o período desejado:", response.text, height=650)
