from PyQt5 import  uic,QtWidgets


#FUNÇÃO PRINCIPAL DO SISTEMA
def funcao_principal():
    linha1 = cadastro.lineEdit.text()
    linha2 = cadastro.lineEdit_2.text()
    linha3 = cadastro.lineEdit_3.text()
    
    if cadastro.radioButton.isChecked() :
        print("\nCategoria selecionada: Desktop")
    elif cadastro.radioButton_2.isChecked() :
        print("\nCategoria selecionada: Notebooks")
    else :
        print("\nCategoria selecionada: Periféricos")

    print("\n-------------------------------")
    print("Código : ",linha1)
    print("Descricao : ",linha2)
    print("Preço : ",linha3)
    print("-------------------------------\n ")

    
#CARREGA A USER INTERFACE DENTRO DO CÓDIGO
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()