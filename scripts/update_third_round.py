from pathlib import Path
import html
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ("Home", "index.html"),
    ("Research", "research.html"),
    ("People", "people.html"),
    ("Projects", "projects.html"),
    ("Facilities", "facilities.html"),
    ("Publications", "publications.html"),
    ("Activities", "activities.html"),
    ("Contact", "contact.html"),
]

def header(title, desc="공주대학교 신소재공학과 신구조재료실험실 ASML 공식 홈페이지"):
    nav = "\n".join([f'        <a href="{href}">{label}</a>' for label, href in NAV])
    return f'''<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="{html.escape(desc)}" />
    <meta property="og:title" content="{html.escape(title)}" />
    <meta property="og:description" content="공주대학교 신소재공학과 신구조재료실험실. 고온 금속재료, 수소취성, 초내열합금, Ti/Zr 합금 및 소재 데이터 분석 연구." />
    <meta property="og:type" content="website" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="theme-color" content="#243241" />
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="index.html" aria-label="ASML home">
        <span class="brand-mark">ASML</span>
        <span class="brand-text"><strong>Advanced Structural Materials Lab</strong><span>Kongju National University</span></span>
      </a>
      <nav class="site-nav" aria-label="Primary navigation">
{nav}
      </nav>
    </header>
'''

def footer():
    return '''    <footer class="site-footer"><span>ASML, Kongju National University · Department of Advanced Materials Engineering</span><a href="index.html">Back to home</a></footer>
    <script type="module" src="script.js"></script>
  </body>
</html>
'''

def page(title, eyebrow, h1, lead, body):
    return header(f"ASML | {title}") + f'''    <main id="top">
      <section class="page-hero"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p></section>
{body}
    </main>
''' + footer()

def img_or_placeholder(slug, alt):
    p = ROOT / "assets" / "people" / f"{slug}.jpg"
    if p.exists():
        return f'<div class="member-photo"><img src="./assets/people/{slug}.jpg" alt="{html.escape(alt)}" loading="lazy" /></div>'
    return '<div class="member-photo placeholder">Photo</div>'

def member_card(name_ko, name_en, role, topics, slug):
    topic_html = "".join(f"<li>{html.escape(t)}</li>" for t in topics)
    return f'''          <article class="member-card">{img_or_placeholder(slug, name_en or name_ko)}<p class="role">{html.escape(role)}</p><h3>{html.escape(name_ko)}</h3><p class="member-name-en">{html.escape(name_en)}</p><ul class="member-topics">{topic_html}</ul></article>'''

phd = [
    ("정윤종", "Yun Jong Jung", "Ph.D. Student", ["Refractory high entropy alloys", "Hydrogen embrittlement"], "jung-yoonjong"),
    ("이강진", "Kang Jin Lee", "Ph.D. Student", ["Refractory high entropy alloys", "Hydrogen embrittlement"], "lee-kangjin"),
]
masters = [
    ("신승환", "Seung Hwan Shin", "M.S. Student", ["Refractory high entropy alloys"], "shin-seunghwan"),
    ("최순원", "Soon Won Choi", "M.S. Student", ["Ferritic high entropy alloys"], "choi-soonwon"),
    ("임성진", "Seong Jin Im", "M.S. Student", ["Hydrogen embrittlement"], "im-seongjin"),
    ("허민아", "Min A Heo", "M.S. Student", ["Refractory high entropy alloys"], "heo-mina"),
    ("박상민", "Sang Min Park", "M.S. Student", ["Ferritic high entropy alloys"], "park-sangmin"),
    ("권민철", "Min Cheol Kwon", "M.S. Student", ["Hydrogen embrittlement"], "kwon-mincheol"),
]
undergrads = [
    ("신윤지", "Yoon Ji Shin", "Undergraduate Researcher", ["Hydrogen embrittlement"], "shin-yoonji"),
    ("김동현", "Dong Hyun Kim", "Undergraduate Researcher", ["Refractory high entropy alloys"], "kim-donghyun"),
    ("임정현", "Jeong Hyeon Im", "Undergraduate Researcher", ["Refractory high entropy alloys"], "im-jeonghyeon"),
    ("곽선영", "Seon Yeong Kwak", "Undergraduate Researcher", ["Zr alloys"], "kwak-seonyeong"),
]
alumni = [
    ("김종태", "Jong Tae Kim", "Alumni", ["High entropy alloys", "Ni-based superalloys", "Current: 생산기술연구원"], "kim-jongtae"),
    ("송호섭", "Ho Seop Song", "Alumni", ["High entropy alloys", "Magnetic materials", "Current: (주) 삼기"], "song-hoseop"),
    ("조병찬", "Byung Chan Cho", "Alumni", ["3D printing (Maraging steels)", "Ferritic superalloys", "Current: (주) 창성"], "cho-byungchan"),
    ("김정은", "Jeong Eun Kim", "Alumni", ["Ferritic superalloys", "Current: 특허 사무소"], "kim-jeongeun"),
    ("Hamza", "Syed Muhammad Hamza Ifthikar", "Alumni", ["High entropy alloys", "Current: RMIT University"], "hamza-ifthikar"),
    ("박강현", "Kang Hyun Park", "Alumni", ["Ferritic superalloys", "High entropy alloys", "Current: 한국재료연구원"], "park-kanghyun"),
]

