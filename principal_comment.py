def result_comment(percentage):
    if (percentage >= 90):
        return "Outstanding performance"
    elif (percentage >= 80 and percentage <= 89):
        return "An excellent performance"
    elif (percentage >= 70 and percentage <= 79):
        return "A very good performance"
    elif (percentage >= 60 and percentage <= 69):
        return "A good performance"
    elif (percentage >= 50 and percentage <= 59):
        return "An average performance"
    elif (percentage >= 40 and percentage <= 49):
        return "A fair performance"
    else:
        return "Advice to withdraw"

