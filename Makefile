# Variáveis - APONTANDO DIRETAMENTE PARA O VENV
PYTHON = ./venv/bin/python
PIP = ./venv/bin/pip
MODEL = llama3.2
PDF_FILE = Pdf_Exemplo.pdf

.PHONY: all setup serve run check clean

# Comando padrão
all: setup

# 1. Setup: Instala dependências, baixa modelo e VERIFICA com ollama list
setup: install pull check
	@echo "✅ Setup concluído e verificado!"

install:
	@echo "📦 Instalando dependências no venv..."
	$(PIP) install ollama pypdf click

pull:
	@echo "📥 Baixando o modelo $(MODEL)..."
	ollama pull $(MODEL)

# Comando de Verificação (Onde entra o ollama list)
check:
	@echo "📋 Verificando modelos instalados..."
	ollama list

# 2. Servidor
serve:
	@echo "🚀 Iniciando servidor Ollama..."
	ollama serve

# 3. Execução
# Para rodar com o arquivo padrão: make run
# Para rodar com outro arquivo: make run FILE=outro.pdf
run:
	$(eval FINAL_FILE := $(if $(FILE),$(FILE),Pdf_Exemplo.pdf))
	@echo "🔍 Sumarizando o arquivo: $(FINAL_FILE)..."
	$(PYTHON) main.py summarize "$(FINAL_FILE)"

clean:
	@echo "🧹 Limpando arquivos temporários..."
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
