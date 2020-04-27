from collections import Counter
import string
import matplotlib.pyplot as plt
from tkinter import*
import tkinter as tk


def check_text():
    sep = input_text.get()
    sep=str(sep)
    lower_case=sep.lower()
    clean_txt = lower_case.translate(str.maketrans('','',string.punctuation))
    sep=clean_txt.split()
    #print(sep)
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now",".........","."]
    
    final = []
    for i in sep:
        if i not in stop_words:
            final.append(i)
    #print(final)
    #now emotions
    emotion_list= []
    with open('emotions.txt','r') as file:
        for i in file:
            clear= i.replace('\n','').replace(',','').replace("'",'').strip()
            word , emotion = clear.split(':')
            
            if word in final:
                emotion_list.append(emotion)
    
    #print(emotion_list)
    if emotion_list == []:
        print("No Such Dominant Emotions found , Its Neutral\n")#.place(x=60,y=200)
    else:
        print("\nThe Dominant Emotions in the text are\n")
        w= Counter(emotion_list)
        print(w)
        #output.insert(END,w)
    plt.pie(w.values(),labels=w.keys(),autopct='%1.1f%%')
    plt.show()  

main=Tk()
main.title("Sentiment Analysis Of Text")
main.geometry("400x400")
Label(main,text="Welcome to sentiment analysis!",font =10).place(x=45,y=10)
Label(main,text="Enter Text to analyze:").place(x=60,y=80)
#Label(main,text="Output:").place(x=60,y=180)
input_text=StringVar()
Entry(main,text="",textvar=input_text,width=40).place(x=60,y=100)
Button(main,text = "Submit",width =6,command=check_text,height="1",font=8).place(x=160,y=150)

main.mainloop()