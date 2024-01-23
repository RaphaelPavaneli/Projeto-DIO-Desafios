''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
animal = {
    "vertebrado": {
        "ave": {"carnivoro": "aguia", "onivoro": "pomba"},
        "mamifero":{"onivoro": "homem", "herbivoro": "vaca"}
    },
    "invertebrado": {
        "inseto":{"hematofago": "pulga", "herbivoro": "lagarta"},
        "anelideo":{"hematofago": "sanguessuga", "onivoro": "minhoca"}
    }
}

a = input() 
b = input() 
c = input() 


print(animal[a][b][c])