# AI-Powered PDF Summarizer CLI

Este projeto é uma ferramenta de interface de linha de comando (CLI) que utiliza IA para sumarizar documentos PDF. Ele utiliza o Ollama com o modelo Llama 3.2 para inferência de IA local e a biblioteca pypdf para a análise (parsing) de PDFs.

## Setup

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/ingrdsoares/ai_found.git
    cd pdf-summarizer-cli
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # No Windows use: .\venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install ollama pypdf click
    ```
4.  **Certifique-se de que o Ollama está rodando e o modelo Llama 3.2 está disponível:**
    Certifique-se de que o Ollama está rodando em segundo plano e que você baixou o modelo 'llama3.2' executando `ollama pull llama3.2`.

## Usage

```bash
python main.py summarize <caminho_para_seu_arquivo.pdf>
```

**Exemplo:**
```bash
python main.py summarize ./meu_documento.pdf
```

## Project Structure

*   `venv/`: Ambiente virtual Python.
*   `main.py`: O script principal da ferramenta CLI.
*   `.gitignore`: Especifica os arquivos que o Git deve ignorar.
*   `README.md`: Este arquivo, fornecendo a visão geral do projeto e instruções.

## Implementation Details

- **AI Model:** Llama 3.2 (via Ollama)
- **PDF Engine:** pypdf
- **CLI Framework:** Click
- **Text Handling:** Implementada a truncagem da janela de contexto (4.000 caracteres) para garantir a compatibilidade com os limites do modelo.
EOF
