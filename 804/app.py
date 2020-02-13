class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        setMorse = set()
        for word in words:
        	morseCode = ''
          	for letter in word:
            	morseCode += morse[ord(letter.lower()) - 97]
          	setMorse.add(morseCode)
        return len(setMorse)