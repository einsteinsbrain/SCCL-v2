import random as rand                                                                                                                                                                                                                                                                                                                                                                                                                                   
l0 = "                              \n"
l1 = "                              \n"
l2 = "                              \n"
l3 = "                              \n"
l4 = "                              \n"
l5 = "                              \n"
l6 = "                              \n"
l7 = "                              \n"
l8 = "                              \n"
l9 = "                              \n"
l10 = "                              \n"
l11 = "                              \n"
l12 = "                              \n"
l13 = "                              \n"
l14 = "                              \n"
l15 = "                              \n"
l16 = "                              \n"
l17 = "                              \n"
l18 = "                              \n"
l19 = "                              \n"
l20 = "                              \n"
l21 = "                              \n"
l22 = "                              \n"
l23 = "                              \n"
l24 = "                              \n"
l25 = "                              \n"
l26 = "                              \n"
l27 = "                              \n"
l28 = "                              \n"
l29 = "                              \n"


lm1 = []
lm2 = []
lm3 = []
lm4 = []
lm5 = []
lm = [lm1, lm2, lm3, lm4, lm5]

LandmarkList = []
def landmarker(q):
    X =rand.randint(1, 29)
    Y =rand.randint(1, 29)
    return lm[q].append((X-1, Y-1))

landmarker(0)
landmarker(1)
landmarker(2)
landmarker(3)
landmarker(4)

#print(line9)
#print(len(line9))
x = -1 #starts at -1
y = 0 #starts at 0
Run  = True

    
    
    
while Run == True:

    screen = [l0,l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29]
    screen[y] = screen[y][:x+1:] + "X" + screen[y][x+2::]

                                        

    landmark0 = str(lm[0][0]).replace(")", "")
    landmark0 = landmark0.replace("(", "")
    lm0split = landmark0.find(",")
    landmark0 = landmark0.replace(",","")
    lm0X =landmark0[:lm0split:]
    lm0Y =landmark0[lm0split+1::]
###########################################################
    landmark1 = str(lm[1][0]).replace(")", "")
    landmark1 = landmark1.replace("(", "")
    lm1split = landmark1.find(",")
    landmark1 = landmark1.replace(",","")
    lm1X =landmark1[:lm1split:]
    lm1Y =landmark1[lm1split+1::]
###########################################################
    landmark2 = str(lm[2][0]).replace(")", "")
    landmark2 = landmark2.replace("(", "")
    lm2split = landmark2.find(",")
    landmark2 = landmark2.replace(",","")
    lm2X =landmark2[:lm2split:]
    lm2Y =landmark2[lm2split+1::]
###########################################################
    landmark3 = str(lm[3][0]).replace(")", "")
    landmark3 = landmark3.replace("(", "")
    lm3split = landmark3.find(",")
    landmark3 = landmark3.replace(",","")
    lm3X =landmark3[:lm3split:]
    lm3Y =landmark3[lm3split+1::]
###########################################################
    landmark4 = str(lm[4][0]).replace(")", "")
    landmark4 = landmark4.replace("(", "")
    lm4split = landmark4.find(",")
    landmark4 = landmark4.replace(",","")
    lm4X =landmark4[:lm4split:]
    lm4Y =landmark4[lm4split+1::]



    dictLm = {}
    
    screen[int(lm0Y)] = screen[int(lm0Y)][:int(lm0X)+1:] + "O" + screen[int(lm0Y)][int(lm0X)+2::]
    screen[int(lm1Y)] = screen[int(lm1Y)][:int(lm1X)+1:] + "O" + screen[int(lm1Y)][int(lm1X)+2::]
    screen[int(lm2Y)] = screen[int(lm2Y)][:int(lm2X)+1:] + "O" + screen[int(lm2Y)][int(lm2X)+2::] 
    screen[int(lm3Y)] = screen[int(lm3Y)][:int(lm3X)+1:] + "O" + screen[int(lm3Y)][int(lm3X)+2::]  
    screen[int(lm4Y)] = screen[int(lm4Y)][:int(lm4X)+1:] + "O" + screen[int(lm4Y)][int(lm4X)+2::]


    screen[y] = screen[y][:x+1:] + "X" + screen[y][x+2::]



    screenOutput = str(screen).replace(",", "")
    screenOutput = screenOutput.replace("[", "")
    screenOutput = screenOutput.replace("]", "")
    screenOutput = screenOutput.replace("\'", "")
    screenOutput = "('" + screenOutput + "')"
    screenOutput = 'print' + screenOutput 
    exec(screenOutput)

    
    #print(line9[::])
    #print(len(line9[::]))
    move = input("please move \"X\":")

    if move[:1:] == "N":
        
        
        if move[1:2:] == "1":
            if y-1 < 0:
                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
            else:
                y-=1
        elif move[1:2:] == "2":
            if y-2 < 0:
                print("Out of Bounds!")
                
            else: y-=2
    elif move[:1:] == "S":
        
    
        if move[1:2:] == "1":
            if y+1 > 29:
                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
            else:
                y+=1
        elif move[1:2:] == "2":
            if y+2 > 29:
                print("Out of Bounds!")
                
            else: y+=2
    elif move[:1:] == "W":
        
        if move[1:2:] == "1":
#            if x-1 < 0:
#                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
                    
#            else:
                    x-=1
        elif move[1:2:] == "2":
#            if x-2 > -1:
#                print("Out of Bounds!")
                    
#            else:
                 x-=2
    elif move[:1:] == "E":
        print(lm0X+"\n"+lm0Y)
        
        if move[1:2:] == "1":
            if x+1 > 29:
                print("STOP TRYING TO EXCAPE THE 30X30 ZONE")
                    
            else:
                x+=1
        elif move[1:2:] == "2":
            if x+2 > 29:
                print("Out of Bounds!")
                    
            else: x+=2
    
    

    
    else:
        print("You seem to have entered an Invalid Move!")
        Run = 1
