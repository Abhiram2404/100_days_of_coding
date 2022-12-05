myBill = float(input("What was the bill?: "))
Tip_Percentage = int(input("% of tip to be added to the bill total: "))
numberOfPeople = int(input("How many people?: "))
#logic 1
tip_amount = Tip_Percentage / 100 * myBill
print("tip_amount = ",tip_amount)
#logic 2
answer = (myBill+tip_amount) / numberOfPeople
answer = round(answer,2)
print("You all owe", answer)
