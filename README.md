# Python3 코딩 테스트 풀이

* [프로그래머스](https://programmers.co.kr/learn/challenges)
* [이것이 취업을 위한 코딩 테스트다](https://github.com/ndb796/python-for-coding-test)

## Programming Tips

### 내장 함수

1. `isalpha()` : 문자열이 알파벳([a-zA-Z])으로만 구성되었는지 확인하는 파이썬 문자열 메소드

```python
print('abcD'.isalpha())
>> >
True
```

2. `isalnum()` : 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열 메소드

```python
print('ab123'.isalnum())
>> >
True
```

3. `isdigit()` : 문자열이 숫자([0-0])로만 구성되었는지 확인하는 파이썬 문자열 메소드

```python
print('1234'.isdigit())
>> >
True
```

4. `divmod(num, divide)` : divide로 나눈 몫과 나머지를 리턴

```python
print(divmod(7, 3)), print(*divmod(7, 3))
>> >
(2, 1), 2
1

# 무조건 divmod를 사용하는 게 좋은 방법은 아닙니다.
# 가독성이나, 팀의 코드 스타일에 따라서, a//b, a%b와 같이 쓸 때가 더 좋을 수도 있습니다.
# 또한, divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느립니다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르지요.
```