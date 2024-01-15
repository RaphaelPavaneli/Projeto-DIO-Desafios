animal = {
    "vertebrado": {
        "ave": {"carnivoro": "aguia", "onivoro": "pomba"},
        "mamifero":{"onivoro": "homem", "herbivoro": "vaca"}
    },
    "invertebrado": {
        "inseto":{"hematofogo": "pulga", "herbivoro": "lagarta"},
        "anelideo":{"hematofogo": "sanguessuga", "onivoro": "minhoca"}
    }
}

a = input() 
b = input() 
c = input() 


print(animal[a][b][c])