from flask import Flask, render_template, request, redirect
import speech_recognition as sr
#creating a flask environment
#Setting Up the app in the following line 5
app = Flask(__name__)

#This will route to the home page
@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    #Debug will allow to command this file and the flask instance will automatically refresh after each save.
    #Threaded is true so that computer doesn't get overloaded and process multiple requests at the same time