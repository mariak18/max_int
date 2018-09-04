# Notandi setur inn tölu í num_int
# max_int byrjar sem 0 
# meðan num_int er stærra eða jafnt og 0 
# ef num_int er stærra en max_int þá setjum við aðra tölu inn 
# max_int verður þá num_int 
# svo lengi sem num_int er ekki mínus tala þá heldur loopan áfram 
# um leið og slegið verður inn mínus tölu prentar forritið hæstu töluni sem var slegin inn 
 
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0 

while num_int >= 0 :
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
    
    

# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line
