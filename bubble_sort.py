def bubble_sort(n):
    """
    this program takes unsorted list of integers or strings as input 
    and produce sorted list as output
    """
    size = len(n)
    for i in range (size-1):
        swapped = False
        # i implemented swapped variable after the outer for loop as a check for edge cases 
        # where the list is sorted.the outer for loop will iterate only once and produce output.
        for j in range(size-1-i):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
                swapped = True
                
        if not swapped:
            break
    return n
if __name__ == '__main__' :
      n = ["emily","chioma","james","jerome","mathew"]
      x = bubble_sort(n)
      #print(x)
      n = [24,-1,-2,16,2,0]
      y = bubble_sort(n)
      #print(y)
      n = [5,3,16,4,12,2]
      z= bubble_sort(n)
      print(x,y,z)