class Beach:
    def __init__(self, location, water_color, temp):
        self.location = location
        self.water_color = water_color
        self.temp = temp
        self.heating_rate = 'hot' if temp > 50 else 'cool'
        self.parts = ['water','sand'] 

    def add_part(self, part):
        self.parts.append(part)
            

if __name__=="__main__": 
    liverpool_beach = Beach('liverpool','red', 70) 
    beach2 = Beach('brighton','yellow', 30) 
    print(liverpool_beach.parts)
    liverpool_beach.add_part('rocks')
    print(liverpool_beach.parts)
