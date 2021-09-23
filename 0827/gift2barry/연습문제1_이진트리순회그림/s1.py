'''
         A
        | \
       B   C
      | w  |w
     D  E  F G
    |w  |  w |w
   H I  J  K L M

1. 전위 순회 : 가운데 -> 왼쪽 -> 오른쪽
    A -> B -> D -> H -> I -> E -> J -> C -> F -> K -> G -> L -> M

2. 중위 순회 :
    H -> D -> I -> B -> J -> E -> A -> F -> K -> C -> L -> G -> M

3. 후위 순회 :
    H -> I -> D -> J -> E -> B -> K -> F -> L -> M -> G -> C -> A
'''