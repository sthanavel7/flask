from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        "id":1,"title":"buy groceries",'description':"buy cheese food","done":False
    },
    {
        "id":2,"title":"learn python",'description':"learn flask ","done":False
    }
]
@app.route("/")
def helloworld():
    return 'world'
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
        task={
            'id':tasks[-1]['id']+1,
            'title':request.json['title'],
            'description':request.json.get('description',''),
            'done':False
        }
        tasks.append(task)
        return jsonify({
            "status":"success",
            "message":"successful"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if __name__=="__main__":
    app.run()
 