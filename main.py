from flask import Flask,render_template
import requests as  re

app = Flask("__name__")

@app.route("/")
def home_page():
    return render_template("index.html",data="https://iso.500px.com/wp-content/uploads/2016/03/stock-photo-142984111.jpg",data2 = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg")


@app.route("/rand_image")
def home_page_image():
    image = re.get("https://picsum.photos/500/300")
    image2 = re.get("https://picsum.photos/500/300")
    return render_template("index.html",data = image.url,data2 = image2.url)


if(__name__ == "__main__"):
    app.run(debug=True)
