from flask import Flask, render_template, request, jsonify
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex  # Ensure this import is correct for your library

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    folder_path = request.form[r'folder_path']
    question = request.form['question']

    
    try:
        os.environ["OPENAI_API_KEY"]="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"
        # Load documents from the specified folder path
        # Load documents from the specified folder path
        documents = SimpleDirectoryReader(folder_path, recursive=True).load_data()
        
        # Create and query the index
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine(similarity_top_k=25)
        response = query_engine.query(question)
        
        return jsonify({'response': str(response)}) 
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)









