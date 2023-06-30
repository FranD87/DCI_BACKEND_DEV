Python-algorithmic_thinking-bubblesort
Implement the bubblesort presented in pseudo code below in Python in the bubblesort.py file. Then run the app.py file to test your implementation. The output should be "Congratulations! No error detected.".

BEGIN BubbleSort(list)
swaps = false
FOR i FROM zero TO (LENGTH OF list MINUS 1)
IF list[i] > list[i+1]
SWAP(list[i], list[i+1])
swaps = true
ENDIF
ENDFOR
IF swaps == true
BubbleSort(list)
ENDIF
RETURN list
END BubbleSort