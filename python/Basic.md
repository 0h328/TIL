# ★Python 총정리★



[TOC]

# 1. 데이터

##### ![image-20210731115856708](Mydoc.assets/image-20210731115856708.png)

![image-20210731115916988](Mydoc.assets/image-20210731115916988.png)

### ![image-20210731115943091](Mydoc.assets/image-20210731115943091.png)

![image-20210731120008819](Mydoc.assets/image-20210731120008819.png)![image-20210731120017828](Mydoc.assets/image-20210731120017828.png)

**매우중요! 줄 바꿈할 때는 print()를 사용하기도 한다. 대신 들여쓰기 확인

![image-20210731120034798](Mydoc.assets/image-20210731120034798.png)

![image-20210731120056643](Mydoc.assets/image-20210731120056643.png)

![image-20210731120206715](Mydoc.assets/image-20210731120206715.png)

# 2. 컨테이너

![image-20210731120318691](Mydoc.assets/image-20210731120318691.png)



## 2.1 시퀀스

### 2.1.1 list

![image-20210731120355275](Mydoc.assets/image-20210731120355275.png)![image-20210731120405355](Mydoc.assets/image-20210731120405355.png)![image-20210731145454990](Mydoc.assets/image-20210731145454990.png)

###### .append(x) : 리스트에 값을 추가 ![image-20210731145518635](Mydoc.assets/image-20210731145518635.png)

###### .extend(iterable) : 리스트에 iterable 항목 추가

![image-20210731145554507](Mydoc.assets/image-20210731145554507.png)

###### .insert(i, x) 

![image-20210731145628051](Mydoc.assets/image-20210731145628051.png)



###### .remove(x) : 리스트에서 값이 x인 것 삭제 ![image-20210731145758639](Mydoc.assets/image-20210731145758639.png)

###### .pop(i) 

![image-20210731145849139](Mydoc.assets/image-20210731145849139.png)

###### .clear() : 모든 항목을 삭제함 ![image-20210731145939332](Mydoc.assets/image-20210731145939332.png)

###### .index(x) : x 값을 찾아 해당 index 값을 반환 ![image-20210731150016699](Mydoc.assets/image-20210731150016699.png)

###### .count(x) : 원하는 값의 개수를 반환 ![image-20210731150037962](Mydoc.assets/image-20210731150037962.png)

###### .sort()와 sorted 함수의 차이점은? .sort()는 원본 리스트를 정렬하고 None 반환. sorted함수는 원본 변경 없음.

![image-20210731150144747](Mydoc.assets/image-20210731150144747.png)



###### .map(function, iterable)

![image-20210731151321371](Mydoc.assets/image-20210731151321371.png)

![image-20210731151342051](Mydoc.assets/image-20210731151342051.png)

list(map(int, input().split())) 에서 '1 3 5 7'이 들어왔다면, 이걸 int형식으로 변환하여 list화 시킴.



###### .filter(function, iterable)

![image-20210731151437915](Mydoc.assets/image-20210731151437915.png)

###### .zip(*iterables)![image-20210731151517987](Mydoc.assets/image-20210731151517987.png)

2차원 배열 사용시 for i in zip(*iterables) 사용!! 



###### **리스트 복사 

![image-20210731150513957](Mydoc.assets/image-20210731150513957.png)

###### *얕은 복사1

![image-20210731150546571](Mydoc.assets/image-20210731150546571.png)



###### *얕은 복사2

![image-20210731150600499](Mydoc.assets/image-20210731150600499.png)

###### *얕은 복사 주의사항

![image-20210731150715700](Mydoc.assets/image-20210731150715700.png)

###### *깊은 복사

![image-20210731150742003](Mydoc.assets/image-20210731150742003.png)

###### *list comprehension

 ![image-20210731151035682](Mydoc.assets/image-20210731151035682.png)![image-20210731151048434](Mydoc.assets/image-20210731151048434.png)<-1~3 중 짝수 list

![image-20210731151156073](Mydoc.assets/image-20210731151156073.png)



### 2.1.2 tuple

