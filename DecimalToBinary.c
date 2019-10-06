#include<stdio.h>

void toBinary(int n) {
    /*
    :type a: int
    
    bits: Number of characters to display Eg. 8 bits = 0000000 Which would get filled up till 2^8-1
    >>: Using Right Shift Bitwise operator to get each bit on units place and comparing it with True
    
    Example 1: 
    Input: 2
    Output: 00000010
    
    Example 2:
    Input: 100
    Output: 01100100
    */
    
    int bits = 8;
        for(int i = bits; i >= 0; i--){
            if ((n>>i & 1)== 1) printf("1");
            else printf("0");
        }
}

int main() {
    int n;
    scanf("%d", &n);
    toBinary(n);
}
