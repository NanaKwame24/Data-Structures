#List of available cars and their prices
cars={"Shelby GT500CR":298000, "Bentley EXP100GT":400000, "Bugatti Chiron":3000000,\
      "Jaguar XJS":500000, "Chevrolet Camaro":550000, "Lotus Espirit":300000,\
      "Cadillac 1959":280000, "Dodge Viper":350000, "Ford Boss 302 Mustang":450000,\
      "Chevrolet Corvette":600000, "Bugatti Divo":5000000, "Pagani Huayra":1160000,\
       "McLaren Senna P15":900000, "Porsche 918 Spyder":822000, "RUF CTR3 Clubsport":652000,\
      "Brabus Maybach SV12":622000, "Brabus EV12":590000, "Koenigsegg CCX":545000,\
      "9ff GT9":490000, "Porsche Carrera GT":450000, "Saleen S7 Twin Turbo":465000,\
      "Ferrari SF90 Stradale":448000, "Lamborghini Aventador SVJ":400000, "Brabus Rocket":430000,\
      "McLaren 765LT Spider":375000, "Lexus LFA":375000, "Mercedes-Benz AMG GT Black Series":350000,\
      	"RUF RT12":300000, "Wiesmann Thunderball":290000, "Aston Martin Vanquish S":250000}
#Get user input for car name
carName= input('Enter car name:')
#Check if car name is in the list of available cars
if carName  in cars:
    print("Yes")
    #if car name is present, get its price
    carPrice = cars[carName]
    print(f"Price of {carName} is ${carPrice}.".format( carName, carPrice))
else:
    #If car name is not available, inform the user
    print(f"{carName} is not available.")
#https://github.com/NanaKwame24