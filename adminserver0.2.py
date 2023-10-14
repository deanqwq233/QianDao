from flask import Flask, request, Response
import datetime
import os

app = Flask(__name__)

@app.route('/QDadmin/', methods=['POST'])
def get_file():
        param = request.args.to_dict()
        name = param['name']
        
        if "V0.2" in name:
            if "QDADMIN" in name:
                date = name.find("DATE: ") + 6
                filename = os.getcwd() + "\\QDFiles\\" + name[date:] + '.txt'
                with open(filename , 'r' ,encoding = 'utf-8') as f:
                    content = f.read()
                return Response(content, mimetype='text/plain')
            else:
                return Response("Failed")
         
        else:
            return Response("VerFailed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8182)
