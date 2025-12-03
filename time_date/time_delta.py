# OPERAÇÕES COM DATA E HORA
from datetime import datetime, timedelta, date, time

tipo_carro  = "m"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "p":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro  chegou: {data_atual}\nFicará pronto: {data_estimada}")
elif tipo_carro == "m":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro  chegou: {data_atual}\nFicará pronto: {data_estimada}")   
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro  chegou: {data_atual}\nFicará pronto: {data_estimada}")     

# MANIPULAR DIA
print(date.today() - timedelta(days=1))

# MANIPULAR HORA
resultado = datetime(2025, 12,  3, 10, 19, 20) - timedelta(hours=1) #PRECISA CRIAR A DATA COMPLETA
print(resultado.time()) 

print(datetime.now().date())