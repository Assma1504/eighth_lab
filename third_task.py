dictLanguages={
    "Alexander":["Russian", "English", "Chinese", "Hindi", "Spanish","Arabic"],
    "Dmitry":["Russian","Chinese","Arabic"],
    "Sergey":["Russian","English","Chinese"],
    "Ivan":["Russian","Chinese","Arabic"],
    "Nikolai":["Russian","English","Arabic"],
    "Mikhail": ["Russian","Chinese"],
    "Andrei": ["Russian","English","Chinese"],
    "Vladimir":["Russian","Arabic", "Hindi"],
    "Yuri":["Russian","Arabic", "Hindi"],
    "Pavel":["Russian","English", "Spanish"]
}

#Here I think we need to use SET, because the set's elements can't be repeated 
setLanguages = set()
listChineeseSpeakers=[]
for item in dictLanguages:
    print(dictLanguages[item])

    if "Chinese" in dictLanguages[item]:
        listChineeseSpeakers.append(item)

    for lang in dictLanguages[item]:
        setLanguages.add(lang)


print(f"Students speak the following languages: {setLanguages}")
listLanguages =sorted(list(setLanguages))
print(f"Here is the sorted languages list: {listLanguages}")
print(f"Students wich speak chineese language are: {listChineeseSpeakers}")
