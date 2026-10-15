import pandas as pd
pd.DataFrame({"Customer Name":[" alice tan","BOB LEE","alice tan ","Chong Wei",None],
 "Email":["ALICE@MAIL.COM","bob@mail.com","alice@mail.com"," cw@mail.com ","x@mail.com"],
 "Amount":["RM 120.50","85","120.5","1,200","40"],"Date":["2026-09-01","01/09/2026","2026-09-01","Sep 3 2026","2026-09-04"]}).to_excel("input/branch_A.xlsx",index=False)
pd.DataFrame({"customer name":["Devi R","bob lee"],"EMAIL":["devi@mail.com","BOB@mail.com"],
 "amount":["RM300","85.00"],"date":["2026-09-05","2026-09-02"]}).to_excel("input/branch_B.xlsx",index=False)
