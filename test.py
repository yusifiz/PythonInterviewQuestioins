from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def index():
    return f"""<form action="/news" method='POST'>
        <input type="text" placeholder="Insert log" name='title'>
        <input type="text" placeholder="Insert password" name='content'>
        <input type="submit">
    </form>
    """


@app.route('/news', methods=['GET','POST'])
def news():
    if request.method=="POST":
        title=request.form['title']
        content=request.form['content']
    
    return f"""
<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <div class="card m-5" style="width: 18rem;">
    <div class="card-body p-5">
    <h5 class="card-title">{title}</h5>
    <p class="card-text">{content}</p>
    </div>
    </div>
    """   




if __name__=='__main__':
    app.run(debug=True)