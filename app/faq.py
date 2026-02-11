import pandas as pd 
from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()


faqs_path = Path(__file__).parent/"resources/faq_data.csv"

chroma_client = chromadb.Client()
collection_name_faq = "faqs"
ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/all-MiniLM-L6-v2")

def ingest_faq_data(path):
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print("Ingesting data into Chromadb....")
        df = pd.read_csv(path)
        
        collection = chroma_client.get_or_create_collection(
            name=collection_name_faq,
            embedding_function=ef
        )

        docs = df["question"].to_list()
        metadata = [{"answer":ans} for ans in df["answer"].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]

        collection.add(documents=docs,
                    metadatas=metadata,
                    ids=ids)
        
        print(f"Data ingested successfullt into Chroma collection:{collection_name_faq}")
    else:
        print(f"Collection {collection_name_faq} already exists")


def get_relevant_qa(query):
    collection = chroma_client.get_collection(name=collection_name_faq)
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result

def faq_chain(query):
    result = get_relevant_qa(query)
    context = "\n\n".join([r["answer"] for r in result['metadatas'][0]])
    answer = generate_answer(query,context)
    return answer     

def generate_answer(query,context):    
    prompt = f"""
    Given the question and context below, generate the answer based on the context only.
    If you don't find the answer inside the context then say "I don't know".
    Do not make things up. 

    QUESTION: {query}

    CONTEXT: {context}
    
    """

    client = Groq()
    completion = client.chat.completions.create(
        model=os.environ["GROQ_MODEL"],
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ],
        temperature=0,
        max_completion_tokens=512,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )
    
    return completion.choices[0].message.content



if __name__ == "__main__":
    ingest_faq_data(faqs_path)
    query = "What is your policy on defective products ?"
    # result = get_relevant_qa(query)
    answer = faq_chain(query)
    print(answer)