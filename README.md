# SCCL-v2
The potentially more buggy sequel to Simple Command Command Line.

BTW:

    elif move [:1:] == "M":
        if x==lm0X and y==lm0Y:
            dictLm[lm1] = int(lm0X), int(lm0Y)
            dictLm.update()
            lm[0:1][::].clear()
        if x==lm1X and y==lm1Y:
            dictLm[lm2] = int(lm1X), int(lm1Y)
            dictLm.update()
            lm[0:2][::].clear()
        if x==lm2X and y==lm2Y:
            dictLm[lm3] = int(lm2X), int(lm2Y)
            dictLm.update()
            lm[0:3][::].clear()
        if x==lm3X and y==lm3Y:
            dictLm[lm4] = int(lm3X), int(lm3Y)
            dictLm.update()
            lm[0:4][::].clear()
        if x==lm4X and y==lm4Y:
            dictLm[lm5] = int(lm4X), int(lm4Y)
            dictLm.update()
            lm[0:5][::].clear()
    elif move[:1:] == "P":
        dictLm.update()
        print(dictLm)
I cut this out because I didn't get it to work someone please help!        
