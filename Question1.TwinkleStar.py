#Base code to learn how to indent from: https://stackoverflow.com/questions/8234274/how-to-indent-the-contents-of-a-multi-line-string#:~:text=You%20can%20indent%20the%20lines,work%20in%20earlier%20Python%20versions.
#Question Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php#EDITOR 

#Purpose of this program was to practice how to indent each line of a text in a certain way for formatting purposes. 
        #This is useful when creating engaging text for company websites.

#question #1
try:
    #this wraps text into a single paragraph
    import textwrap
    textwrap.indent

#I made seperate indentation functions for each of the lines of the song "Twinkle Twinkle Little Star"
except AttributeError:  # leads to error because this function is not defined
    def indent(textTwinkle1, amount, ch=' '):
        padding = amount * ch
        return ''.join(padding+line for line in textTwinkle1.splitlines(True))
    def indent(textTwinkle2, amount, ch=' '):
        padding = amount * ch

        return ''.join(padding+line for line in textTwinkle2.splitlines(True))
    def indent(textTwinkle3, amount, ch=' '):
        padding = amount * ch
        return ''.join(padding+line for line in textTwinkle3.splitlines(True))
    
    def indent(textTwinkle5, amount, ch=' '):
        padding = amount * ch
        return ''.join(padding+line for line in textTwinkle5.splitlines(True))
else:
    #this defines the indentation of specific text
    def indent(textTwinkle1, amount, ch=' '):
        return textwrap.indent(textTwinkle1, amount * ch)
    def indent(textTwinkle2, amount, ch=' '):
        return textwrap.indent(textTwinkle2, amount * ch)
    def indent(textTwinkle3, amount, ch=' '):
        return textwrap.indent(textTwinkle3, amount * ch)
    def indent(textTwinkle5, amount, ch=' '):
        return textwrap.indent(textTwinkle5, amount * ch)
    #the "amount * ch defines number of spaces the text will be indented"

#Define each line so I can indent them seperately
textTwinkle = '''Twinkle twinkle little star.'''
textTwinkle1 = '''How I wonder what you are.'''
textTwinkle2 = '''Up above the world so high.'''
textTwinkle3 = '''Like a diamond in the sky.'''
textTwinkle4 = '''Twinkle twinkle little star.'''
textTwinkle5 = '''How I wonder what you are.'''

#output statements using defined functions above
print(textTwinkle)
print(indent(textTwinkle1,5))
print(indent(textTwinkle2,12))
print(indent(textTwinkle3,12))
print(textTwinkle4)
print(indent(textTwinkle5,5))
