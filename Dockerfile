# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia todo o código para o container
COPY . .

# Comando padrão ao iniciar o container: executa os testes
CMD ["python", "-m", "unittest", "discover", "tests"]