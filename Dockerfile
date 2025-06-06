FROM python:3.11-slim

# Define timezone
ENV TZ=America/Sao_Paulo

# Instala tzdata e outras dependências essenciais
RUN apt-get update && \
    apt-get install -y tzdata nano git && \
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
ENV PATH="/webhook-shopify/venv/bin:$PATH"

# Instala dependências dentro da venv
RUN pip install --no-cache-dir -r requirements.txt

# Define o caminho raiz para módulos Python
ENV PYTHONPATH=/webhook-shopify

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1	

# Comando de execução (gunicorn com uvicorn)
CMD ["gunicorn", "-w", "4", "--threads", "2", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:9000"]