![image-20210731120551771](Mydoc.assets/image-20210731120551771.png)

![image-20210731120638035](Mydoc.assets/image-20210731120638035.png)![image-20210731120710530](Mydoc.assets/image-20210731120710530.png)![image-20210731120723523](Mydoc.assets/image-20210731120723523.png)



### 2.1.3 range

![image-20210731120928370](Mydoc.assets/image-20210731120928370.png)



### 2.1.4 문자열

![image-20210731121057754](Mydoc.assets/image-20210731121057754.png)![image-20210731144558421](Mydoc.assets/image-20210731144558421.png)![image-20210731144618931](Mydoc.assets/image-20210731144618931.png)

![image-20210731144702845](Mydoc.assets/image-20210731144702845.png)

###### .find(x) : x의 첫번째 위치를 반환. 없으면, -1을 반환함.![image-20210731144825706](Mydoc.assets/image-20210731144825706.png)

###### .index(x) : x의 첫번째 위치를 반환. 없으면, 오류 발생![image-20210731144850802](Mydoc.assets/image-20210731144850802.png)

###### .replace(old, new[,count]) ![image-20210731144924868](Mydoc.assets/image-20210731144924868.png)

###### .strip([chars]) : 양쪽 제거.lstrip([chars]) : 왼쪽 제거 .rstrip([chars]) : 오른쪽 제거

![image-20210731145029243](Mydoc.assets/image-20210731145029243.png)

###### .split([chars]) : 문자열을 특정한 단위로 나눠 리스트로 반환

![image-20210731145134683](Mydoc.assets/image-20210731145134683.png)

###### 'separater'.join([iterable]) : 반복가능한 컨테이너 요소들을 separater(구분자)로 합쳐 문자열 반환

![image-20210731145225291](Mydoc.assets/image-20210731145225291.png)

###### 이외에 ![image-20210731145257642](Mydoc.assets/image-20210731145257642.png)![image-20210731145314786](Mydoc.assets/image-20210731145314786.png)

![image-20210731145332242](Mydoc.assets/image-20210731145332242.png)![image-20210731145356762](Mydoc.assets/image-20210731145356762.png)



### 2.1.5 slicing, len, count는 위 4개(list, tuple, range, 문자열)만 가능

![image-20210731121531864](Mydoc.assets/image-20210731121531864.png)![image-20210731121540899](Mydoc.assets/image-20210731121540899.png)![image-20210731121549523](Mydoc.assets/image-20210731121549523.png)![image-20210731121557746](Mydoc.assets/image-20210731121557746.png)

### 2.1.6 연산자

![image-20210731121618555](Mydoc.assets/image-20210731121618555.png)

## 2.2 비시퀀스

### 2.2.1 세트 ![image-20210731151545314](Mydoc.assets/image-20210731151545314.png)

![image-20210731121836064](Mydoc.assets/image-20210731121836064.png)![image-20210731121853645](Mydoc.assets/image-20210731121853645.png)![image-20210731121925650](Mydoc.assets/image-20210731121925650.png)![image-20210731121957787](Mydoc.assets/image-20210731121957787.png)

###### .add(element) ![image-20210731151607585](Mydoc.assets/image-20210731151607585.png)

###### .update(*others) ![image-20210731151622266](Mydoc.assets/image-20210731151622266.png)

###### .remove(element) ![image-20210731151638298](Mydoc.assets/image-20210731151638298.png)

###### .discard(element)![image-20210731151651802](Mydoc.assets/image-20210731151651802.png)

###### .pop() ![image-20210731151718866](Mydoc.assets/image-20210731151718866.png)![image-20210731151725009](Mydoc.assets/image-20210731151725009.png)

### 2.2.2 딕셔너리

![image-20210731122215946](Mydoc.assets/image-20210731122215946.png)![image-20210731151746442](Mydoc.assets/image-20210731151746442.png)

![image-20210731122226347](Mydoc.assets/image-20210731122226347.png)



![image-20210731122239021](Mydoc.assets/image-20210731122239021.png)

