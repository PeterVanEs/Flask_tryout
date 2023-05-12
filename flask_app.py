from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "<p><em><b>Les 11 vraag 4: Wij maken de hoofdtak 'main' aan en we schakelen daar naartoe over.</b></em></p>"

if __name__ == '__main__':
    app.run(port=5000,debug=True)