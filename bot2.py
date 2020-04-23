from nltk.chat.util import Chat, reflections
import matplotlib


train = [

        ['(.*) name is (.*)',['Hi %2!!, How are you?']],
        ['(hi|hey|heyy|hola|Hi|Hey|Hola)',['Hi there, can I know your name?']],
        ['(fine|good|going well|majama|all good )',['do u want any help']],
        ['(.*) help (.*)',['I can Help you...with your mood type any thing I will predict and recomend something']],
        ['(.*)',x] ,   
    ]

print(x)

chat=Chat(train , reflections)
chat.converse()
