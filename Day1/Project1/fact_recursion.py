def tri_recursion(k):
  if k > 0:
         return	k * tri_recursion(k-1)
  else: 
 	 return 1

print("\n\nRecursion Example Results")
print(tri_recursion(6))
	