###### .get(key[,default])![image-20210731151822874](Mydoc.assets/image-20210731151822874.png)

###### .pop(key[,default])![image-20210731151851642](Mydoc.assets/image-20210731151851642.png)

![image-20210731152000906](Mydoc.assets/image-20210731152000906.png)

###### .update() ![image-20210731152015786](Mydoc.assets/image-20210731152015786.png)

###### *딕셔너리 순회 ![image-20210731152034082](Mydoc.assets/image-20210731152034082.png)

![image-20210731152049362](Mydoc.assets/image-20210731152049362.png)

![image-20210731152103777](Mydoc.assets/image-20210731152103777.png)

###### *dictionary comprehension

![image-20210731152143178](Mydoc.assets/image-20210731152143178.png)

## 2.3 컨테이너 간 형변환 및 분류

![image-20210731122404332](Mydoc.assets/image-20210731122404332.png)

![image-20210731122429186](Mydoc.assets/image-20210731122429186.png)

![image-20210731122539308](Mydoc.assets/image-20210731122539308.png)

![image-20210731122551259](Mydoc.assets/image-20210731122551259.png)

![image-20210731122600694](Mydoc.assets/image-20210731122600694.png)

![image-20210731122611483](Mydoc.assets/image-20210731122611483.png)

# 3. 제어문

![image-20210731123123092](Mydoc.assets/image-20210731123123092.png)

## 3.1 조건문

![image-20210731123139795](Mydoc.assets/image-20210731123139795.png)

![image-20210731123210083](Mydoc.assets/image-20210731123210083.png)

## 3.2 반복문

![image-20210731123227899](Mydoc.assets/image-20210731123227899.png)

### 3.2.1 while문

![image-20210731123257810](Mydoc.assets/image-20210731123257810.png)

![image-20210731123317035](Mydoc.assets/image-20210731123317035.png)

### 3.2.2 for문

![image-20210731123403083](Mydoc.assets/image-20210731123403083.png)

![image-20210731123526408](Mydoc.assets/image-20210731123526408.png)

![image-20210731123538099](Mydoc.assets/image-20210731123538099.png)

![image-20210731153953066](Mydoc.assets/image-20210731153953066.png)

###### break  ![image-20210731154040632](Mydoc.assets/image-20210731154040632.png)![image-20210731154046136](Mydoc.assets/image-20210731154046136.png)

###### continue ![image-20210731154123379](Mydoc.assets/image-20210731154123379.png)

![image-20210731154132050](Mydoc.assets/image-20210731154132050.png)

###### for-else ![image-20210731154233633](Mydoc.assets/image-20210731154233633.png)

![image-20210731154241169](Mydoc.assets/image-20210731154241169.png)

###### pass와 continue의 차이 ![image-20210731154322001](Mydoc.assets/image-20210731154322001.png)

# 4. 함수

```python
def 함수명(x, y):
    return x + y

print(함수명(2,3)) = 5
```



![image-20210731155127567](Mydoc.assets/image-20210731155127567.png)

![image-20210731155859542](Mydoc.assets/image-20210731155859542.png)

![image-20210731155912505](Mydoc.assets/image-20210731155912505.png)

![image-20210731155922920](Mydoc.assets/image-20210731155922920.png)

## 4.1 인자

### 4.1.1 위치 인자

### ![image-20210731160028528](Mydoc.assets/image-20210731160028528.png)

![image-20210731160034569](Mydoc.assets/image-20210731160034569.png)

![image-20210731160112113](Mydoc.assets/image-20210731160112113.png)

![image-20210731160117401](Mydoc.assets/image-20210731160117401.png)

### 4.1.2 키워드 인자![image-20210731160128777](Mydoc.assets/image-20210731160128777.png)

![image-20210731160134425](Mydoc.assets/image-20210731160134425.png)

add(x=2, 5) --> 불가

add(2, y=5) --> 가능

### 4.1.3 가변 인자

![image-20210731160227969](Mydoc.assets/image-20210731160227969.png)

![image-20210731160236801](Mydoc.assets/image-20210731160236801.png)

