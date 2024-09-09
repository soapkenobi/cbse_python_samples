def fact(n):
  factorial=1
  for i in range(1,n+1):
      factorial*=i
  return factorial

def combination(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))
def max_comb_str_length(rows):
    rows-=1
    s = ''
    for i in range(rows+1):
        s += f"{combination(rows, i)} "
    return len(s)

rows=int(input())
max_row_length = max_comb_str_length(rows)
for i in range(rows):
    row = ''
    for j in range(i+1):
        row += f"{combination(i,j)} "
    print(row.center(max_row_length))
