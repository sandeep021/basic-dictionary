<<<<<<< HEAD
while True:
    import json
    from difflib import get_close_matches
    data = json.load(open("data.json",))

    def translate(word):
        if word in data:
           return data[word]
        elif len(get_close_matches(word,data.keys()))>0:
           yn= input("Did you mean %s Enter y for Yes and n for No: " % get_close_matches(word,data.keys())[0])
           if yn=="y":
            return data[ get_close_matches(word,data.keys())[0]]
           else :
               return "Sorry word doesn't exist."
        else:
            return "Query Word doesn't exist"

    word = input("Hello! Enter your query word: ").lower()
    l=translate(word)
    if type(l)==list:
       for item in l:
         print(item)
    else:
        print(l)
=======
while True:
    import json
    from difflib import get_close_matches
    data = json.load(open("data.json",))

    def translate(word):
        if word in data:
           return data[word]
        elif len(get_close_matches(word,data.keys()))>0:
           yn= input("Did you mean %s Enter y for Yes and n for No: " % get_close_matches(word,data.keys())[0])
           if yn=="y":
            return data[ get_close_matches(word,data.keys())[0]]
           else :
               return "Sorry word doesn't exist."
        else:
            return "Query Word doesn't exist"

    word = input("Enter your query word: ").lower()
    l=translate(word)
    if type(l)==list:
       for item in l:
         print(item)
    else:
        print(l)
>>>>>>> 6aac301d66f261d1e199a68c7073f3742a17e57b


# testing pull request