def section_cards(title, records):
    cards = "\n".join(member_card(*r) for r in records)
    return f'''      <section class="section member-section"><div class="section-heading compact"><p class="eyebrow">People</p><h2>{title}</h2></div><div class="member-grid">\n{cards}\n        </div></section>'''

people_body = f'''      <section class="section split"><div class="section-heading"><p class="eyebrow">People</p><h2>함께 실험하고, 분석하고, 논문으로 완성하는 팀.</h2><p>구성원 정보는 기존 Google Sites 공개 페이지와 사용자 확인 내용을 반영했습니다. 학생 이메일은 공개 페이지에서 제외하고, 이름·과정·연구분야·사진 중심으로 정리했습니다.</p></div><div class="people-panel"><article class="person-card featured-person"><img class="profile-photo" src="./assets/prof-gian-song.jpg" alt="Prof. Gian Song profile photo" loading="lazy" /><div><p class="role">Principal Investigator</p><h3>Prof. Gian Song · 송기안</h3><p>국립공주대학교 신소재공학부 부교수. 금속재료 설계와 특성 분석, 고엔트로피합금, BCC 기반 초합금, 크리프 최적화, Zr 클래드 소재, 분말야금·주조 비교 연구, 3D 프린팅 금속 소재를 주요 연구 분야로 다룹니다.</p><div class="external-links"><a href="https://ame.kongju.ac.kr/ZD0400/3000/subview.do" target="_blank" rel="noreferrer">KNU faculty profile</a><a href="https://scholar.google.com/citations?user=EVA0x3IAAAAJ&amp;hl=en" target="_blank" rel="noreferrer">Google Scholar</a></div></div></article></div></section>
{section_cards('Ph.D. students', phd)}
{section_cards('Master\'s course', masters)}
{section_cards('Undergraduate researchers', undergrads)}
{section_cards('Alumni', alumni)}'''
(ROOT / "people.html").write_text(page("People", "People", "함께 실험하고, 분석하고, 논문으로 완성하는 팀.", "현재 구성원, 학부 연구생, 졸업생을 카드형 프로필로 정리했습니다.", people_body), encoding="utf-8")

projects = [
    ("화신볼트 인코넬 체결류 공정 최적화", "초내열 인코넬(Inconel 718) 체결류의 원소재 품질 편차, 단조 불량, 숙련공 의존형 공정 설계 문제를 AI 기반 공정 최적화로 해결하기 위한 산학 프로젝트입니다.", "2026.06 - 2027.02", "Partner: 화신볼트산업"),
    ("한화오션 초내열 인코넬 체결류 실증", "차세대 에너지·조선 산업용 초내열 인코넬 체결류의 제조 공정 체계화 및 실증 연구입니다.", "2026.04.01 - 2028.12.31", "Partner: 한화오션 관련"),
    ("응력-온도 감응형 내화성 다중 주원소 합금", "머신러닝 기반 Screw-Edge 전위 이동도 제어를 통한 내화성 다중 주원소 합금 개발 과제입니다.", "2026.03.01 - 2031.02.28", "공주대 주관 핵심연구B"),
    ("고압수소 이송용 심리스강관", "중·장거리 고압수소배관용 485 MPa급 고강도 심리스강관의 미세조직과 수소취성 거동을 연구합니다.", "2024.07.01 - 2028.12.31", "Hydrogen embrittlement, pipeline steels"),
    ("초고내식 Fe계 잉곳·슬래브 공정", "Fe 0.06% 이하 초고내식 7톤급 잉곳 및 대형 슬래브 제조 최적화 공정 기술개발 과제입니다.", "2024.07.01 - 2028.12.31", "Corrosion resistance, slab processing"),
    ("금속소재 제조디지털혁신 플랫폼", "금속소재 공정, 물성, 데이터 기반 해석을 연결하는 디지털 제조혁신 플랫폼 구축 연구입니다.", "2022.07 - 2026.12", "한국재료연구원 관련"),
    ("Ti/Zr 클래드 소재", "Ti, Zr계 모합금 슬라브 제조, 클래드 압연 및 제품화 기술개발과 관련된 공정·부식·산화 연구입니다.", "진행 과제 영역", "Ti/Zr alloys, cladding, corrosion"),
]
project_cards = "\n".join([f'''          <article><h3>{html.escape(name)}</h3><p>{html.escape(desc)}</p><ul class="meta-list"><li><strong>Period</strong><span>{html.escape(period)}</span></li><li><strong>Note</strong><span>{html.escape(note)}</span></li></ul></article>''' for name, desc, period, note in projects])
projects_body = f'''      <section class="section projects-section"><div class="section-heading compact"><p class="eyebrow">Current Projects</p><h2>최근 시작 과제 순으로 정리한 현재 연구과제.</h2><p>화신볼트 및 한화오션 인코넬 과제를 현재 과제에 포함했습니다. 예산, 내부 담당자, 세부 역할은 공개 확인 후 추가합니다.</p></div><div class="project-grid expanded-grid">\n{project_cards}\n        </div><div class="project-note"><strong>Education and training</strong><span>BK21 등 대학원 교육·연구역량 강화 프로그램과 학부 연구생, 석사, 박사 과정 연구 참여를 연계합니다.</span></div></section>'''
(ROOT / "projects.html").write_text(page("Projects", "Projects", "현재 과제를 최근 시작 순으로 정리했습니다.", "화신볼트 인코넬 과제와 한화오션 인코넬 과제를 포함해 공개 가능한 과제명과 기간 중심으로 배열했습니다.", projects_body), encoding="utf-8")

