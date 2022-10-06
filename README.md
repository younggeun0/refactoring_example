# [리팩터링 2판 1장-예시](http://www.yes24.com/Product/Goods/89649360?pid=123487&cosemkid=go15851280284143301&gclid=Cj0KCQjw1vSZBhDuARIsAKZlijTu055egKPyid3969hBjfURb41ji0hWJ3TjczJvF-ONEwET6_rYgqwaArRXEALw_wcB)

> 커밋 단위로 리팩터링하는 과정을 기록

예시 코드는 연극정보(`play.json`), 청구서(`invoices.json`) 데이터를 가지고 관람 총액과 적립 포인트를 plainText로 출력하는 프로그램

### 리팩터링1
- 출력 결과가 plainText가 아닌 html로 출력되는 기능이 추가된다면? => `단개쪼개기`

### 리팩터링2
- 비극, 희극 외 다른 장르의 연극이 추가된다면? => `조건부 로직을 다형성으로 바꾸기`


---

위부터 아래로 순서대로 진행
- [assert 코드](https://github.com/younggeun0/refactoring_example/commit/5a86eab6359dc1ed4d639e6c06a3d262b4104310)가 최초에 누락됐지만 매 단계마다`컴파일-테스트-커밋` 반복

## 1. [최초 프로그램](https://github.com/younggeun0/refactoring_example/commit/6976a62cd62383f05853d6353a1bdc17f56a1b00)

## 2. 기능 추가 전 기존 코드를 중첩함수로 리팩터링
- [금액 계산 코드를 중첩 함수로 추출](https://github.com/younggeun0/refactoring_example/commit/19bfa0cba5f590458221cd8ebc94e8989c5d5633)
- [매개변수, 변수명을 명확히](https://github.com/younggeun0/refactoring_example/commit/12720b64b6980def3c46f746a172fa857b3bd9aa)
- [임시 변수를 질의 함수로 바꾸기](https://github.com/younggeun0/refactoring_example/commit/80bb4356522a20f227e3b76074ac44c86f0068f9)
- [변수 인라인하기](https://github.com/younggeun0/refactoring_example/commit/7f0a6cecea0d373601d7cde95619f7acc8920aed)
- [함수 선언 바꾸기](https://github.com/younggeun0/refactoring_example/commit/212ba410d57bb353466372723ccb7b74621978e0)
- [변수 인라인하기](https://github.com/younggeun0/refactoring_example/commit/e37f62132a3003eb65bf7013756905ec9c9a1cb1)
- [적립 포인트 계산 코드도 함수로 추출](https://github.com/younggeun0/refactoring_example/commit/4de62874a77a10a8515045215349daa88aa28cfa)
- [매개변수, 변수명을 명확히](https://github.com/younggeun0/refactoring_example/commit/4285c13687e26043e03567830d857e28524a2fc5)
- [함수 임시 변수를 직접 선언해 사용하도록 변경](https://github.com/younggeun0/refactoring_example/commit/35180adcd0b07d2cbaaa0823c624a0ceb7c6f4c5)
- [함수 선언 바꾸기](https://github.com/younggeun0/refactoring_example/commit/d4c1543b1296c779a92dc6c5af67b7bc39476600)
- [독립적인 작업을 수행하기 위해 반복문 쪼개기](https://github.com/younggeun0/refactoring_example/commit/e13f83a415ce9e371226fcc5150889179a5abd06)
- [문장 슬라이드하기](https://github.com/younggeun0/refactoring_example/commit/f2fe32031dcd58147c764161760070495eb46d22)
- [적립 포인트 총합 계산 코드를 함수로 추출](https://github.com/younggeun0/refactoring_example/commit/70f2a2df26abb0941b653928585c8b3ff8317079)
- [변수를 인라인하기](https://github.com/younggeun0/refactoring_example/commit/0576781f6d994ce0e05ef4b7631202b9559e842e)
- [총 금액 계산 코드도 함수로 추출](https://github.com/younggeun0/refactoring_example/commit/ba8887487b92ea3d323cdbe0fafa7459fc2a1683)
- [변수 인라이하기, 함수 선언 바꾸기](https://github.com/younggeun0/refactoring_example/commit/eda96f41ed6f2dc71f144755bb8dbf4964d1a77e)
- [변수명을 명확히](https://github.com/younggeun0/refactoring_example/commit/eabd3843fadc2a11db51943ab6eb311537645486)

## 3. 계산 단계와 포맷팅 단계를 분리하는 단계 쪼개기

- [단계 쪼개기 시작, 렌더 함수 분리](https://github.com/younggeun0/refactoring_example/commit/90069ee4ac428da999990a7a0ab9702e8ad46458)
- [매개변수로 전달할 중간 데이터 구조 생성](https://github.com/younggeun0/refactoring_example/commit/413ab26eadb552dffdb7ac61014f9bedf83ea86e)
- [렌더 함수에서 중간 데이터 구조로 데이터를 옮김1](https://github.com/younggeun0/refactoring_example/commit/e5611ce29a3ccf4ad165047fc0c769a595ee5546)
- [렌더 함수에서 중간 데이터 구조로 데이터를 옮김2](https://github.com/younggeun0/refactoring_example/commit/b66832707511d4f9b59d05eabf694f827d382a4e)
- [렌더 함수에서 중간 데이터 구조로 데이터를 옮김3](https://github.com/younggeun0/refactoring_example/commit/972f85bef3f06caa854ab9fa6662752189fb654a)
- [렌더 함수에서 중간 데이터 구조로 데이터를 옮김4](https://github.com/younggeun0/refactoring_example/commit/00a0d651c480f83709bf7bf63192bddd5feba0a3)
- [렌더 함수에서 중간 데이터 구조로 데이터를 옮김5](https://github.com/younggeun0/refactoring_example/commit/0b089bef8a3cb79f5e61e88bf5b824ef4006cfd9)
- [렌더 함수에서 중간 데이터 구조로 데이터를 옮김6](https://github.com/younggeun0/refactoring_example/commit/9fd5e1f247a917f00902d422deaddd89326a6073)
- [렌더 함수에서 중간 데이터 구조로 데이터를 옮김7](https://github.com/younggeun0/refactoring_example/commit/e95247a5bfa0a0d770c0aaab534afbbcc1866df6)
- [반복문을 파이프라인으로 바꾸기](https://github.com/younggeun0/refactoring_example/commit/3b5e145953588f3495972f83025d4779cfdb3867)
- [데이터 처리에 해당하는 코드를 함수로 추출](https://github.com/younggeun0/refactoring_example/commit/ed4ecb06db466b477404307772e02da41b3dba27)
- [데이터 처리 코드를 별도 파일로 분리](https://github.com/younggeun0/refactoring_example/commit/09d6bd62c08cee2ac4706da0129d55874480cbea)

## 4. [HTML 포맷팅 기능 추가](https://github.com/younggeun0/refactoring_example/commit/fd51dbd050ed97c23b4a9d0421748066edb6d0da)

## 5. 연극 장르를 쉽게 추가 가능하도록 조건부 로직을 다형성으로 바꾸기

- [상속 계층 정의, 금액과 적립 포인트를 계산하는 부모 클래스 추가](https://github.com/younggeun0/refactoring_example/commit/be9d253049d5ed10e9fa558edeb1881efaecc3b9)
- [함수 선언 바꾸기](https://github.com/younggeun0/refactoring_example/commit/ff3086d4dbbf9f4f71660b03daaeaa00e0454701)
- [금액 구하는 코드를 클래스로 옮기기](https://github.com/younggeun0/refactoring_example/commit/7f7013649fd6178061403f54aa349eb6e7c3a9c4)
- [적립 포인트 구하는 코드를 클래스로 옮기기](https://github.com/younggeun0/refactoring_example/commit/96eae0db9c14f01d5632d55c3733f14e4fa63dc6)
- [타입 코드를 서브 클래스로 바꾸기, 생성자를 팩터리 함수로 변경](https://github.com/younggeun0/refactoring_example/commit/28748801129c5dd7ca32fc24213da4174e32c8a4)
- [조건부 로직을 다형성으로 바꾸기, 금액과 적립 포인트를 서브 클래스에서 계산](https://github.com/younggeun0/refactoring_example/commit/bbd7f40facd190e247740d457bb4733b204ae2cc)