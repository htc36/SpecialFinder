def liquorCheck(name, typee, i):
    if typee == "liquor-beer-cider":
        amount = i['size']['packageType']
        amountInPack = i['size']['volumeSize']
        if amount == None:
            amount = i['variety']
        try:
            name += " " +  amountInPack
        except:
            pass
        return name, amount

