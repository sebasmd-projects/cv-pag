from datetime import datetime

def custom_processors(request):
    today = datetime.today()
    birthdate = datetime(1999, 5, 16)

    ctx = {}
    ctx['age'] = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return ctx