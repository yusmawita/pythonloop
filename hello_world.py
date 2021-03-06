# Copyright (c) 2015 Pepijn Oomen <oomen@piprograms.com>
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.


from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/code1')
def code1():
    output = ""
    for i in range(0,100):
        for j in range(0,i):
            output+="*"
        output+="\n"
    return output, 200, { 'Content-Type': 'text/plain' }

@app.route('/code2')
def code2():
    output = ""
    for i in range(1,100):
        output +="Kelipatan angka "+str(i)+"\n"
        for j in range(1,100):
            output += str(i*j)+" "
        output += "\n\n"
    return output, 200, { 'Content-Type': 'text/plain' }

@app.route('/code3')
def code3():
    return render_template('hello.html')



if __name__ == '__main__':
    app.run(debug = True)

