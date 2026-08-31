```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/")
def inicio():
    return "JARVIS está online!"

@app.route("/chat", methods=["POST"])
def chat():

    dados = request.get_json()

    mensagem = dados.get("mensagem", "")

    if not mensagem:
        return jsonify({
            "resposta": "Você não enviou nenhuma mensagem."
        })

    try:

        resposta = client.responses.create(
            model="gpt-5",
            instructions="""
            Você é JARVIS, um assistente virtual.
            Responda em português do Brasil.
            Seja educado, inteligente e direto.
            """,
            input=mensagem
        )

        return jsonify({
            "resposta": resposta.output_text
        })

    except Exception as erro:

        print(erro)

        return jsonify({
            "resposta": "Desculpe, ocorreu um erro ao falar com a inteligência artificial."
        }), 500


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta)
```
