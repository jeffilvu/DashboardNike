import streamlit as st
import pandas as pd

maiorvenda = 0
st.set_page_config(page_title='DASHBOARD')
menu_option = st.sidebar.radio(" ", ["Resultados", "Contratos","Nosso Time!"])



def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela


col1, col2 = st.columns(2)


with col2:
        st.subheader("Bem vindo ao Dashboard mensal da Nike!")
        
        st.subheader("Olá, Colaborador!")
        st.write("[Acompanhe o Instagram!](https://www.instagram.com/nike/)")
        st.write("[Acompanhe o Twitter!](https://twitter.com/nike)")
        st.write("[Acompanhe o Youtube!](https://www.youtube.com/@nike)")
    
    
with col1:
    image = "logo.jpg"
    st.image(image, width=250)



if menu_option == "Contratos":
        st.write("---")
        st.title("Relações Contratuais")
        st.write("Confira informações sobre os contratos fechados com os atletas neste mês:")
        
        dados_contratuais = "dados_contratuais.xlsx"
        relacoes_contratuais = pd.read_excel(dados_contratuais)
        st.write(relacoes_contratuais)
        
        st.write("---")
        
elif menu_option == "Nosso Time!":
        st.write("---")
        st.title("Nosso Time")
        
        st.write("A essência central da Nike reside na sua celebração da diversidade. Desde sua fundação, a marca abraçou a pluralidade em todas as formas - seja cultural, étnica, ou de gênero. Através de suas campanhas e iniciativas, a Nike não apenas reconhece, mas também valoriza a riqueza que a diversidade traz para o mundo do esporte e além. Para a Nike, a diversidade não é apenas um valor, mas sim a força motriz que impulsiona sua inovação, criatividade e excelência.")
        
        
        st.write("---")
        
        st.title("Embaixador")
        

elif menu_option == "Resultados":
    with st.container():
    
        st.write("---")
        st.title("Resultados")
        st.write("Confira as metas que foram alcançadas!")
        st.write("---")
        st.title("Vendas")
        qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
        num_dias = int(qtde_dias.replace("D", ""))
        dados = carregar_dados()
        dados = dados[-num_dias:]
        st.area_chart(dados, x="Data", y="Vendas")
        
        
        for venda in dados['Vendas']:
            if venda > maiorvenda:
                maiorvenda = venda
        
        st.subheader(f"Nosso recorde de vendas em um dia foi de {maiorvenda} produtos vendidos!!")
        
        st.write("---")
        st.title("Principais Produtos")
        
    with st.container():
        col1, col2, col3,col4,col5,col6 = st.columns(6)
        
        with col1:
            image = "airforce.jpg"
            st.image(image, width=250,caption="Tênis Air Force Branco Unissex")
        
        with col4:
            image = "mochila.jpg"
            st.image(image, width=250, caption="Mochila Rosa")