from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def index():
    return f"""<form action="/about" method='POST'>
        <input type="text" placeholder="Insert log" name='name'>
        <input type="text" placeholder="Insert password" name='pass'>
        <input type="submit">
    </form>
    """


@app.route('/about', methods=['GET','POST'])
def about ():
    if request.method=="POST":
        ad=request.form['name']
        parol=request.form['pass']
    
    return f"""
<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <div class="card m-5" style="width: 18rem;">
    <div class="card-body p-5">
    <h5 class="card-title">{ad}</h5>
    <p class="card-text">{parol}</p>
    </div>
    </div>
    """   




if __name__=='__main__':
    app.run(debug=True)