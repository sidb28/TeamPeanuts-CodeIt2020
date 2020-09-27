input = [{"searchItemName":"Samsung Aircon","items":["Smsng Auon","Amsungh Aircon","Samsunga Airon"]}]

s1 = input[0]["searchItemName"]
items = input[0]["items"]
searchResults = []
resultCosts = []

for s2 in items:
  s1 += " "
  s2 += " "
  k = k1 = k2 = num_operations = 0
  res = ''
  l1 = len(s1)
  l2 = len(s2)
  while(k1<l1 and k2<l2):
    if s1[k1] == s2[k2]:
      res+=s1[k1]
      k1 += 1
      k2 += 1
    else:
      num_operations += 1
      p = s1.index(" ", k1)
      if s2[k2] not in s1[k1:p]:
        res += "+" + s2[k2]
        k2 += 1
      else:
        res += "-" + s1[k1]
        k1 += 1

  while (k < len(res)-4):
    substring = res[k:k+3]
    if ( "+" in substring and "-" in substring and substring.index("+")<substring.index("-") ):
      res = res[0:k]+res[k+1]+res[k+4:-1]
      num_operations -= 1
    k+=1

  searchResults.append(res)
  resultCosts.append(num_operations)

print(searchResults)
