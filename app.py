from flask import Flask,render_template,request,redirect,url_for
import os
import openai
openai.api_key = os.getenv("OPENAI_KEY") 
openai.api_key = 'sk-' 
messages = []
system_msg = "You are a drepression assist chatbot only and answer in short keep it 1-2 lines."
messages.append({"role": "system", "content": system_msg})

app = Flask(__name__)



chats=[]
@app.route("/") #home
def hello():
	return render_template("chat_bot.html",type="start to type")

@app.route("/start",methods=['POST','GET'])
def start():
        inp = [str(x) for x in request.form.values()]
        print(inp[0])
        messages.append({"role": "user", "content": inp[0]})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
        result = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": result})
        print(result)
        chats.append("You: " + inp[0])
        chats.append(result)
        return render_template('chat_bot.html',chats=chats[::-1],type="")


			
# start() 
if __name__=="__main__":
	app.run(debug=False,host='0.0.0.0')

