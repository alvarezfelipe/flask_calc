from flask import *

app = Flask(__name__)

class Calculadora():
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/', methods=['POST'])
    def operacoes():
        operacao = request.form['operacao']
        num_1 = int(request.form['var_1'])
        num_2 = int(request.form['var_2'])
        result = 0
        
        if operacao == 'adicao':
            result = num_1 + num_2
        elif operacao == 'subtracao':
            result = num_1 - num_2
        elif operacao == 'multiplicacao':
            result = num_1 * num_2
        elif operacao == 'divisao':
            result = num_1 / num_2
        elif operacao == 'raiz_quadrada':
            result = num_1 + num_2
        elif operacao == 'potencia':
            result = num_1 ^ num_2
        else:
            result =  'operação inválida'        
        
        return render_template('home.html', result=result)
        
    if __name__ == "__main__":
        app.run(debug=True)