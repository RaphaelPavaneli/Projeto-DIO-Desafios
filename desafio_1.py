#O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.



while True:
    T = input()
    limite_caracteres = 0

    for letra in T: 
        limite_caracteres += 1

    if limite_caracteres >= 1 and limite_caracteres <= 500:
        break


status = "TWEET" if limite_caracteres >= 1 and limite_caracteres <= 140 else "MUTE"
print(status)

if status == "TWEET":
 print(T)


#forma simplificada
T = input()

print ("TWEET" if len(T) >= 1 and len(T) <= 140 else "MUTE")
    