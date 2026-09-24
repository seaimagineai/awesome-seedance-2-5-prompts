# Seedance 2.5 프롬프트: 보고, 복사하고, 만들기

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_TW.md) · [日本語](README_JA.md) · [Português](README_PT.md) · [Español](README_ES.md) · [Deutsch](README_DE.md) · [Русский](README_RU.md) · [Français](README_FR.md) · [한국어](README_KO.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md) · [Bahasa Indonesia](README_ID.md) · [Italiano](README_IT.md)

![주황색 전차가 굽은 선로를 따라가고, 거리는 선화에서 종이 모형, 따뜻한 조명의 사실적인 건물로 변합니다.](assets/seaimagine-seedance-hero-v5.jpg)

구조 스케치에서 재질, 조명, 움직임으로 발전하는 창작 구상을 독창적인 장면으로 표현했습니다.

120개 레시피를 중국어 60개와 영어 60개로 제공합니다. 한국어 연습 6개부터 시작해 자신의 아이디어에 맞게 바꿔 보세요.

## 한 장면부터 시작하기

아래 한국어 연습에서 주제를 고르고 피사체, 재질, 카메라 움직임을 바꿔 보세요. SeaImagine에서 입력 방식과 길이를 선택한 뒤 짧은 장면을 먼저 확인하며 다듬습니다.

[한국어 연습 6개](prompts/i18n/prompt-library.ko.md) · [레시피 120개 목록 · 중국어 간체](prompts/README.md)

## 커뮤니티 영상에서 배우기

미리보기를 눌러 움직임과 소리를 살펴보세요. 각 사례에는 작성자의 원문 링크도 있습니다.

### 요리와 소리의 타이밍

[![요리와 소리의 타이밍 — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2099186062715404288/img/D-iYamhA_iFRBooM.jpg)](https://video.twimg.com/amplify_video/2099186062715404288/vid/avc1/1920x1080/H8uxwKxVsSU09_LW.mp4?tag=29)

[작성자의 원문과 프롬프트](https://x.com/Goodmanprotocol/status/2099186117769822462) · **@Goodmanprotocol**

재료의 근접 촬영과 동작에 맞춘 소리가 마지막 웃음을 어떻게 준비하는지 살펴보세요.

### 옷 한 벌로 여러 스타일

[![옷 한 벌로 여러 스타일 — @Goodmanprotocol](https://pbs.twimg.com/amplify_video_thumb/2095216899445649408/img/690ykZJzst5uQLwH.jpg)](https://video.twimg.com/amplify_video/2095216899445649408/vid/avc1/1920x1080/LZt4YKiTkMag5Db1.mp4?tag=29)

[작성자의 원문과 프롬프트](https://x.com/Goodmanprotocol/status/2095216981624721691) · **@Goodmanprotocol**

옷의 색과 구조를 유지하고 비슷한 동작으로 스타일 전환을 연결하세요.

[커뮤니티 사례 12개 전체 · 영어](README.md) · [공식 사례와 출처 · 영어](docs/official-examples.md)

## 프롬프트 기본 구조

```text
[목표] 사용자, 용도, 길이, 화면비
[참조 역할] 각 이미지나 영상에 한 가지 역할만 지정
[고정 요소] 인물, 제품, 공간, 조명 중 바뀌면 안 되는 항목
[타임라인] 도입 → 행동 → 전환점 → 최종 프레임
[카메라] 숏 크기, 높이, 경로, 속도, 초점, 정지 위치
[사운드] 대사, 환경음, 효과음, 음악, 동기화 지점
[금지] 형태 변화, 중복, 신체 오류, 가짜 글자, 로고, 워터마크
```

## 제품 영상 프롬프트 복사하기

![탄산차 참조 이미지](assets/product-sparkling-tea-reference.png)

위 이미지를 참고해 브랜드 표시가 없는 병 이미지를 준비하세요. 물방울과 기포를 보여 주는 5초부터 시작하고, 전체 장면은 화면에서 선택할 수 있는 길이에 맞춰 조정하세요.

```text
이미지 1의 투명 유리병을 유일한 제품 기준으로 사용한다. 병 실루엣, 캡, 빈 라벨 비율, 호박색 액체 높이, 응결, 주광 방향을 유지하고 글자를 생성하지 않는다.

00:00–00:05 응결 방울 하나를 매크로로 촬영한 뒤 액체 안의 작은 기포로 초점을 이동한다. 00:05–00:11 시계 방향으로 35도 돌며 천천히 뒤로 이동하고, 얼음 받침의 굴절은 자연스럽게 변하지만 병은 안정적으로 유지한다. 00:11–00:17 따뜻한 역광이 지나가고 캡이 아주 조금 열리며 소량의 안개만 나온다. 00:17–00:24 낮은 히어로 앵글에서 상단 여백을 남기고 정면으로 멈춘다.

소리: 캡, 탄산, 얼음, 최소한의 오리지널 리듬. 추가 병, 라벨 이동, 유리 변형, 액체 관통, 가짜 문자, 로고, 상표, 워터마크 금지.
```

## SeaImagine에서 만들기

![종이 바다 위의 금빛 돛단배와 따뜻한 빛을 비추는 등대.](assets/seaimagine-paper-sea.jpg)

제품 예제의 형태 유지, 질감 지정, 카메라 움직임을 작은 이야기에 적용해 보세요. SeaImagine에서 텍스트로 영상을 만들며 다음 5초 구성을 시도할 수 있습니다.

```text
5초, 하나의 연속 장면. 금빛 종이 돛단배가 청록색 종이 파도 위를 천천히 나아간다. 카메라는 낮은 위치에서 배를 따라가고, 먼 등대가 따뜻한 빛을 비춘다. 선체, 돛, 종이 섬유를 유지한다. 마지막에는 부드럽게 멈춘다. 글자, 로고, 추가 배, 변형은 넣지 않는다.
```

[SeaImagine · Seedance 2.5](https://seaimagine.com/ko/model/seedance-2-5/) · [SeaImagine · Create](https://seaimagine.com/ko/create/)

[한국어 연습 6개](prompts/i18n/prompt-library.ko.md) · [레시피 120개 목록 · 중국어 간체](prompts/README.md) · [제작 안내 · 영어](docs/seaimagine-workflow.md)

[SeaImagine · GitHub](https://github.com/seaimagineai/awesome-seedance-2-5-prompts)

## 출처 및 이용 안내

표지, 종이 바다, 제품 참조 이미지는 AI로 만든 정지 이미지이며 영상 생성 결과가 아닙니다. 연습 프롬프트는 편집한 학습 자료로, 첨부 영상의 원래 지시문과 다르며 생성 테스트를 거치지 않았습니다. 외부 영상의 모델명은 작성자의 설명을 따릅니다. 자료의 권리와 이용 조건은 [출처 안내(영어)](docs/PROVENANCE.md)와 [라이선스(영어)](LICENSE)를 확인하세요.
