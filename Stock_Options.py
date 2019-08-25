##Asks user to enter values for a stock and then returns a share valuation and European option info
import fin2
stk_dict = {}

def stk_code ():
    stk_dict['code'] = raw_input("\tEnter the stock code: ")  

def stk_S ():
    stk_dict['S'] = raw_input ("\tEnter current stock price ($): ")
    stk_dict['S'] = float(stk_dict['S'])
    sub_menu()
    sub_menu()

def stk_e ():
    stk_dict['e'] = raw_input ("\tEnter equity per share ($): ")
    stk_dict['e'] = float(stk_dict['e'])
    sub_menu()

def stk_R ():
    stk_dict['R'] = raw_input ("\tEnter return on equity (%): ")
    stk_dict['R'] = float(stk_dict['R'])/100.0
    sub_menu()

def stk_p ():
    stk_dict['p'] = raw_input ("\tEnter P/E ratio: ")
    stk_dict['p'] = float(stk_dict['p'])
    sub_menu()

def stk_d ():
    stk_dict['d'] = raw_input ("\tEnter dividend payout ratio (%): ")
    stk_dict['d'] = float(stk_dict['d'])/100.0
    sub_menu()

def stk_K ():
    stk_dict['K'] = raw_input ("\tEnter strike price ($): ")
    stk_dict['K'] = float(stk_dict['K'])
    sub_menu()

def stk_v ():
    stk_dict['v'] = raw_input ("\tEnter stock volatility (%): ")
    stk_dict['v'] = float(stk_dict['v'])/100.0
    sub_menu()

def stk_rm ():
    stk_dict['rm'] = raw_input ("\tEnter the expected return of the market (%): ")
    stk_dict['rm'] = float(stk_dict['rm'])/100.0
    sub_menu()

def stk_b ():
    stk_dict['b'] = raw_input ("\tEnter beta of the asset relative to the market (ratio): ")
    stk_dict['b'] = float(stk_dict['b'])
    sub_menu()

def stk_T ():
    stk_dict['T'] = raw_input ("\tEnter time stock/option wil be held (years): ")
    stk_dict['T'] = float(stk_dict['T'])
    sub_menu()

def stk_rf ():
    stk_dict['rf'] = raw_input ("\tEnter the risk free rate of return (%): ")
    stk_dict['rf'] = float(stk_dict['rf'])/100.0
    sub_menu()

def stk_tx ():
    stk_dict['tx'] = raw_input ("\tEnter personal tax rate (%): ")
    stk_dict['tx'] = float(stk_dict['tx'])/100.0
    sub_menu()

def stk_cgt ():
    stk_dict['cgt'] = raw_input ("\tEnter capital gain that is subject to tax (%): ")
    stk_dict['cgt'] = float(stk_dict['cgt'])/100.0
    sub_menu()

def stk_all ():
    stk_dict['code'] = raw_input("\tEnter the stock code: ")
    stk_dict['S'] = raw_input ("\tEnter Current Share Price ($): ")/1.0
    stk_dict['e'] = raw_input ("\tEnter Equity per Share ($): ")/1.0
    stk_dict['R'] = raw_input ("\tEnter Return on Equity (%): ")/100.0
    stk_dict['p'] = raw_input ("\tEnter P/E Ratio: ")/1.0
    stk_dict['d'] = raw_input ("\tEnter Dividend Payout Ratio (%): ")/100.0
    stk_dict['K'] = raw_input ("\tEnter strike price ($): ")/1.0
    stk_dict['v'] = raw_input ("\tEnter stock volatility (%): ")/100.0
    stk_dict['rm'] = raw_input ("\tEnter the expected return of the market (%): ")/100.0
    stk_dict['b'] = raw_input ("\tEnter beta of the asset relative to the market (ratio): ")/1.0
    stk_dict['T'] = raw_input ("\tEnter Time Stock/Option wil be held (years): ")/1.0
    stk_dict['rf'] = raw_input ("\tEnter the risk free rate of return (%): ")/100.0
    stk_dict['tx'] = raw_input ("\tEnter Personal Tax Rate (%): ")/100.0
    stk_dict['cgt'] = raw_input ("\tEnter Capital Gain Subject to CGT (%): ")/100.0
    sub_menu()

