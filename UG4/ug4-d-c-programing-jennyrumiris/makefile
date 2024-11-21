

test_hello1: 
	gcc hello.c -o hello.out
	./hello.out < input/hello1input.txt > your_hello1.txt
	if diff your_hello1.txt output/hello1output.txt; then \
		echo "\033[0;32m passed test1 \033[0m"; \
	else \
		echo "\033[0;31m not passed test 1 \033[0m"; \
	fi

test_hello2: 
	gcc hello.c -o hello.out
	./hello.out < input/hello2input.txt > your_hello2.txt
	if diff your_hello2.txt output/hello2output.txt; then \
		echo "\033[0;32m passed test2 \033[0m"; \
	else \
		echo "\033[0;31m not passed test 2 \033[0m"; \
	fi

test_mario2: 
	gcc mario.c -o mario.out
	./mario.out < input/mario2input.txt > your_mario2.txt
	if diff your_mario2.txt output/mario2output.txt; then \
		echo "\033[0;32m passed test 2 \033[0m"; \
	else \
		echo "\033[0;31m not passed test 2 \033[0m"; \
	fi

test_mario3:
	gcc mario.c -o mario.out
	./mario.out < input/mario3input.txt > your_mario3.txt
	if diff your_mario3.txt output/mario3output.txt; then \
		echo "\033[0;32m passed test 3 \033[0m"; \
	else \
		echo "\033[0;31m not passed test 3 \033[0m"; \
	fi

test_mario4:
	gcc mario.c -o mario.out
	./mario.out < input/mario4input.txt > your_mario4.txt
	if diff your_mario4.txt output/mario4output.txt; then \
		echo "\033[0;32m passed test 4 \033[0m"; \
	else \
		echo "\033[0;31m not passed test 4 \033[0m"; \
	fi
