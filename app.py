from flask import Flask, redirect,request,render_template, url_for

movies =[
    {
        'id':1,
        'title':'A star was born',
        'desc': 'Singer',
        'year': '2010',
    },
    {
        'id':2,
        'title':'Beauty and beast',
        'desc': 'prince and princess',
        'year': '2021',
    }
]

app = Flask(__name__)


def get_next_id(list):
    return list[-1]['id']+1 if len(list) > 0 else 1

@app.route('/')
def index():
    return render_template('index.html', movies=movies)


@app.route('/movies', methods=['POST','GET'])
def create_movie():
    if request.method =='GET':
        return render_template('movie_form.html')
    #POST 
    movies.append({
        'id':get_next_id(movies),
        'title':request.form.get('title'),
        'desc':request.form.get('desc'),
        'year':request.form.get('year'),
    })
    return redirect (url_for('index'))


@app.route('/movies/<int:id>')
def get_movie(id):
    movie = list(filter(lambda movie:movie['id']==id, movies))
    if not len(movie):
        return "not found"
    movie = movie[0]
    return render_template ('moviedetails.html', movie=movie)


@app.route('/del-movie/<int:id>')
def del_movie(id):
    movie = list(filter(lambda movie:movie['id']==id, movies))
    if not len(movie):
        return "not found"
    for i in movies:
        if i['id'] == id:
            movies.remove(i)
            break
    return redirect('/')


@app.route('/edit-movie/<int:id>', methods=['POST','GET'])
def edit_movie(id):
    movie = list(filter(lambda movie:movie['id']==id, movies))
    if not len(movie):
        return "not found"
    movie = movie[0]
    if request.method =='GET':
        return render_template('update_movie.html', movie=movie)
    # POST 
    for i in movies:
        if i['id'] == id:
            i['id']= request.form.get('id')
            i['title']=request.form.get('title')
            i['desc']=request.form.get('desc')
            i['year']=request.form.get('year')
    return redirect (url_for('index'))




app.run('localhost', 8000 , debug=True)


