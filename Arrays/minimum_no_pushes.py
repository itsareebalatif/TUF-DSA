def main():
    minipress("aabbccddeeffgghhiiiiii")
    
def minimumpushes(word):
    freq=[0]*26
    for char in word:
        index=ord(char)-ord('a')
        freq[index]+=1

    freq.sort(reverse=True)
    
    iteration=0
    minipress=0
    for i in range(25):
        if iteration<8:
            one_press_cost=1
        elif iteration<16:
            one_press_cost=2
        elif iteration<24:
            one_press_cost=3
        else:
            one_press_cost=4

        total_cost_of_char=freq[i]*one_press_cost
        minipress+=total_cost_of_char
        iteration+=1
    print(minipress)                


#OPTIMAL SOLUTION
def minipress(word):
    freq=[0]*32
    for char in word:
        index=ord(char)-ord('a')
        freq[index]+=1
    freq.sort(reverse=True)
    press=0
    for i in range(4):
        for j in range(8):
            press+=(i+1)*freq[8*i+j]
    print(press)            



if __name__=="__main__":
    main()
