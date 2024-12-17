#include <stdio.h>


int main() {
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(arr[0]);
    int try, a, c;

    printf("Original Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    for(a=0, c=9; a<c; a++, c--){
        try=arr[a];
        arr[a]=arr[c];
        arr[c]=try;
    }
    //proses balik Array

    printf("\nReversed Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}