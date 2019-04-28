from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import Form
from wtforms import IntegerField, StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import Required
import pickle
from sklearn import datasets
import numpy as np

# Inicializacia Flask aplikacie
app = Flask(__name__)

# Nacitanie vytvoreneho modelu pomocou pickle
print("loading my model")
with open('../model.pkl', 'rb') as handle:
    machine_learning_model = pickle.load(handle)
print("model loaded")


# Inicializacia formularu pre vyplnenie hodnot atributov
class theForm(Form):
    param1 = DecimalField(label='Sepal Length (cm):', places=2, validators=[Required()])
    param2 = DecimalField(label='Sepal Width (cm):', places=2, validators=[Required()])
    param3 = DecimalField(label='Petal Length (cm):', places=2, validators=[Required()])
    param4 = DecimalField(label='Petal Width (cm):', places=2, validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    print(session)
    form = theForm(csrf_enabled=False)
    if form.validate_on_submit():  # ked klineme na submit:
        # zoberieme vyplneneh hodnoty z policok
        session['sepal_length'] = form.param1.data
        session['sepal_width'] = form.param2.data
        session['petal_length'] = form.param3.data
        session['petal_width'] = form.param4.data
        # transformujeme ich na numpy array, ktoremu rozumie vytvoreny model
        flower_instance = np.array([float(session['sepal_length']), float(session['sepal_width']), float(session['petal_length']),
                           float(session['petal_width'])]).reshape(1,-1)

        
        #flowers = ['setosa', 'versicolor', 'virginica']
        
        #session['prediction'] = flowers[machine_learning_model.predict(flower_instance)[0]]
        session['prediction'] = machine_learning_model.predict(flower_instance)[0]

        
        return redirect(url_for('home'))

    return render_template('home.html', form=form, **session)


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.secret_key = 'super_secret_key_shhhhhh'
if __name__ == '__main__':
    app.run(debug=True)
