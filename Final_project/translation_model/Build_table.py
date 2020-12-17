from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Languege", "Precision", "Recall", "F1-Score"]


table.add_row(["Fra-Eng",'0.797','0.882','0.837'])
table.add_row(["Spa-Eng","0.889","0.904","0.896"])
table.add_row(['Deu-Eng','0.803','0.987','0.886'])

print(table)
