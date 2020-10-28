from yahooquery import Ticker
from termcolor import colored
import pandas as pd



resultadoFinal=[]
totalLote=[]   
TotalCarteira=[]
TotalCarteiraCompra=[]




def carteira_fiis():
    Ativos = {'BTLG11.SA':105,'HCTR11.SA':131.69}
    QTD ={ 'HCTR11.SA':5,'BTLG11.SA':1}
    
    return Ativos,QTD

def carteira_acoes():
    ativos = {'OIBR3.SA': 1.70,
                'VALE3.SA': 61.85,
                'BBDC4.SA':19.50,
                'CCRO3.SA':12.77,
                'IRBR3.SA':8.22,
                'ITSA4.SA':8.82,
                'VVAR3.SA':17.84,
                'MGLU3.SA':25.99,
                'FRAS3.SA':6.20,
                'MMXM3.SA':11.75,
                'DMMO3.SA':1.35}


    qtd = {     'OIBR3.SA': 234,
                'VALE3.SA': 3,
                'BBDC4.SA':10,
                'CCRO3.SA':10,
                'IRBR3.SA':110,
                'ITSA4.SA':10,
                'VVAR3.SA':10,
                'MGLU3.SA':10,
                'FRAS3.SA':10,
                'MMXM3.SA':1,
                'DMMO3.SA':200}
    
    return ativos,qtd

def formatar(valor):
    valor = ('{:.2f}'.format(valor))
    return str(valor)

def cor (a):
    if float(a) < 0:
        vlr=(colored(str("R$"+a),'red'))
    
    elif float(a) == 0:
        vlr=(colored(str("R$"+a),'yellow'))

    
    else: 
        vlr=(colored(str("R$"+a),'green'))
    return vlr


def taxa (vlr):
    if float(vlr) < 20:
        vlr=(colored(str("<--"),'red'))
    
    elif float(vlr) == 0:
        vlr=(colored(str("--"),'yellow'))

    
    else: 
        vlr=(colored(str("-->"),'green'))
    return vlr


def cotacao(a):
    # 1d, 5d, 7d, 60d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    ativo = Ticker(a)
    
    t1 = ativo.history(period='1d')
    vlrFechamento = (t1["close"].values[0])
    return (vlrFechamento)


def dados (carteira):
   
    Ativos,QTD = carteira()
  
  
    


    for ativo,vlr in Ativos.items():
        vlrAtual = (cotacao(ativo))
        vlrAtual1 = (cotacao(ativo))
        
        QtdA=QTD.get(ativo)
        

        pc = vlr * QtdA
        pc = formatar(pc)
        vlrAtual = vlrAtual  * QtdA
        vlrAtual = formatar(vlrAtual) 
        resultado = float(vlrAtual) - float(pc) 
        resultado = formatar(resultado)
        resultadoFinal.append(float(resultado))
        totalLote.append(QtdA)
        
        TotalCarteiraCompra.append(float(pc))
        TotalCarteira.append(float(vlrAtual))
        
        
        TC = sum(TotalCarteira)
        TCC =sum(TotalCarteiraCompra)
   
   

        print(ativo +"  -  " +"Lote:"+str(QtdA) + "  -  "  + "Preço Nominal:"+str(cor(formatar(vlr)))+  "  -   "  +"Total Compra:R$"+str(pc) +"  -  " +"Atual:R$" +str(vlrAtual)  +"  -  " +"Resultado:"+ str(cor(resultado)) +"  -  "+"Atual:R$" +str(formatar(vlrAtual1)  )) 
        taxas = ((float(pc)*(0.30)/100)+10)
        
        #print(ativo +"  -  " +"Total Compra:R$"+str(pc)  +" - "+ "Taxas R$:" + str(formatar(taxas)))
    print("")
    print("Total de Lote:"+str(sum(totalLote)))
    print("Total da Carteira Compra:"+str(cor(formatar(TCC))))
    print("Total da Carteira:"+str(cor(formatar(TC))))
    print("Resultado do dia:"+str(cor(formatar(sum(resultadoFinal)))))
    print("--------------------------------------------------------------------------------------")
    resultadoFinal.clear()
    TotalCarteira.clear()
    TotalCarteiraCompra.clear()
    totalLote.clear()
   
dados(carteira_acoes)
dados(carteira_fiis)


