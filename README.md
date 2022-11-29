### 담당 거래소
- 바이낸스: 경섭
- 코인베이스: 승흠
- 업비트: 창주

### 대락젹인 플로우차트
1. 거래소별 api써서 가격 긁어오기
2. if문으로 중복 코인을 비교하고 같은 페어끼리 가격을 비교

- 심화: 특정 거래소에서 가격 긁어오는게 에러 -> 이전 가격 쓰던지 아니면 스킵하던지

- 만약 이전 가격 쓰면 3회 이상 에러 -> 텔그로 노티

- 30초 간격으로 해서 2번 과정에서 이상치 발생하면 알림 보내기

### 1번 플로우차트 가이드라인
- 결과물: list of dictionaries
- dictionary element는 3개의 key를 가지고 있어야 함
  - `symbol`: {코인 이름}/USDT 형식으로
  - `price`: 해당 페어 가격 (가능하다면 종가로)
  - `volume`: 해당 페어의 거래량
- spot에 올라간 파생상품 코인 (BTCUP, BTCDOWN) 등은 제외
  - 제외한 방식: `/binance/test.py` 참고

- [CCXT 레포](https://github.com/ccxt/ccxt) 활용
- 짤막하게 만든 구현체: `/binance/test.py` 참고

- 코드와 진행사항 Pull request 활용 공유

- api key, telegram bot token / chat ID 같이 private한 정보는 깃헙에 올리지 않고 서로 공유 (테스트할 때 .gitignore로 private한 정보가 깃업에 올라가지 못하도록 할 수 있음.)

- 거래소별 데이터 취합하고 알림 모니터링하는 2번 작업은 `app.py`에서 진행. 추후 코드 추가 예정.