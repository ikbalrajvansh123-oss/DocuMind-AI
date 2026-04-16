import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


st.set_page_config(page_title="AI PDF Chatbot", page_icon="📄")
st.title("📄 AI PDF Chatbot")


# Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# Process PDFs
@st.cache_resource
def process_pdfs(files):
    documents = []

    for file in files:
        with open(file.name, "wb") as f:
            f.write(file.read())

        loader = PyPDFLoader(file.name)
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    docs = splitter.split_documents(documents)

    # ✅ LOCAL embeddings (NO HF API issue)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        docs,
        embedding=embeddings
    )

    return vectorstore.as_retriever(search_kwargs={"k": 4})


# Upload PDFs
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)


if uploaded_files:

    with st.spinner("Indexing PDFs..."):
        retriever = process_pdfs(uploaded_files)

    # LLM
    llm = ChatGroq(
        groq_api_key=st.secrets["GROQ_API_KEY"],
        model="llama3-70b-8192",
        streaming=True
    )

    system_prompt = (
        "Use the following context to answer the question. "
        "If you don't know the answer, say you don't know.\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}\n\nChat History:\n{chat_history}")
        ]
    )

    qa_chain = create_stuff_documents_chain(llm, prompt)

    rag_chain = create_retrieval_chain(
        retriever,
        qa_chain
    )

    question = st.chat_input("Ask something about the PDFs")

    if question:

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            placeholder = st.empty()
            answer = ""

            chat_history = "\n".join(
                [f"{m['role']}: {m['content']}" for m in st.session_state.messages]
            )

            with st.spinner("Thinking..."):

                response = rag_chain.invoke({
                    "input": question,
                    "chat_history": chat_history
                })

                full_answer = response["answer"]

                for word in full_answer.split():
                    answer += word + " "
                    placeholder.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        # Sources
        with st.expander("📚 Sources"):
            for doc in response["context"]:
                st.write(
                    f"Page: {doc.metadata.get('page')} | Source: {doc.metadata.get('source')}"
                )