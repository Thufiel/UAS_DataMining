import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model_file = open('logisticmodel_BC.pkl', 'rb')
model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('index.html', output='belum diprediksi')


@app.route('/predict', methods=['POST'])
def predict():
    radius, texture, perimeter, area, smoothness, compactness, concavity, concave_points, symmetry, fractal_dimension = [
        x for x in request.form.values()]
    data = []

    #data.append(int(usia))
    #if jeniskelamin == 'Laki-Laki':
    #    data.extend([1])
    #else:
    #    data.extend([0])
    data.append(int(radius))
    data.append(int(texture))
    data.append(int(perimeter))
    data.append(int(area))
    data.append(int(smoothness))
    data.append(int(compactness))
    data.append(int(concavity))
    data.append(int(concave_points))
    data.append(int(symmetry))
    data.append(int(fractal_dimension))

    prediction = model.predict([data])
    output = (prediction[0])
    if output == 1.0:
        hasil = "Anda beresiko penyakit jantung"
    else:
        hasil = "Anda tidak beresiko penyakit jantung"

    return render_template('index.html', output=hasil, radius=radius, texture=texture, perimeter=perimeter, area=area, smoothness=smoothness, compactness=compactness, concavity=concavity, concave_points=concave_points, symmetry=symmetry, fractal_dimension=fractal_dimension)

    if __name__ == '__main__':
        app.run(debug=True)
