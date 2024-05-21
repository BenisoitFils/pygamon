# class multiplication
class Operation:
    def __init__(ok,num1,num2):
        ok.num1 = num1
        ok.num2 = num2

    def resulta(no):
        return no.num1 * no.num2
# input # a multiplier
operation = Operation(num1=int(input('#')),num2=int(input('#')),)
print(operation.resulta())
