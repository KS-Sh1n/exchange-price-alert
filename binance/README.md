## 거래소 가격 불러오기 (Binance)

### [CCXT 레포](https://github.com/ccxt/ccxt)
1. `pip install ccxt`로 ccxt 라이브러리 설치

- [파이썬 텔레그램 봇](https://github.com/python-telegram-bot/python-telegram-bot/wiki/) 활용 (텔레그램 봇 버전은 20.0a4로 통일)

- 깃헙을 통해 코드와 진행사항 공유 (Pull request 활용)

- api key, telegram bot token / chat ID 같이 private한 정보는 깃업에 올리지 않고 서로 공유 (테스트할 때 .gitignore로 private한 정보가 깃업에 올라가지 못하도록 할 수 있음.)

### 대락젹인 플로우차트
1. 거래소별 api써서 가격 긁어오기
2. if문으로 중복 코인을 비교하고 같은 페어끼리 가격을 비교

심화: 특정 거래소에서 가격 긁어오는게 에러 -> 이전 가격 쓰던지 아니면 스킵하던지

만약 이전 가격 쓰면 3회 이상 에러 -> 텔그로 노티

30초 간격으로 해서 2번 과정에서 이상치 발생하면 알림 보내기