# clean txt


# lower case
from colections import Counter
import string
text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()

# removing punctuations

clean_txt = lower_case.translate(str.maketrans('','',string.punctuation))

#seperation

sep = clean_txt.split()

#removing meaningless words

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final = []

for i in sep:
    if i not in stop_words:
        final.append(i)

print(final)

#adding emotions

emotion_list= [ ]
with open('emotions.txt','r') as file:

    for i in file:
        clear= i.replace('\n','').replace(',','').replace("'",'').strip()
        word , emotion = clear.split(':')
        #print( "Word:" +word + " " + "Emotion:" +emotion)


        if word in final:
            emotion_list.append(emotion)

print(emotion_list)
c= Counter(emotion_list)
