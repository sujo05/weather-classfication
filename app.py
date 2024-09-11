from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('model (6).pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST']) 
def submit():
    # Get input values from the form
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Wind_Speed = float(request.form['Wind_Speed'])
    Precipitation = float(request.form['Precipitation'])
    Cloud_Cover = int(request.form['Cloud_Cover'])
    Atmospheric_Pressure = float(request.form['Atmospheric_Pressure'])
    UV_Index = int(request.form['UV_Index'])
    Season = int(request.form['Season'])
    Visibility_KM = float(request.form['Visibility_KM']) 
    Location = int(request.form['Location'])
    Weather_Severity_Score = float(request.form['Weather_Severity_Score'])

    # # ... get other input values as needed ...

    # # Create a feature vector (include all the features your model expects)
    input_features = [[Temperature, Humidity, Wind_Speed, Precipitation, Cloud_Cover, 
                        Atmospheric_Pressure, UV_Index, Season, Visibility_KM, Location, 
                        Weather_Severity_Score]]
    # return input_features
  # Make a prediction
    prediction = model.predict(input_features)

        # Render the result template
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(port=8000)


