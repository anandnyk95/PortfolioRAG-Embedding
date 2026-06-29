import json
import os
from services.resume_loader import load_resume
from services.chunking import chunk_text
from services.embedding import get_embedding

def create_embeddings():
    print("Step 1: Loading resume...")
    text = load_resume()

    print("Step 2: Chunking text...")
    chunks = chunk_text(text)
    print(f"Total chunks: {len(chunks)}")

    print("Step 3: Creating embeddings...")
    data = []
    for i, chunk in enumerate(chunks):
        print(f"  Embedding chunk {i + 1}/{len(chunks)}...")
        vector = get_embedding(chunk)
        data.append({
            "chunk": chunk,
            "embedding": vector
        })

    print("Step 4: Saving to embeddings.json...")
    output_path = os.path.join(os.path.dirname(__file__), "embeddings.json")
    with open(output_path, "w") as f:
        json.dump(data, f)

    print(f"Done! {len(data)} chunks saved to embeddings.json ✅")

if __name__ == "__main__":
    create_embeddings()