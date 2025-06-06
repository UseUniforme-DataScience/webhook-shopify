FROM python:3.11-slim

# Define timezone
ENV TZ=America/Sao_Paulo

# Instala tzdata e outras dependências essenciais
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da raiz do projeto local para o container
COPY . .

# Cria venv interna (exclusiva do container)
RUN python -m venv /opt/venv

# Ativa a venv no PATH do container
ENV PATH="/use-api/venv/bin:$PATH"

# Instala dependências dentro da venv
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9100"]
