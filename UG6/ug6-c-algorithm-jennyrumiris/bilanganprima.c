#include <stdio.h>
int main(){
        int j,y=1,z,r=0;
        printf("Masukkan Bilangan Bulat Positif : ");
        scanf("%i", &j);
        if(j<=1){
                printf("%i Bukan Bilangan Prima\n", j);
                return 0;
        }
        for (y; y<=j; y++) {
                z = j%y;
                if(z==0)
                        r++;
        }
        if (r==2)
                printf("%i Adalah Bilangan Prima\n", j);
        else
                printf("%i Bukan Bilangan Prima\n", j);
}