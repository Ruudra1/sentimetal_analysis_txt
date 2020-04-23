from nltk.chat.util import Chat, reflections

train = [

        ['(.*) name is (.*)',['Hi %2!!, How are you?']],
        ['(hi|hey|heyy|hola|Hi|Hey|Hola)',['Hi there, can I know your name?']],
        ['(.*) help (.*)',['I can Help you...']],
        ['(.*) + (.*)',['The answer is %1 + %2']],
        ['(good|all set|fine|all good|)',['Good to hear that! \n Btw do you kn about the epidemic COVID 19 !!']],
       
    ]



chat=Chat(train , reflections)
chat.converse()
