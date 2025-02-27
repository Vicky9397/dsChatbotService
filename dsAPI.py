from flask import Flask, Response,request
import dsInterface as dsi

app = Flask(__name__)

@app.route('/chat', methods=['GET'])
def chat():
    prompt = request.args.get("prompt")
    return Response(dsi.generate_response(prompt), content_type="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, threaded=True)