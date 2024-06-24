for i in range(1,256):
    if i < 128:
        filename = 'bin' + str(bin(i)) + '.html'
        file1 = open(filename, 'w')
        L=["<!DOCTYPE html>\n",
           "<html>\n",
           "<title>binary</title>\n",
           "<img src='file:///C:/Users/s945853/Downloads/best%20of%202021/images/bruhmomento.png' width=50px; length=100px;> choose a path: <img src='file:///C:/Users/s945853/Downloads/best%20of%202021/images/bruhmomento.png' width=50px; length=100px;><br/>\n",
           '<form action="./bin'+str(bin(i))+'0'+'.html">\n',
           '<button type="submit" class="button1">\n',
           'zero\n',
           '</button>\n','</form>\n',
           '<form action="./bin'+str(bin(i))+'1'+'.html">\n',
           '<button type="submit" class="button1">\n',
           'one\n','</button>\n',
           '</form>\n',"</html>\n"]
        file1.writelines(L)
        file1.close()
    if i > 127:
        filename = 'bin' + str(bin(i)) + '.html'
        file1= open(filename, 'w')
        L=["<!DOCTYPE html>\n", "<html>\n","Your number is " + str(int(i)) + "!<br/>\n","<a href='file:///C:/Users/s945853/Downloads/best%20of%202021/index.html'>homepage</a>\n","</html>"]
        file1.writelines(L)
        file1.close

print("done")