# Publications: use high/medium confidence records from the clean index, grouped by year.
pub_path = Path(r"C:\Users\user\Hermes_Workspace\knowledge\achievements\publications_clean.xlsx")
df = pd.read_excel(pub_path)
df = df[df["confidence_level"].astype(str).str.lower().isin(["high", "medium"])]
df = df[~df["title"].astype(str).str.contains("논문실적현황", na=False)]
df["year"] = pd.to_numeric(df["year"], errors="coerce").fillna(0).astype(int)
df = df.sort_values(["year", "title"], ascending=[False, True])

def valid(v):
    if pd.isna(v):
        return False
    s = str(v).strip()
    return bool(s) and s != "확인 필요" and s.lower() != "nan"

groups = []
for year, g in df.groupby("year", sort=False):
    if year == 0:
        continue
    items = []
    for _, r in g.iterrows():
        title = html.escape(str(r["title"]).strip())
        authors = html.escape(str(r["authors"]).strip()) if valid(r.get("authors")) else ""
        journal = html.escape(str(r["journal"]).strip()) if valid(r.get("journal")) else ""
        vol = html.escape(str(r["volume_issue_pages"]).strip()) if valid(r.get("volume_issue_pages")) else ""
        doi = str(r["DOI"]).strip() if valid(r.get("DOI")) else ""
        meta = " · ".join(x for x in [authors, journal, vol] if x)
        doi_html = f'<p class="pub-links"><a href="https://doi.org/{html.escape(doi.replace("https://doi.org/", ""))}" target="_blank" rel="noreferrer">doi:{html.escape(doi.replace("https://doi.org/", ""))}</a></p>' if doi else ""
        items.append(f'''            <article class="publication-entry"><h3>{title}</h3>{f'<p>{meta}</p>' if meta else ''}{doi_html}</article>''')
    groups.append(f'''        <section class="publication-year"><h2>{year}</h2><div class="publication-year-list">\n{chr(10).join(items)}\n          </div></section>''')

pub_body = f'''      <section class="section publications"><div class="section-heading compact"><p class="eyebrow">Publications</p><h2>Full publication list by year</h2><p>아래 목록은 publications_clean.xlsx에서 confidence가 high 또는 medium인 정리 항목을 연도별로 구성한 공개용 전체 리스트입니다. DOI는 확인된 항목만 연결했습니다.</p></div><div class="publication-summary"><h3>Publication list summary</h3><p>Displayed records: {len(df)}. Source: C:\\Users\\user\\Hermes_Workspace\\knowledge\\achievements\\publications_clean.xlsx</p></div><div class="publication-years">\n{chr(10).join(groups)}\n        </div></section>'''
(ROOT / "publications.html").write_text(page("Publications", "Publications", "전체 논문 목록을 연도별로 정리했습니다.", "대표 논문뿐 아니라 clean index의 검증 수준이 높은 논문 기록을 연도별로 확인할 수 있습니다.", pub_body), encoding="utf-8")

# Update home summary wording.
index_path = ROOT / "index.html"
index_html = index_path.read_text(encoding="utf-8")
index_html = index_html.replace("한화오션 과제를 포함한 현재 과제를 최근 시작 순으로 정리.", "화신볼트·한화오션 인코넬 과제를 포함한 현재 과제를 최근 시작 순으로 정리.")
index_path.write_text(index_html, encoding="utf-8")

print("updated people, projects, publications, and home summary")
print("publication_records", len(df))
