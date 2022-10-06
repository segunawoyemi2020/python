def find_grade(mark):
    if mark >= 75:
        return 'A1'
    elif mark >= 70 and mark <= 74:
        return 'B2'
    elif mark >= 65 and mark <= 69:
        return 'B3'
    elif mark >= 60 and mark <= 64:
        'C4'
    elif mark >= 55 and mark <= 59:
        return 'C5'
    elif mark >= 50 and mark <= 54:
        return 'C6'
    elif mark >= 45 and mark <= 49:
        return 'D7'
    elif mark >= 40 and mark <= 44:
        return 'E8'
    else:
        return 'F9'
