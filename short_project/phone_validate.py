def phone_validate(p):
    try:
        if type(int(p)) == int:
            return "valid number"
    except Exception as e:
        return "It's Invalid phone number"
