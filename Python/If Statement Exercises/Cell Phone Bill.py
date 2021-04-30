SUPPORT_911 = 0.44
ADDITIONAL_TM = 0.15
ADDITIONAL_PC = 0.25
SALES_TAX = 0.05

cell_phone = int(input("Enter the minutes you spent : "))
text_message = int(input("Enter the text message you used : "))
all_bill = 0
if cell_phone > 50 and text_message > 50:
    all_bill = ((cell_phone - 50) * ADDITIONAL_PC + (text_message - 50) * ADDITIONAL_TM + SUPPORT_911) * SALES_TAX
    print("All bill = {0:.2f}, additional minutes = {1}, additional text = {2}".format(all_bill, (cell_phone - 50), (text_message - 50)))
else:
    all_bill = SUPPORT_911 * SALES_TAX
    print("All bill = {0:.2f}. Congratulations! You spent a normal count of time and message".format(all_bill))