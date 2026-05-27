# Relatório Técnico: Sumarizador de PDFs com IA Local (Ollama)
**Kensei CyberSec Lab | AI Foundations 2026**

## 1. Visão Geral do Projeto
O objetivo deste projeto foi desenvolver uma ferramenta de interface de linha de comando (CLI) capaz de ler arquivos PDF e gerar resumos automáticos utilizando inteligência artificial processada localmente. A escolha por IA local visa garantir a privacidade dos dados e a independência de APIs pagas.

## 2. Tecnologias Utilizadas
- **Linguagem:** Python 3.9
- **Modelo de IA:** Llama 3.2 (via Ollama)
- **Processamento de PDF:** `pypdf` (extração de texto bruto)
- **Interface CLI:** `click` (gerenciamento de argumentos e comandos)
- **Controle de Versão:** Git & GitHub

## 3. Arquitetura e Implementação
### 3.1 Fluxo de Funcionamento
1. **Entrada:** O usuário fornece o caminho de um arquivo PDF via comando `summarize`.
2. **Extração:** O sistema utiliza a biblioteca `pypdf` para percorrer todas as páginas do documento e consolidar o texto.
3. **Pré-processamento:** Implementou-se um limite de caracteres (4.000) para evitar que o volume de texto exceda a janela de contexto do modelo de IA.
4. **Inferência:** O texto extraído é enviado ao modelo Llama 3.2 através da API local do Ollama com um prompt específico para sumarização concisa.
5. **Saída:** O resumo gerado é retornado e exibido diretamente no terminal do usuário.

### 3.2 Desafios Técnicos e Soluções
- **Erro de Sintaxe (String Literals):** Durante o desenvolvimento, a manipulação de caracteres de nova linha (`
`) causou erros de sintaxe no interpretador. A solução foi a implementação de `chr(10)`, garantindo a compatibilidade do código.
- **Dependências de Biblioteca:** A migração de `PyPDF2` para `pypdf` foi necessária para alinhar o código com a versão mais recente e estável da biblioteca.
- **Limites de Contexto:** Para evitar falhas na API do Ollama, foi implementada a truncagem do texto, garantindo que o prompt fosse processado com sucesso independentemente do tamanho do PDF.

## 4. Resultados Alcançados
A ferramenta demonstrou eficácia na leitura de documentos PDF e na geração de resumos coerentes, processando arquivos de múltiplas páginas (ex: 16 páginas) e entregando a essência do conteúdo em poucos segundos.

## 5. Conclusão e Próximos Passos
O MVP (Minimum Viable Product) foi entregue com sucesso, cumprindo os requisitos da Trilha C. Como melhorias futuras, planeja-se:
- Implementar OCR para PDFs baseados em imagem.
- Adicionar suporte a múltiplos modelos de IA.
- Implementar a exportação do resumo para arquivos `.txt` ou `.md`.
EOF