### 4.1.4 가변 키워드 인자

![image-20210731160258944](Mydoc.assets/image-20210731160258944.png)

![image-20210731160303529](Mydoc.assets/image-20210731160303529.png)

### 4.1.5 함수 정의 주의 사항

![image-20210731160332305](Mydoc.assets/image-20210731160332305.png)

![image-20210731160343402](Mydoc.assets/image-20210731160343402.png)![image-20210731160349089](Mydoc.assets/image-20210731160349089.png)

![image-20210731160355041](Mydoc.assets/image-20210731160355041.png)

## 4.2 함수 스코프

![image-20210731160637887](Mydoc.assets/image-20210731160637887.png)

![image-20210731160704246](Mydoc.assets/image-20210731160704246.png)

### 4.2.1 LEGB

![image-20210731160731410](Mydoc.assets/image-20210731160731410.png)

![image-20210731160750794](Mydoc.assets/image-20210731160750794.png)

## 4.3 재귀함수(recursive function)

![image-20210731160932922](Mydoc.assets/image-20210731160932922.png)

*변수 사용 적게 가능. but, 메모리 사용 많음, 속도가 느림.

### 4.3.1 팩토리얼

![image-20210731161352298](Mydoc.assets/image-20210731161352298.png)

### 4.3.2 피보나치



## 4.4 예외(Exception)



### 4.4.1 에러

![image-20210731162407134](Mydoc.assets/image-20210731162407134.png)

![image-20210731162416364](Mydoc.assets/image-20210731162416364.png)

![image-20210731162432105](Mydoc.assets/image-20210731162432105.png)

![image-20210731162438696](Mydoc.assets/image-20210731162438696.png)

![image-20210731162452824](Mydoc.assets/image-20210731162452824.png)

![image-20210731162502776](Mydoc.assets/image-20210731162502776.png)

![image-20210731162509312](Mydoc.assets/image-20210731162509312.png)

![image-20210731162516416](Mydoc.assets/image-20210731162516416.png)

![image-20210731162524561](Mydoc.assets/image-20210731162524561.png)

![image-20210731162540145](Mydoc.assets/image-20210731162540145.png)

### 4.4.2 예외 처리

![image-20210731162602605](Mydoc.assets/image-20210731162602605.png)

![image-20210731162643009](Mydoc.assets/image-20210731162643009.png)![image-20210731162647632](Mydoc.assets/image-20210731162647632.png)

![image-20210731162717529](Mydoc.assets/image-20210731162717529.png)

![image-20210731162815024](Mydoc.assets/image-20210731162815024.png)![image-20210731162820984](Mydoc.assets/image-20210731162820984.png)

![image-20210731162950849](Mydoc.assets/image-20210731162950849.png)

![image-20210731163009120](Mydoc.assets/image-20210731163009120.png)

![image-20210731163106017](Mydoc.assets/image-20210731163106017.png)



###### raise ![image-20210731163125480](Mydoc.assets/image-20210731163125480.png)![image-20210731163149026](Mydoc.assets/image-20210731163149026.png)

###### assert![image-20210731163204160](Mydoc.assets/image-20210731163204160.png)

![image-20210731163212432](Mydoc.assets/image-20210731163212432.png)

# 5. OOP

![image-20210731163441872](Mydoc.assets/image-20210731163441872.png)

![image-20210731163504674](Mydoc.assets/image-20210731163504674.png)

isinstance(10, int)

10이 class 'int'로 만들어졌냐? T

isinstance(10, object)

10이 class 'object'에 포함되어있냐? T

isinstance(0, (bool, int, complex)) -> 하나라도 일치하면 T임

0이 bool~complex 안에 포함되어있냐? T

