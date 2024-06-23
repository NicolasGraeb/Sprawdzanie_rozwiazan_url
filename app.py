from flask import Flask, request, render_template
from forms import process_form_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        big_text = request.form['big-text-area']
        number = request.form['number-input']
        additional_fields = []
        for i in range(1, int(number) + 1):
            field_name = f'additional-field-{i}'
            additional_fields.append(request.form.get(field_name, ''))

        results = process_form_data(big_text, additional_fields)
        return render_template('result.html', results=results)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
