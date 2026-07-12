# HERMES_HANDOFF

이 문서는 Hermes가 KNU ASML 홈페이지 작업을 전담해서 이어받기 위한 인수인계 문서입니다.

## Current Goal

공주대학교 신소재공학과 신구조재료실험실 ASML 홈페이지를 정적 사이트로 관리한다.
사용자는 휴대폰에서 공개 URL을 확인하고, Hermes가 원본 파일을 수정해 사이트를 개선하는 흐름을 원한다.

## Public Preview URL

https://knu-asml-preview.gasongknu.chatgpt.site/

주의: 이 URL은 결과물이다. 직접 접속해서 편집하는 방식이 아니라, 아래 원본 폴더의 파일을 수정해야 한다.

## Source Folder

```text
C:\Users\user\.openclaw\workspace\projects\knuasml-site
```

## Main Files

- `index.html`: 홈페이지 본문, 섹션, 문구
- `styles.css`: 색상, 레이아웃, 반응형 디자인
- `script.js`: 스크롤/네비게이션 동작
- `assets/microstructure.svg`: 첫 화면 이미지
- `README.md`: 사이트 운영 개요
- `CONTENT_TODO.md`: 실제 자료 보강 필요 목록
- `.openai/hosting.json`: OpenAI Sites 프로젝트 ID. 임의 수정 금지

## Current Content Status

현재 홈페이지에는 다음 정보가 반영되어 있다.

- 기존 Google Sites 홈페이지 공개 정보
  - 공주대학교 신소재공학과 신구조재료실험실 ASML
  - 학부연구생, 석사, 박사 과정 모집
  - Office: 2공학관 111호
  - Tel: 041-521-9471
  - 2026 춘계 금속재료학회 임성진 석사 과정 학생 우수논문상
- 로컬 `profile` DB 기반 정보
  - `profile/cv.json`
  - `profile/students.json`
  - `profile/projects.json`
  - `profile/publications.json`
  - `profile/data_map.json`
- 반영된 섹션
  - Home
  - About ASML
  - Research Areas
  - How We Work
  - Join ASML
  - People
  - Projects
  - Facilities
  - Data Infrastructure
  - Publications
  - News
  - Contact

## Data Sources To Use

우선순위:

1. 기존 공개 홈페이지
   - https://sites.google.com/view/knuasml?pli=1
2. 로컬 profile DB
   - `C:\Users\user\.openclaw\workspace\profile\cv.json`
   - `C:\Users\user\.openclaw\workspace\profile\students.json`
   - `C:\Users\user\.openclaw\workspace\profile\projects.json`
   - `C:\Users\user\.openclaw\workspace\profile\publications.json`
   - `C:\Users\user\.openclaw\workspace\profile\data_map.json`
3. ASML/RMPEA 로컬 자료
   - `C:\Users\user\.openclaw\workspace\tmp_asml_all.txt`
   - `C:\Users\user\.openclaw\workspace\tmp_asml_db.txt`
4. Notion/모션
   - 현재 연결 재인증이 필요하다.
   - 재인증 전에는 Notion 정보를 확정 사실처럼 쓰지 않는다.

## Important Current Caveat

Notion/모션 연결은 현재 `oauth_token_invalid_grant` 재인증 오류로 직접 접근되지 않았다.
따라서 현재 홈페이지 최신 버전은 기존 홈페이지 공개 정보 + 로컬 profile DB + ASML/RMPEA 자료 구조 기반이다.

## Local Commands

작업 폴더로 이동:

```powershell
cd C:\Users\user\.openclaw\workspace\projects\knuasml-site
```

개발 서버:

```powershell
npm run dev
```

빌드 검증:

```powershell
npm run build
```

Git 상태 확인:

```powershell
git status --short
```

커밋:

```powershell
git add index.html styles.css script.js assets README.md CONTENT_TODO.md HERMES_HANDOFF.md
git commit -m "Update ASML homepage content"
```

## Deployment

현재 공개 URL은 OpenAI Sites로 배포되어 있다.

Sites project ID:

```text
appgprj_6a5351e4ae2881918140af4a03f36ccd
```

Hermes가 OpenAI Sites 도구/권한을 갖고 있지 않다면 직접 배포하지 말고, 수정 후 커밋까지만 완료한 뒤 송카맨에게 배포를 요청한다.

장기적으로 Hermes 전담 운영을 하려면 GitHub Pages 또는 Cloudflare Pages로 이전하는 편이 가장 안정적이다.

## Editing Rules

- 공개 홈페이지에는 확인된 사실만 쓴다.
- 논문 제목, DOI, 저널명, 연도, 저자 정보는 확인 전 단정하지 않는다.
- 학생 개인정보, 이메일, 학번, 내부 연락처는 공개하지 않는다.
- Notion/모션 정보는 재인증 후 확인된 항목만 반영한다.
- 디자인 변경 시 모바일 화면을 반드시 확인한다.
- 변경 후 `npm run build`를 통과해야 한다.

## Suggested Next Tasks

1. Publications 섹션을 실제 논문 제목, 저널, DOI 기준으로 정리한다.
2. People 섹션에서 현재 구성원 학위과정/연구주제를 사용자가 확인한 뒤 다듬는다.
3. Facilities에 실제 장비 사진 또는 장비명/모델명을 추가한다.
4. Projects에 과제명, 기간, 역할, 지원기관을 공개 가능 범위에서 정리한다.
5. Contact에 이메일 공개 여부를 사용자에게 확인한다.
6. 최종 운영 방식을 GitHub Pages 또는 Cloudflare Pages로 정한다.

## Message To User After Editing

수정 완료 후 사용자에게 다음을 간단히 보고한다.

- 어떤 섹션을 수정했는지
- 어떤 자료를 근거로 삼았는지
- 확인이 필요한 정보가 남아 있는지
- 빌드/배포 여부
- 확인할 공개 URL

