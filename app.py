from flask import Flask, request, render_template
import cv2
import pytesseract

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        text = pytesseract.image_to_string(image)
        return render_template('result.html', text_detected=text)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=80)