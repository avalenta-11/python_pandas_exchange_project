
import csv
import pandas as pd

days_counter = -1
exchange_rate_e = 0
exchange_rate_a = 0
exchange_rate_g = 0


while True:
    try:

        print('ACME(tm) US DOLLAR EXCHANGE RATE APP')
        print('1) LOAD currency exchange rate data from a file \n2) USE AVERAGE exchange rate \n3) USE HIGHEST exchange rate \n4) USE LOWEST exchange rate \n5) CONVERT USD TO EUR \n6) CONVERT USD TO AUD \n7) CONVERT USD TO GBP \n0) QUIT program')


        function = int(input('Choose what to do: '))


        ###FUNCTION 0        
        if function == 0:
            break


        ###FUNCTION 1
        elif function == 1:
            filename = input('Give name of the data file: ')
            df = pd.read_csv(filename, delimiter = ";")

            with open (filename, 'r') as readfile:
                for row in readfile:
                    days_counter += 1
            
            from_date = df.iloc[0,0]
            to_date = df.iloc[-1,0]
            
            print('Data loaded successfully!')
            print('Currency exchange data is from', days_counter, 'days between', from_date, 'and', to_date, '\n')

#---------------------------------------------------------------------------

        ###FUNCTION 2
        elif function == 2:
            df = pd.read_csv(filename, delimiter = ";")

            exchange_rate_e = df['USD-EUR'].mean()
            exchange_rate_a = df['USD-AUD'].mean()
            exchange_rate_g = df['USD-GBP'].mean()
            
            print('Using the average currency exchange rate. \n')

#---------------------------------------------------------------------------

        ###FUNCTION 3
        elif function == 3:
            df = pd.read_csv(filename, delimiter = ";")

            exchange_rate_e = df['USD-EUR'].max()
            exchange_rate_a = df['USD-AUD'].max()
            exchange_rate_g = df['USD-GBP'].max()

            print('Using the highest currency exchange rate. \n')

#---------------------------------------------------------------------------

        ###FUNCTION 4
        elif function == 4:
            df = pd.read_csv(filename, delimiter = ";")

            exchange_rate_e = df['USD-EUR'].min()
            exchange_rate_a = df['USD-AUD'].min()
            exchange_rate_g = df['USD-GBP'].min()

            print('Using the lowest currency exchange rate. \n')

#---------------------------------------------------------------------------

        ###FUNCTION 5
        elif function == 5:
            convert_e = input('Give USD to convert: ')
            euro_converted = int(convert_e) * exchange_rate_e
            print(convert_e, 'USD in EUR is', euro_converted, '\n')

#---------------------------------------------------------------------------

        ###FUNCTION 6
        elif function == 6:
            convert_a = input('Give USD to convert: ')
            aud_converted = int(convert_a) * exchange_rate_a
            print(convert_a, 'USD in EUR is', aud_converted, '\n')

#---------------------------------------------------------------------------

        ###FUNCTION 7
        elif function == 7:
            convert_g = input('Give USD to convert: ')
            gbp_converted = int(convert_g) * exchange_rate_g
            print(convert_g, 'USD in EUR is', gbp_converted, '\n')
                    
    except:
        print("Bad input!")











