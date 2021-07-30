def getType(value):
    type = {
        b'\x00': "Debit",
        b'\x01': "Credit",
        b'\x02': "StartAutopay",
        b'\x03': "EndAutopay"
    }
    return type.get(value, "Invalid State")

def hasField(value):
    type = {
        b'\x00': True,
        b'\x01': True,
        b'\x02': False,
        b'\x03': False
    }
    return type.get(value, "Invalid State")
