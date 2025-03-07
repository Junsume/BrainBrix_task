import os
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PDFChatbot:
    def __init__(self):
        # Load API key from environment
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        # Initialize LLM (ChatGroq)
        self.llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")
        
        # Load Embedding Model
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        # Initialize placeholders
        self.vectorstore = None
        self.chat_history = []

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
            
            return "PDF processed successfully! You can now ask questions."
        
        except Exception as e:
            return f"Error processing PDF: {str(e)}"

    def chat(self, query):
        """Retrieves relevant text from the PDF and generates an AI response."""
        if not self.vectorstore:
            return "Please upload and process a PDF first."

        try:
            # Retrieve relevant documents
            retrieved_docs = self.vectorstore.similarity_search(query, k=3)
            retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
            
            # Create conversational retrieval chain dynamically
            qa_chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm, 
                retriever=retriever,
                return_source_documents=True
            )
            
            # Process user query with chat history
            result = qa_chain({
                "question": query, 
                "chat_history": self.chat_history
            })

            response = result['answer']
            self.chat_history.append((query, response))

            return response
        
        except Exception as e:
            return f"Error in processing query: {str(e)}"


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
