print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")
win=False
'''w1=""
w2=""
w3=""
w4=""
w5=""
w6=""
w7=""
w8=""
w9=""
'''
while win==False:
    chance=input("Enter where you want to make a move: ")
    if chance=='1':
        w1+=input("Enter your move: ")
    elif chance=='2':
        w2+=input("Enter your move: ")
    elif chance=='3':
        w3+=input("Enter your move: ")
    elif chance=='4':
        w4+=input("Enter your move: ")
    elif chance=='5':
        w5+=input("Enter your move: ")
    elif chance=='6':
        w6+=input("Enter your move: ")
    elif chance=='7':
        w7+=input("Enter your move: ")
    elif chance=='8':
        w8+=input("Enter your move: ")
    elif chance=='9':
        w9+=input("Enter your move: ")
    else:
        print("Please enter a valid number displayed above")
    if  (w1=='o' and w5=='o' and w9=='o') or (w1=='x' and w5=='x' and w9=='x') or (w3=='o' and w5=='o' and w7=='o') or (w3=='x' and w5=='x' and w7=='x') or (w1=='o' and w4=='o' and w7=='o') or (w1=='x' and w4=='x' and w7=='x') or (w2=='o' and w5=='o' and w8=='o') or (w2=='x' and w5=='x' and w8=='x') or (w3=='o' and w6=='o' and w9=='o') or (w3=='x' and w6=='x' and w9=='x') or (w1=='o' and w2=='o' and w3=='o') or (w1=='x' and w2=='x' and w3=='x') or (w4=='o' and w5=='o' and w6=='o') or (w4=='x' and w5=='x' and w6=='x') or (w7=='o' and w8=='o' and w9=='o') or (w7=='x' and w8=='x' and w9=='x'):
        win=True
        break
    else:
        win=False
print(win)    
print(w1,'|',w2,'|',w3)
print("-------")
print(w4,'|',w5,'|',w6)
print("-------")
print(w7,'|',w8,'|',w9)









