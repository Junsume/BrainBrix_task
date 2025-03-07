import os
import gradio as gr
import openai  # Import OpenAI for setting API key
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()

class PDFChatbot:
    def __init__(self):
        """Initializes the chatbot with OpenAI API and necessary components."""
        # Load API key from environment
        self.api_key = os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError("⚠️ OPENAI_API_KEY is missing! Set it in .env or system environment variables.")

        # Set API key for OpenAI
        openai.api_key = self.api_key  # ✅ Fix 4

        # Initialize LLM (OpenAI GPT Model)
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)  # ✅ Using GPT-3.5 Turbo for better response

        # Load Embedding Model (Pass API key)
        self.embeddings = OpenAIEmbeddings(api_key=self.api_key)  # ✅ Fix 1
        
        # Initialize placeholders
        self.vectorstore = None
        self.qa_chain = None  # ✅ Store the chain once
        self.chat_history = []  # ✅ Store as a list of tuples

    def process_pdf(self, pdf_path):
        """Processes the uploaded PDF: extracts text, creates embeddings, and stores in FAISS."""
        try:
            # Load PDF and extract text
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()

            # Split text into smaller chunks for efficient retrieval
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, 
                chunk_overlap=200
            )
            texts = text_splitter.split_documents(documents)

            # Create FAISS vector store
            self.vectorstore = FAISS.from_documents(texts, self.embeddings)

            # Create retriever from FAISS
            retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})

            # ✅ Initialize the QA chain once here (Fix 2)
            self.qa_chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm, 
                retriever=retriever,
                return_source_documents=True
            )

            return "✅ PDF processed successfully! You can now ask questions."
        
        except Exception as e:
            return f"❌ Error processing PDF: {str(e)}"

    def chat(self, query):
        """Retrieves relevant text from the PDF and generates an AI response."""
        if not self.qa_chain:
            return "⚠️ Please upload and process a PDF first."

        try:
            # Process user query with chat history
            result = self.qa_chain({
                "question": query, 
                "chat_history": self.chat_history  # ✅ Fix 3 (history as list of tuples)
            })

            response = result['answer']
            self.chat_history.append((query, response))  # ✅ Store as tuple

            return response
        
        except Exception as e:
            return f"❌ Error in processing query: {str(e)}"


def create_interface():
    """Creates the Gradio interface for the PDF chatbot."""
    chatbot = PDFChatbot()

    def process_file(file):
        return chatbot.process_pdf(file.name)

    def chat_response(message, history):
        return chatbot.chat(message)

    with gr.Blocks() as demo:
        gr.Markdown("# 📄 PDF Chat Assistant")
        
        with gr.Row():
            pdf_input = gr.File(
                type="filepath", 
                file_types=[".pdf"], 
                label="Upload PDF"
            )
            process_btn = gr.Button("Process PDF")
        
        status_output = gr.Textbox(label="Status")
        
        chatbot_interface = gr.ChatInterface(
            fn=chat_response,
            title="Chat with your PDF",
            description="Ask questions about the uploaded PDF"
        )

        process_btn.click(
            process_file, 
            inputs=pdf_input, 
            outputs=status_output
        )

    return demo

def main():
    interface = create_interface()
    interface.launch(share=True)

if __name__ == "__main__":
    main()
