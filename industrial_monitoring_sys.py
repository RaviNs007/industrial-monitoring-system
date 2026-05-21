def main():
    choice = main_menu()
    
    high_alerts, low_alerts, data_list = process_data(choice)
    
    print_report(high_alerts, low_alerts, data_list, choice)

    
def main_menu():
    print(f"""
    ################################
    #        ---Main Menu---       #
    #------------------------------#
    #   1. Temperature             #
    #                              #
    #   2. Pressure                #
    #                              #
    #   3. Voltage                 #
    ################################
    """)
    
    while True:
        choice = input("Choose senser from menu (1-3): ").strip().lower()
    
        if choice == "1" or choice == 't':
            return "Temperature"
            break
        
        elif choice == '2' or choice == 'p':
            return "Pressure"
            break
            
        elif choice == '3' or choice == 'v':
            return "Voltage"
            break
        print('Invalid choice')
        continue

def process_data(choice):
    
# setting limits for each attribute
    limits = {
        "Temperature": (20, 80),
        "Pressure": (30, 100),
        "Voltage": (210, 240)
    }
    
#checking limits
    low_limit, high_limit  = limits[choice]
    
# initializing variables
    data_list = []
    high_alerts = 0
    low_alerts = 0
    
# taking input & validating
    while True:
            
        data = (input(f"Enter {choice}: ").strip().lower())
        
        if data == 'done':
            break
        try:
            data = float(data)

            data_list.append(data)
            
        except ValueError:
            
            print("Please enter a correct value")
            continue
        
# alert tracking
        if data > high_limit:
            print(f"High {choice}")
            
            high_alerts += 1
            
        elif data < low_limit:
            print(f"Low {choice}")
            
            low_alerts += 1
            
        else:
            print(f"Normal {choice}")
        
    return high_alerts, low_alerts, data_list

def print_report(high_alerts, low_alerts, data_list, choice):
    
    if not data_list:
        print('No data received')
        
    return
#calculating average and printing REPORT
    
    avg = round(sum(data_list)/len(data_list),2)
    highest_value = max(data_list)
    lowest_value = min(data_list)

    if choice  == "Temperature":
        unit = '°C'

    elif choice == "Pressure":
        unit = 'PSI'

    elif choice == "Voltage":
        unit = 'VOLTS'
    
    print(f"""
########################################################
#                        REPORT                        #
########################################################
## Highest Value:            {highest_value} {unit:<19}##
## Lowest Value:             {lowest_value} {unit:<21}##
## Average Value:            {avg} {unit:<18}##
## Total Alerts:             {high_alerts + low_alerts:<25}##
## Total High Alerts:        {high_alerts:<25}##
## Total Low Alerts:         {low_alerts:<25}##
## Total Number of Readings: {len(data_list):<25}##
########################################################
""")

main()