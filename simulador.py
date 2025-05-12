import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Conta Certa", layout="centered")

st.title("💰 Conta Certa – Simulador de Orçamento Pessoal")
st.markdown("Insira sua **renda mensal** e os **gastos por categoria** para ver como está sua saúde financeira.")

# 1. Entrada de dados
st.header("1️⃣ Renda Mensal")
salario = st.number_input("🏠 Salário:", min_value=0.0, step=10.0, format="%.2f")
auxilio = st.number_input("🍲 Bolsa/Auxílio:", min_value=0.0, step=10.0, format="%.2f")
bicos = st.number_input("🚌 Bicos/Trabalhos extras:", min_value=0.0, step=10.0, format="%.2f")
outros = st.number_input("🩺 Outros:", min_value=0.0, step=10.0, format="%.2f")
total_receitas = sum([salario, auxilio, bicos, outros])
st.success(f"**Total de Receitas:** R$ {total_receitas:.2f}")

st.header("2️⃣ Despesas por Categoria")
moradia = st.number_input("🏠 Moradia (aluguel, luz, água):", min_value=0.0, step=10.0, format="%.2f")
alimentacao = st.number_input("🍲 Alimentação:", min_value=0.0, step=10.0, format="%.2f")
transporte = st.number_input("🚌 Transporte:", min_value=0.0, step=10.0, format="%.2f")
saude = st.number_input("🩺 Saúde:", min_value=0.0, step=10.0, format="%.2f")
educacao = st.number_input("📚 Educação:", min_value=0.0, step=10.0, format="%.2f")
lazer = st.number_input("🎉 Lazer:", min_value=0.0, step=10.0, format="%.2f")
outras = st.number_input("🛒 Outras Despesas:", min_value=0.0, step=10.0, format="%.2f")
total_despesas = sum([moradia, alimentacao, transporte, saude, educacao, lazer, outras])
st.error(f"**Total de Despesas:** R$ {total_despesas:.2f}")

# 2. Cálculos
saldo = total_receitas - total_despesas

st.header("3️⃣ Resultado do Mês")
st.write(f"**Total de Receitas:** R$ {total_receitas:.2f}")
st.write(f"**Total de Despesas:** R$ {total_despesas:.2f}")
st.write(f"**Saldo Final (Renda - Despesas):** R$ {saldo:.2f}")

# 3. Saída visual – Gráfico
st.subheader("📊 Distribuição das Despesas")
categorias = ["Moradia", "Alimentação", "Transporte", "Saúde", "Educação", "Lazer", "Outras"]
valores = [moradia, alimentacao, transporte, saude, educacao, lazer, outras]

if total_despesas > 0:
    fig, ax = plt.subplots()
    ax.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.success("Adicione valores às despesas para ver o gráfico.")

# 4. Dicas e Recomendações
st.header("💡 Dicas Financeiras")
if saldo > 0:
    st.info("Parabéns! Você fechou o mês no azul. Considere guardar parte do saldo como reserva de emergência ou investir em algo seguro.")
elif saldo < 0:
    st.error("Atenção! Você gastou mais do que ganhou. Reveja seus gastos e tente cortar despesas não essenciais.")
else:
    st.warning("Você fechou o mês zerado. Que tal tentar economizar um pouquinho no próximo?")
