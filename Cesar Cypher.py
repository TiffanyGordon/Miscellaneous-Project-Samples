def cesar(x): #defines function cesar
    infile=open(x) #opens file x
    newfile=open(y, 'w') #opens file y for writing
    content=infile.read() #reads file x
    mode=b #assigns variable 'mode' to input b
    if mode=='0':
        lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        shift=a #assigns variable 'shift' to input a
        if shift<0: 
            shift=shift+26 #makes shift a positive number
        outfile='' #creates new string called outfile
        for ch in content:
            if ch in lower: #loops through lowercase characters
                trans=content.maketrans(ch, lower[(lower.index(ch)+shift)%26]) #creates table to change character
                newch=ch.translate(trans) #transfers character according to table
                newfile.write(newch) #writes new character in newfile
            elif ch in upper: #loops through uppercase characters
                trans=content.maketrans(ch, upper[(upper.index(ch)+shift)%26]) #creates table to change character
                newch=ch.translate(trans) #transfers character according to table
                newfile.write(newch) #writes new character in newfile
            else:
                newfile.write(ch) #writes any character that is not in either list to newfile
    elif mode=='1':
        lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        shift=-a #assigns variable 'shift' to the negative of input a
        if shift<0:
            shift=shift+26
        outfile='' #creates new string called outfile
        for ch in content:
            if ch in lower: #loops through lowercase characters
                trans=content.maketrans(ch, lower[(lower.index(ch)+shift)%26]) #creates table to change character
                newch=ch.translate(trans) #transfers character according to table
                newfile.write(newch) #writes new character in newfile
            elif ch in upper: #loops through uppercase characters
                trans=content.maketrans(ch, upper[(upper.index(ch)+shift)%26]) #creates table to change character
                newch=ch.translate(trans) #transfers character according to table
                newfile.write(newch) #writes new character in newfile
            else:
                newfile.write(ch) #writes any character that is not in either list to newfile
    else:
        mode=input('Enter 0 if you would like to encrypt a file or 1 if you would like to decrypt a file: ')
    newfile.write(outfile) #writes string 'outfile' to newfile
    newfile.close() #closes newfile
    numChar=len(content) #counts number of characters in content
    numWord=len(content.split()) #counts number of words in content
    numlines=len(content.split('\n')) #counts number of lines in content
    infile.close() #closes file infile
    print('Your file contains ' + str(numlines) + ' lines,' + str(numWord) + ' words, and ' + str(numChar) + ' characters.') #prints out the number of lines, words, and characters in the input file for user to view


x=input('Enter the path for the input file: ') #Asks user for input file path
y=input('Enter the path for the output file: ') #Asks user for output file path
a=eval(input('Enter the cypher: ')) #Asks user for the cypher
b=input('Enter 0 if you would like to encrypt a file or 1 if you would like to decrypt a file: ') #Asks user if input file should be encrypted or decrypted
cesar(x) #runs function cesar
print('Your file is now available at '+ y) #prints the path of the output file for the user to view
