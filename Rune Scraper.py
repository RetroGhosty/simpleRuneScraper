import requests
from bs4 import BeautifulSoup
from os import system, name

class championList:
   

    def showChampion(self):
        champ_lib = {}
        URL = "https://champion.gg/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        champss = soup.find_all('div', class_='champ-height')

        for cList in champss:
            cName = cList.find('span', class_='champion-name').text
            roles = cList.find('a', attrs={'style': 'display:block'})
            d_roles = list(roles.stripped_strings)
            d_role = "\n\n".join(d_roles) if d_roles else ""
            champ_lib[cName] = d_role
            
        return champ_lib

    def showRunes(self, name):
        self.name = name
        champ_list = championList()
        daList = champ_list.showChampion()
        url = "https://champion.gg/champion/{}/{}?".format(self.name, daList[self.name])

        mainList = []
        subList = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        pRune = soup.find_all('div', class_='Slot__Block-epLguL iEzUxo')
        
        for highestRune in pRune:
            try:
                main = highestRune.find('div', class_='Description__Title-jfHpQH bJtdXG', attrs={'color': '#9faafc'})
                mainList.append(main.text)
                
            except AttributeError:
                continue

        del mainList[6:-1] 
    
        
        
        for subrune in pRune:
            try:
                sub = subrune.find('div', class_='Description__Title-jfHpQH eOLOWg', attrs={'color':'#d44242'})
                subList.append(sub.text)
                
            except AttributeError:
                continue

        del subList[0]
        del subList[1:-1]
     
    
        mainList.insert(4, subList[0])
        mainList.insert(5, subList[1])
        mainList.insert(4, " ")
        mainList.insert(7, " ")

        print("-=-=-=-=-=-=-{}-=-=-=-=-=-=-\n".format(self.name))
        for a in mainList:
            print(a)
        print("-=-=-=-=-=Highest Winrate=-=-=-=-=-\n")    
    
def clear():
    if name == 'nt':
        _ = system('cls')
      

while True:
     try:
        champ_list  = championList()
        stringChamp = input("Champion Name: ")
        champ_list.showRunes(stringChamp)

        clears = input("")
        clear()
     except KeyError:
        continue
    


