# AI-Powered PDF Summarizer CLI

This project is a command-line interface (CLI) tool that uses AI to summarize PDF documents. It leverages Ollama with the Llama 3.2 model for local AI inference and pypdf for PDF parsing.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ingrdsoares/ai_found.git
    cd pdf-summarizer-cli
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install ollama pypdf click
    ```
4.  **Ensure Ollama is running and Llama 3.2 model is available:**
    Make sure Ollama is running in the background and you have pulled the 'llama3.2' model by running `ollama pull llama3.2`.

## Usage

```bash
python main.py summarize <path_to_your_pdf.pdf>
```

**Example:**
```bash
python main.py summarize ./my_document.pdf
```

## Project Structure

*   `venv/`: Python virtual environment.
*   `main.py`: The main script for the CLI tool.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `README.md`: This file, providing project overview and instructions.

## Implementation Details

- **AI Model:** Llama 3.2 (via Ollama)
- **PDF Engine:** pypdf
- **CLI Framework:** Click
- **Text Handling:** Implemented context window truncation (4000 chars) to ensure compatibility with model limits.
EOF
