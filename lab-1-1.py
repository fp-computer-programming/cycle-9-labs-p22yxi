# Yongdong XI
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin" "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]


for x in rows:
    for name in x:
        if(name.endswith("s")):
            print("{0}\'".format(name))
        else:
            print("{0}\'s".format(name))