![image-20210731163606008](Mydoc.assets/image-20210731163606008.png)![image-20210731163614352](Mydoc.assets/image-20210731163614352.png)![ima

print(r1.area())  ,   print(r2.circumference()) 식으로 부름.

![image-20210731163704367](Mydoc.assets/image-20210731163704367.png)

## 5.1 클래스와 인스턴스

![image-20210731163723448](Mydoc.assets/image-20210731163723448.png)

![image-20210731163739936](Mydoc.assets/image-20210731163739936.png)

### 5.1.1 속성

![image-20210731163816890](Mydoc.assets/image-20210731163816890.png)

### 5.1.2 메서드

![image-20210731163827209](Mydoc.assets/image-20210731163827209.png)

### 5.1.3 self

![image-20210731163846240](Mydoc.assets/image-20210731163846240.png)

### 5.1.4 생성자

![image-20210731163858489](Mydoc.assets/image-20210731163858489.png)

### 5.1.5 소멸자

![image-20210731163908808](Mydoc.assets/image-20210731163908808.png)

### 5.1.6 매직 메서드

![image-20210731163923353](Mydoc.assets/image-20210731163923353.png)

### 5.1.7 인스턴스 변수

![image-20210731164354160](Mydoc.assets/image-20210731164354160.png)

![image-20210731164359679](Mydoc.assets/image-20210731164359679.png)

각각의 instance는 독립적이다 -> 항상 특정 instance에 묶여있음. -> 오로지 해당 객체에만 영향

(instance1 변경 시, instance2에 영향 X)

instance는 class메서드와 static메서드에 접근 가능.

class에 저장되지 않고, class에서 생성된 개별 객체에 저장



### 5.1.8 클래스 변수

![image-20210731164413248](Mydoc.assets/image-20210731164413248.png)

c2.pi = 3.141592로 바꾸면

print(c2.pi)는 3.141592로 바뀌고 print(c1.pi)는 그대로 3.14

### 5.1.9 인스턴스와 클래스 간의 이름 공간

![image-20210731164442224](Mydoc.assets/image-20210731164442224.png)

![image-20210731164452849](Mydoc.assets/image-20210731164452849.png)

![image-20210731164509208](Mydoc.assets/image-20210731164509208.png)

## 5.2 메서드![image-20210731164550911](Mydoc.assets/image-20210731164550911.png)

### 5.2.1 인스턴스 메서드

![image-20210731164605336](Mydoc.assets/image-20210731164605336.png)

instance_method 호출 시, 반드시 자동으로 self가 오든, self가 있어야함.

Class가 instance_method를 부르려면, Class명.instance_method(instance명) 으로 부른다.

MyClass.instance_method() -> TypeError 발생. (self 값을 넣을 방법 없음.)

instance가 class에 접근은 가능하여, class상태를 수정할 수는 있으나 절대 하면 안됨.

### 5.2.2 클래스 메서드

![image-20210731164615056](Mydoc.assets/image-20210731164615056.png)

cls 인자에만 접근 가능하여, instance 상태 수정 불가능.

### 5.2.3 스태틱 메서드

![image-20210731164623576](Mydoc.assets/image-20210731164623576.png)

임의 개수의 매개 변수를 받을 수는 있음.

self와 cls의 매개 변수는 사용 불가능.

### 5.2.4 메서드 정리

![image-20210731164646121](Mydoc.assets/image-20210731164646121.png)

![image-20210731164702273](Mydoc.assets/image-20210731164702273.png)

![image-20210731164717920](Mydoc.assets/image-20210731164717920.png)

## 5.3 상속

상속하는 이유는 상위클래스의 메서드를 가져와야 할때, 부모 클래스와의 공통점이 있을때

![image-20210731164737336](Mydoc.assets/image-20210731164737336.png)

![image-20210731164753880](Mydoc.assets/image-20210731164753880.png)

![image-20210731164824192](Mydoc.assets/image-20210731164824192.png)

### 5.3.1 issubclass

![image-20210731164850296](Mydoc.assets/image-20210731164850296.png)

### 5.3.2 super()

![image-20210731164904960](Mydoc.assets/image-20210731164904960.png)

### 5.3.3 메서드 오버라이딩

![image-20210731164921296](Mydoc.assets/image-20210731164921296.png)

### 5.4 상속 정리

![image-20210731164936232](Mydoc.assets/image-20210731164936232.png)

