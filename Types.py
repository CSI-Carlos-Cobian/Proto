def getType(value):
    types = {
        b'\x00': "Debit",
        b'\x01': "Credit",
        b'\x02': "StartAutopay",
        b'\x03': "EndAutopay"
    }
    return types.get(value, "Invalid State")