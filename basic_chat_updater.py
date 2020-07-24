while True:
    que = input("Enter your command \n")
    ans = input("answer of your question \n")
    file = open("basic_chat.aiml","a")
    file.write('\n\t<category>\n\t<pattern>' + que.upper()  +'</pattern>\n\t<template>\n\t\t'+ ans +"\n\t</template>\n\t</category>\n\n")
    file.close