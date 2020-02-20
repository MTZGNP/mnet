from flask import Flask, request #import main Flask class and request object
import json
app = Flask("app") #create the Flask app
@app.route('/post')
def query_example():
    room = request.args.get('room')
    message = request.args.get('message') #if key doesn't exist, returns None
    name = request.args.get("user")
    with open("%s.txt" % room,"r+") as roomf:
        data = json.loads(roomf.read())
        data.append({"user":name,"message":message})
        roomf.truncate(0)
        print(json.dumps(data))
        roomf.seek(0)
        roomf.write(json.dumps(data))
        print("done")
    return '''<h1>%s says %s</h1>''' %(name , message)  
@app.route('/get')
def show():
    room = request.args.get('room')
    with open("%s.txt" % room,"r+") as roomf:
        html = """"""
        for message in json.loads(roomf.read()):
            html = html+"<h1>%s says %s<h1>" %(message["user"],message["message"])
        return html
app.run(debug=True, port=5000) #run app in debug mode on port 5000
