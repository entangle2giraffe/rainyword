
import json
import sender.word_list as wl

if __name__ == "__main__":
    #print("Hello")
    word_list_dict = {}
    words = wl.generate_random_words()
    print(words) # {"word": ["mh", "framed", "support", "transparent", "rep"]}
    #print (words)
    #print (words["word"][0])
    word_list_dict["1"] = []
    #word_list_dict["2"] = []
    #for i in words["word"]:
        #word_list_dict["1"].append(i)
    #for i in words["word"]:
        #word_list_dict["2"].append(i)    
    print(word_list_dict)
    word = {"scoreList":[{"id":0,"score":100},{"id":3,"score":99}]}
    message = {"playerTyped":'assault'}
    typed_word = message["playerTyped"][0]
    mes = '{"wordRemoved":' + str(typed_word) + '}'
    print(mes)    