def stk_vals ():

    company_stk = fin2.Stock()
    company_call = fin2.Call()
    company_put = fin2.Put()

    Gain = company_stk.Val(stk_dict['R'], stk_dict['e'], stk_dict['d'],stk_dict['p'], stk_dict['S'], stk_dict['T'],stk_dict['rf'], stk_dict['tx'], stk_dict['cgt']) - stk_dict.get('S')
    Return = Gain/stk_dict.get('S')

    print "\n\tBased on the current parameters for",stk_dict.get('code'),"stock held over",stk_dict.get('T'),"years, the results are:"
    print "\n\tStock values (after tax)"
    print "\n\t\tCurrent stock price","\t$",stk_dict.get('S')
    print
    print "\t\tSale Proceeds (NPV)","\t$",company_stk.Sale(stk_dict['R'], stk_dict['e'], stk_dict['d'],stk_dict['p'], stk_dict['S'], stk_dict['T'],stk_dict['rf'], stk_dict['tx'], stk_dict['cgt'])
    print "\t\tDividend stream (NPV)","\t$",company_stk.Div(stk_dict['R'], stk_dict['e'], stk_dict['d'],stk_dict['T'],stk_dict['rf'], stk_dict['tx'])
    print "\t\tValuation (NPV)","\t$",company_stk.Val(stk_dict['R'], stk_dict['e'], stk_dict['d'],stk_dict['p'], stk_dict['S'], stk_dict['T'],stk_dict['rf'], stk_dict['tx'], stk_dict['cgt'])
    print "\n\t\tUndervalued by","\t\t$",Gain
    print "\t\tCalculated return","\t",Return*100,"%"
    print
    print "\t\tExpected CAPM return\t",company_stk.Capm(stk_dict['b'], stk_dict['rm'], stk_dict['rf'])*100,"%"
    print
    print "\tCall options with strike price of $",stk_dict.get('K')
    print
    print "\t\tPrice ","\t\t\t$",company_call.Price(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tDelta ","\t\t\t$",company_call.Delta(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tGamma ","\t\t\t$",company_call.Gamma(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tTheta ","\t\t\t$",company_call.Theta(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tVega ","\t\t\t$",company_call.Vega(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tRho ","\t\t\t$",company_call.Rho(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print
    print "\tPut options with strike price of $",stk_dict.get('K')
    print
    print "\t\tPrice ","\t\t\t$",company_put.Price(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tDelta ","\t\t\t$",company_put.Delta(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tGamma ","\t\t\t$",company_put.Gamma(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tTheta ","\t\t\t$",company_put.Theta(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tVega ","\t\t\t$",company_put.Vega(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    print "\t\tRho ","\t\t\t$",company_put.Rho(stk_dict['S'],stk_dict['K'],stk_dict['rf'],stk_dict['v'],stk_dict['T'])
    main_menu()

##Defaulted parameters
stk_dict['code'] = "BHP"
stk_dict['S']=25.00
stk_dict['e'] = 10.29
stk_dict['R'] = .3832
stk_dict['p'] = 8.34
stk_dict['d'] = 0.256
stk_dict['K'] = 40.00
stk_dict['v'] = 0.25
stk_dict['rm'] = 0.12
stk_dict['b'] = 1.11
stk_dict['T'] = 0.25
stk_dict['rf'] = 0.0425
stk_dict['tx'] = .35
stk_dict['cgt'] = .50

def main_menu():
    print "\n\t\t---- MAIN MENU ----\n"

    print "\t1. Display current parameters or enter new values"
    print"\t2. Display stock valuation with option prices & greeks\n"
    print"\t99. To Quit Program\n"

    select = raw_input("\tPlease make a selection: ")

    if select == '1': sub_menu()
    elif select == '2': stk_vals()
    elif select == '99': quit()
    else: print '\n\tThat choice is invalid!\n'
    main_menu()

def sub_menu():
    print "\n\t\t--- CURRENT PARAMETERS ---\n"
    print "\t  1. Stock code\t\t\t\t",stk_dict.get('code')
    print "\t  2. Current stock price\t\t","$",stk_dict.get('S')
    print "\t  3. Equity per share\t\t\t","$",stk_dict.get('e')
    print "\t  4. Return on equity\t\t\t",stk_dict.get('R')*100,"%"
    print "\t  5. P/E ratio\t\t\t\t","x",stk_dict.get('p')
    print "\t  6. Dividend payout rate\t\t",stk_dict.get('d')*100,"%"
    print "\t  7. Option strike price\t\t","$",stk_dict.get('K')
    print "\t  8. Stock volatility\t\t\t",stk_dict.get('v')*100,"%"
    print "\t  9. Expected market return\t\t",stk_dict.get('rm')*100,"%"
    print "\t10. Beta of stock\t\t\t","x",stk_dict.get('b')
    print "\t11. Time stock/option wil be held\t",stk_dict.get('T'),"years"
    print "\t12. Risk free/discount rate\t\t",stk_dict.get('rf')*100,"%"
    print "\t13. Personal tax rate\t\t\t",stk_dict.get('tx')*100,"%"
    print "\t14. Capital gain subject to CGT\t\t",stk_dict.get('cgt')*100,"%"
    print "\n\t15. To change all parameters"
    print "\n\t0. Return to main menu"
    print "\t99. To Quit Program\n"

    select2 = raw_input("\tEnter item number to change: ")

    print "\n"
    if select2 == '1': stk_code()
    elif select2 == '2': stk_S()
    elif select2 == '3': stk_e()
    elif select2 == '4': stk_R()
    elif select2 == '5': stk_p()
    elif select2 == '6': stk_d()
    elif select2 == '7': stk_K()
    elif select2 == '8': stk_v()
    elif select2 == '9': stk_rm()
    elif select2 == '10': stk_b()
    elif select2 == '11': stk_T()
    elif select2 == '12': stk_rf()
    elif select2 == '13': stk_tx()
    elif select2 == '14': stk_cgt()
    elif select2 == '15': stk_all()
    elif select2 == '0': main_menu()
    elif select2 == '99': quit()
    else: print '\n\tThat choice is invalid!'
    sub_menu()

main_menu()

#LEARN WHAT THE STANDARD END STUFF IS IN PYTHON FILES!! ALL THIS: ___MAIN___ STUFF.
