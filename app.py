from flask import Flask,render_template,request

from tensorflow import keras
import keras_cv
import matplotlib.pyplot as plt

app=Flask(__name__)

model=keras_cv.models.StableDiffusion(img_width=512,img_height=512)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/result',methods=['POST'])
def result():
    prompt=str(request.form['prompt'])
    image=model.text_to_image(prompt,batch_size=3)
    plt.imsave('result.jpg',image[0])
    # plt.savefig('result.jpg')
    return render_template('result.html',text=prompt)













if __name__=='__main__':
    app.run(debug=True)