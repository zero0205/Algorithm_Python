def solution(goods):
  goodslen = len(goods)
  
  
  #각각의 문자열(pencil)로 만들 수 있는 모든 경우의 문자열(p,e,n,c,i,l,pe,en,...,pencil)을 넣을 집합 리스트
  goodsset= [set() for _ in range(goodslen)]
  for i in range(goodslen):
    #strlen : 집합에 저장할 문자열 길이 
    strlen = 1
    itemlen = len(goods[i])
    while strlen <= itemlen:
      #start : 문자열 시작점
      for start in range(itemlen-strlen+1):
       goodsset[i].add(goods[i][start:start+strlen])
      strlen += 1
  
  #차집합(고유 검색어)를 저장할 리스트
  result = []
  for i in range(goodslen):
    newset = goodsset[i]
    for j in range(goodslen):
      if i == j:
        continue
      #고유 검색어를 찾음
      newset = newset.difference(goodsset[j])
    if newset:
      #고유 검색어 정렬
      newsetArray = sorted(list(newset), key=lambda x: (len(x), x))
      #가장 짧은 고유 검색어의 길이
      first = len(newsetArray[0])
      #가장 짧은 고유 검색어들을 저장할 리스트
      newsetResult = []
      for i in newsetArray:
        if len(i) != first:
          #고유 검색어 길이가 가장 짧은것보다 긴 것은 처리안함
          break
        newsetResult.append(i)
      #고유 검색어 리스트 -> 문자열로 바꿈
      result.append(' '.join(newsetResult))
    else:
      result.append("None")
  return result
      
print(solution(["pencil","cilicon","contrabase","picturelist"]))
print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))