""" 
    Program służy obliczania wyników takich
     działań jak tetracji oraz petracji wiekszych 
    niema sensu bez super komputera
    """
#funkcja pobiera 3 agumenty jakie można
# znaleść w notacji strzałkowej 
# zakładając że w działaniu mamy 1 strzałke
# to a jest podstawą potęgi
# a b jest jej stopniem
def wielpotengowanie(a,b,strzalki):
    #instrukcja if sprawdza czy zmienna strzałki
    # jest równa 1 jeżeli tak to można zastosować
    #zwykłe potęgowanie i wartość jest 
    #zwracana jeżeli nie funkcja jest
    # wykonywana z swojego wnętrza dopóki
    # zmienna strzałki nie będzie równa 1
    if(strzalki == 1):
        return a**b
    else:
      wynik = wielpotengowanie(a,b,strzalki - 1)
      return a ** wynik
      
print(wielpotengowanie(3,3,3))
