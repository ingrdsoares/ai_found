import click
import ollama
import PyPDF2
import os

# --- Configuration ---
DEFAULT_MODEL = 'llama3'
MAX_TEXT_LENGTH_FOR_PROMPT = 4000

@click.group()
def cli():
    """CLI tool for PDF summarization using AI."""
    pass

@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True))
def summarize(pdf_path):
    """Summarizes a PDF file using the configured Ollama model."""
    click.echo(f"Processing PDF: {pdf_path}")
    
    try:
        text_content = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            click.echo(f"Found {num_pages} page(s) in the PDF.")
            
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                if page_text:
                    text_content += page_text + "
"

        if not text_content.strip():
            click.echo("Error: Could not extract text from the PDF. It might be image-based or empty.")
            return

        if len(text_content) > MAX_TEXT_LENGTH_FOR_PROMPT:
            click.echo(f"Warning: PDF content truncated to fit model's context window ({MAX_TEXT_LENGTH_FOR_PROMPT} characters).")
            text_content = text_content[:MAX_TEXT_LENGTH_FOR_PROMPT]

        click.echo("Text extracted successfully. Sending to AI for summarization...")

        try:
            response = ollama.chat(model=DEFAULT_MODEL, messages=[
                {
                    'role': 'user',
                    'content': f"Please provide a concise summary of the following document:

{text_content}",
                },
            ])
            
            summary = response['message']['content']
            click.echo("
--- AI Generated Summary ---")
            click.echo(summary)

        except ollama.ResponseError as e:
            click.echo(f"Ollama API Error: {e}")
            click.echo("Please ensure Ollama is running and the 'llama3' model is available (ollama pull llama3).")
        except Exception as e:
            click.echo(f"An unexpected error occurred during AI processing: {e}")

    except FileNotFoundError:
        click.echo(f"Error: The file '{pdf_path}' was not found.")
    except PyPDF2.errors.PdfReadError:
        click.echo(f"Error: Could not read PDF file '{pdf_path}'. It might be encrypted, corrupted, or an unsupported format.")
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    cli()
