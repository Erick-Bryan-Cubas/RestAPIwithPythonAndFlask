from flask import Flask
app = Flask(__name__)

"""

- Atráves do parametro na função hello, é possível passar um valor para a URI
- Se no decorador não tiver o tipo do valor URI, por padrão é string 
"""

@app.route("/<int:numero>", methods=['GET','POST']) # Decorador que define a rota da URL
def hello(numero):
    return u'Olá mundo! {0}'.format(numero) # Retorna uma string


if __name__ == '__main__': # Acessar o módulo principal
    app.run(debug=True) # Dispobiliza a aplicação na web
    
""" 
- Sem o if __name__ == '__main__':, Qualquer módulo pode chamá-lo e executá-lo.
- O método debug = True, permite que a aplicação seja atualizada automaticamente, recomendado apenas para desenvolvimento.
"""