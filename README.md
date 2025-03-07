# Chat with PDF using OpenAI LLM API and Gradio

## Overview
This project is a chatbot application that allows users to upload a text-based PDF file, extract its content, and interact with it by asking questions. The chatbot leverages LLM API and a vector-based retrieval system to generate context-aware responses based on the uploaded document. The user interface is built with Gradio for an interactive and user-friendly experience.

## Tech Stack
- **Python (3.9+)**
- **Gradio** (for UI development)
- **OpenAI API / Groq LLM API** (for natural language processing)
- **LangChain** (for conversational retrieval chains)
- **PyPDF2** (for PDF text extraction)
- **FAISS** (for storing and searching vector embeddings)
- **Hugging Face Sentence Transformers** (for embedding generation)
- **dotenv** (for environment variable management)

## Setup and Installation
### Prerequisites
Ensure you have Python 3.9+ installed on your system. You also need an OpenAI or Groq API key to interact with the LLM.

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/pdf-chatbot.git
   cd pdf-chatbot
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables:**
   Create a `.env` file in the project root and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Running the Application
To start the chatbot, run:
```bash
python app.py
```
This will launch the Gradio interface in your browser.

## Usage
1. Upload a text-based PDF file.
2. Click "Process PDF" to extract its content.
3. Start asking questions about the document through the chat interface.

## Project Structure
```
├── app.py               # Main application script
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
├── utils/               # Helper functions (if any)
├── README.md            # Project documentation
```
