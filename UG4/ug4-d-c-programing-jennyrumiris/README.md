[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AjpjTMkw)
# UG5-PrakTekom-C-Template
ug 5 prak tekom about introducing C
## 1. Hello, Its's Me (Score 30)
Dalam file bernama hello.c, buatlah program dalam C yang meminta inputan nama pengguna dan kemudian menyapa pengguna tersebut. Misalnya, jika nama penggunanya adalah Dendy, program Anda akan mencetak hello, Dendy\n!

Contoh : 
```c
$ make hello                                                                    
$ ./hello                                                                       
Siapakah namamu? Dendy
hello, Dendy
$ ./hello                                                                       
Siapakah namamu? Dida
hello, Dida
$
```
               
## 2. Mario Pyramid 
a. Dalam file bernama mario.c, buatlah program dalam C yang menggambar sebuah piramida menggunakan karakter hash(#). (Score 40)

Contoh dibawah ini : 
```c
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

b. modifikasi program diatas agar jumlah tingkatan piramida dapat di-inputkan melalui prompt input. (Score 30)

Contoh 
```c
$ ./mario                                                                       
Tinggi piramida: 8                                                                       
       #                                                                        
      ##                                                                        
     ###                                                                        
    ####                                                                        
   #####                                                                        
  ######                                                                        
 #######                                                                        
########
                                                                   
$ ./mario                                                                       
Tinggi piramida: 3
  #                                                                        
 ##                                                                        
###                                                                        
```

lakukan pengecekan dengan command sebagai berikut:
- make test_hello1
- make test_hello2
- make test_mario2
- make test_mario3
- make test_mario4
(Note: jangan lupa save file lalu compile terlebih dahulu dan namakan output file dengan .out)
```c
gcc hello.c -o hello.out
gcc mario.c -o mario.out
```
