class Translator:
 
        def ___init__(self):
                pass
       
        def main(self):
                print("Welcome to Snayer's Text to Morse Code")
                self.translateText()
       
        def translateText(self):
				print "\n"
				text = raw_input(str("Enter Text to Translate: "))
				text = text.lower()
				dictionary = {
				'a': ' .- ','b':' -... ','c':' -.-. ',
				'd':' -.. ','e':' . ','f':' ..-. ',
				'g':' --. ','h':' .... ','i':' .. ',
				'j':' .--- ','k':' -.- ','l':' .-.. ',
				'm':' -- ','n':' -. ','o':' --- ',
				'p':' .--. ','q':' --.- ','r':' .-. ',
				's':' ... ','t':' - ','u':' ..- ',
				'v':' ...- ','w':' .-- ','x':' -..- ',
				'y':' -.. ','z':' --.. ',' ':'  /  ',  
				}
				for letter in text:
						print dictionary[letter],
				self.translateText()
               
if __name__ == "__main__":
        ObjT = Translator()
        ObjT.main()
