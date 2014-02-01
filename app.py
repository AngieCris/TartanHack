from flask import Flask, render_template, request
from pydub import *
from random import *

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', event="TartanHacks")

@app.route("/music",methods=["POST"])
def take_text():
	text = request.form['text_to_convert']
	if (len(text)==0):
		return render_template("warning.html")
	else:
		for i in xrange(0, len(text)):
			if (text[i].isdigit()):
				return render_template("warning2.html")
	playsound(text)
	return render_template('new-music.html', music_filename="static/Yo.wav")


def convert(letter):
    if (letter == "A" or letter == "a"):
        sound = AudioSegment.from_wav("A.wav")
    elif (letter == "B" or letter == "b"):
        sound = AudioSegment.from_wav("B.wav")
    elif (letter == "C" or letter == "c"):
        sound = AudioSegment.from_wav("C.wav")
    elif (letter == "D" or letter == "d"):
        sound = AudioSegment.from_wav("D.wav")
    elif (letter == "E" or letter == "e"):
        sound = AudioSegment.from_wav("E.wav")
    elif (letter == "F" or letter == "f"):
        sound = AudioSegment.from_wav("F.wav")
    elif (letter == "G" or letter == "g"):
        sound = AudioSegment.from_wav("G.wav")
    elif (letter == "H" or letter == "h"):
        sound = AudioSegment.from_wav("H.wav")
    elif (letter == "I" or letter =="i"):
        sound = AudioSegment.from_wav("I.wav")
    elif (letter == "J" or letter == "j"):
        sound = AudioSegment.from_wav("J.wav")
    elif (letter == "K" or letter == "k"):
        sound = AudioSegment.from_wav("K.wav")
    elif (letter == "L" or letter == "l"):
        sound = AudioSegment.from_wav("L.wav")
    elif (letter == "M" or letter == "m"):
        sound = AudioSegment.from_wav("M.wav")
    elif (letter == "N" or letter == "n"):
        sound = AudioSegment.from_wav("N.wav")
    elif (letter == "O" or letter == "o"):
        sound = AudioSegment.from_wav("O.wav")
    elif (letter == "P" or letter == "p"):
        sound = AudioSegment.from_wav("P.wav")
    elif (letter == "Q" or letter == "q"):
        sound = AudioSegment.from_wav("Q.wav")
    elif (letter == "R" or letter == "r"):
        sound = AudioSegment.from_wav("R.wav")
    elif (letter == "S" or letter == "s"):
        sound = AudioSegment.from_wav("S.wav")
    elif (letter == "T" or letter == "t"):
        sound = AudioSegment.from_wav("T.wav")
    elif (letter == "U" or letter == "u"):
        sound = AudioSegment.from_wav("U.wav")
    elif (letter == "V" or letter == "v"):
        sound = AudioSegment.from_wav("V.wav")
    elif (letter == "W" or letter == "w"):
        sound = AudioSegment.from_wav("W.wav")
    elif (letter == "X" or letter == "x"):
        sound = AudioSegment.from_wav("X.wav")
    elif (letter == "Y" or letter == "y"):
        sound = AudioSegment.from_wav("Y.wav")
    elif (letter == "Z" or letter == "z"):
        sound = AudioSegment.from_wav("Z.wav")
    elif (letter == " "):
        sound = AudioSegment.from_wav("Space.wav")
    elif (letter == "," or letter == ":" or letter == ";"):
        sound = AudioSegment.from_wav("Commas.wav")
    elif (letter == "."):
        sound = AudioSegment.from_wav("PERIOD.wav")
    elif (letter == "!"):
        sound = AudioSegment.from_wav("!!.wav")
    elif (letter == "("):
        sound = AudioSegment.from_wav("leftBracket.wav")
    elif (letter == ")"):
        sound = AudioSegment.from_wav("rightBracket.wav")
    elif (letter == "?"):
        sound = AudioSegment.from_wav("??.wav")
    elif (letter == "!"):
        sound = AudioSegment.from_wav("!!.wav")
    return sound
    
def playsound(text):
    sound = convert(text[0])
    for i in xrange(1, len(text)):
        sound += convert(text[i])
    return sound.export("static/Yo.wav", format = "wav")

	
if __name__ == "__main__":
	app.debug = True
	app.run()