from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]

def read_base_functions():
    # Reuse the simple page shell from update_third_round.py without executing its top-level updates.
    text = (ROOT / "scripts" / "update_third_round.py").read_text(encoding="utf-8")
    return text

NAV = [("Home", "index.html"),("Research", "research.html"),("People", "people.html"),("Projects", "projects.html"),("Facilities", "facilities.html"),("Publications", "publications.html"),("Activities", "activities.html"),("Contact", "contact.html")]

def header(title, desc="공주대학교 신소재공학과 신구조재료실험실 ASML 공식 홈페이지"):
    nav = "\n".join([f'        <a href="{href}">{label}</a>' for label, href in NAV])
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><meta name="description" content="{html.escape(desc)}" /><meta property="og:title" content="{html.escape(title)}" /><meta property="og:description" content="공주대학교 신소재공학과 신구조재료실험실. 고온 금속재료, 수소취성, 초내열합금, Ti/Zr 합금 및 소재 데이터 분석 연구." /><meta property="og:type" content="website" /><meta name="twitter:card" content="summary_large_image" /><meta name="theme-color" content="#243241" /><title>{html.escape(title)}</title><link rel="stylesheet" href="styles.css" /></head><body><header class="site-header"><a class="brand" href="index.html" aria-label="ASML home"><span class="brand-mark">ASML</span><span class="brand-text"><strong>Advanced Structural Materials Lab</strong><span>Kongju National University</span></span></a><nav class="site-nav" aria-label="Primary navigation">\n{nav}\n      </nav></header>\n'''

def footer():
    return '''    <footer class="site-footer"><span>ASML, Kongju National University · Department of Advanced Materials Engineering</span><a href="index.html">Back to home</a></footer><script type="module" src="script.js"></script></body></html>\n'''

def page(title, eyebrow, h1, lead, body):
    return header(f"ASML | {title}") + f'''    <main id="top"><section class="page-hero"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p></section>\n{body}\n    </main>\n''' + footer()

def img_or_placeholder(slug, alt):
    p = ROOT / "assets" / "people" / f"{slug}.jpg"
    if p.exists():
        return f'<div class="member-photo"><img src="./assets/people/{slug}.jpg" alt="{html.escape(alt)}" loading="lazy" /></div>'
    return '<div class="member-photo placeholder">Photo</div>'

def member_card(name_ko, name_en, role, topics, slug):
    topic_html = "".join(f"<li>{html.escape(t)}</li>" for t in topics)
    return f'''          <article class="member-card">{img_or_placeholder(slug, name_en or name_ko)}<p class="role">{html.escape(role)}</p><h3>{html.escape(name_ko)}</h3><p class="member-name-en">{html.escape(name_en)}</p><ul class="member-topics">{topic_html}</ul></article>'''

def section_cards(title, records):
    return f'''      <section class="section member-section"><div class="section-heading compact"><p class="eyebrow">People</p><h2>{title}</h2></div><div class="member-grid">\n{chr(10).join(member_card(*r) for r in records)}\n        </div></section>'''

phd=[("정윤종","Yun Jong Jung","Ph.D. Student",["Refractory high entropy alloys","Hydrogen embrittlement"],"jung-yoonjong"),("이강진","Kang Jin Lee","Ph.D. Student",["Refractory high entropy alloys","Hydrogen embrittlement"],"lee-kangjin")]
masters=[("신승환","Seung Hwan Shin","M.S. Student",["Refractory high entropy alloys"],"shin-seunghwan"),("최순원","Soon Won Choi","M.S. Student",["Ferritic high entropy alloys"],"choi-soonwon"),("임성진","Seong Jin Im","M.S. Student",["Hydrogen embrittlement"],"im-seongjin"),("허민아","Min A Heo","M.S. Student",["Refractory high entropy alloys"],"heo-mina"),("박상민","Sang Min Park","M.S. Student",["Ferritic high entropy alloys"],"park-sangmin"),("권민철","Min Cheol Kwon","M.S. Student",["Hydrogen embrittlement"],"kwon-mincheol")]
undergrads=[("신윤지","Yoon Ji Shin","Undergraduate Researcher",["Hydrogen embrittlement"],"shin-yoonji"),("김동현","Dong Hyun Kim","Undergraduate Researcher",["Refractory high entropy alloys"],"kim-donghyun"),("임정현","Jeong Hyeon Im","Undergraduate Researcher",["Refractory high entropy alloys"],"im-jeonghyeon"),("곽선영","Seon Yeong Kwak","Undergraduate Researcher",["Zr alloys"],"kwak-seonyeong")]
alumni=[("김종태","Jong Tae Kim","Alumni",["High entropy alloys","Ni-based superalloys","Current: 생산기술연구원"],"kim-jongtae"),("송호섭","Ho Seop Song","Alumni",["High entropy alloys","Magnetic materials","Current: (주) 삼기"],"song-hoseop"),("조병찬","Byung Chan Cho","Alumni",["3D printing (Maraging steels)","Ferritic superalloys","Current: (주) 창성"],"cho-byungchan"),("김정은","Jeong Eun Kim","Alumni",["Ferritic superalloys","Current: 특허 사무소"],"kim-jeongeun"),("Hamza","Syed Muhammad Hamza Ifthikar","Alumni",["High entropy alloys","Current: RMIT University"],"hamza-ifthikar"),("박강현","Kang Hyun Park","Alumni",["Ferritic superalloys","High entropy alloys","Current: 한국재료연구원"],"park-kanghyun")]
people_body=f'''      <section class="section split"><div class="section-heading"><p class="eyebrow">People</p><h2>함께 실험하고, 분석하고, 논문으로 완성하는 팀.</h2><p>구성원 정보와 사진은 기존 Google Sites 공개 페이지와 사용자 확인 내용을 반영했습니다. 학생 이메일은 공개 페이지에서 제외하고, 이름·과정·연구분야·사진 중심으로 정리했습니다.</p></div><div class="people-panel"><article class="person-card featured-person"><img class="profile-photo" src="./assets/prof-gian-song.jpg" alt="Prof. Gian Song profile photo" loading="lazy" /><div><p class="role">Principal Investigator</p><h3>Prof. Gian Song · 송기안</h3><p>국립공주대학교 신소재공학부 부교수. 금속재료 설계와 특성 분석, 고엔트로피합금, BCC 기반 초합금, 크리프 최적화, Zr 클래드 소재, 분말야금·주조 비교 연구, 3D 프린팅 금속 소재를 주요 연구 분야로 다룹니다.</p><div class="external-links"><a href="https://ame.kongju.ac.kr/ZD0400/3000/subview.do" target="_blank" rel="noreferrer">KNU faculty profile</a><a href="https://scholar.google.com/citations?user=EVA0x3IAAAAJ&amp;hl=en" target="_blank" rel="noreferrer">Google Scholar</a></div></div></article></div></section>\n{section_cards('Ph.D. students',phd)}\n{section_cards("Master's course",masters)}\n{section_cards('Undergraduate researchers',undergrads)}\n{section_cards('Alumni',alumni)}'''
(ROOT/'people.html').write_text(page('People','People','함께 실험하고, 분석하고, 논문으로 완성하는 팀.','현재 구성원, 학부 연구생, 졸업생을 카드형 프로필로 정리했습니다.',people_body),encoding='utf-8')

projects=[
("차세대 에너지 산업용 초내열 인코넬 체결류 제조 공정 체계화 및 실증 연구","화신볼트산업 등 산학협력 기반의 인코넬 718 체결류 공정 체계화·실증 과제입니다.","2026.04.01 - 2028.12.31","공공연구성과 실증 시범사업 / 주관: 공주대학교 산학협력단"),
("응력-온도 감응형 내화성 다중 주원소 합금","머신러닝 기반 Screw-Edge 전위 이동도 제어를 통한 내화성 다중 주원소 합금 개발 과제입니다.","2026.03.01 - 2031.02.28","공주대 주관 핵심연구B"),
("잠수함용 고심도 해수환경 합금 및 배관 제작 기술 개발","한화오션 슈퍼을 후보/active current 과제로, 고심도 해수환경 합금 및 배관 제작 기술 개발 관련 연구입니다.","review_required; 2026.07.01 - 2032.12.31 후보","한화오션 슈퍼을 / source evidence 확인 필요"),
("고압수소 이송용 심리스강관","중·장거리 고압수소배관용 485 MPa급 고강도 심리스강관의 미세조직과 수소취성 거동을 연구합니다.","2024년 시작 확인; 총 연구기간 확인 필요","Hydrogen embrittlement, pipeline steels"),
("초고내식 Ti, Zr계 모합금 슬라브 제조, 클래드 압연 및 제품화 기술개발","기존 Ti/Zr 클래드 소재 항목과 같은 과제로, Ti·Zr계 모합금 슬라브 제조, 클래드 압연 및 제품화 기술을 다룹니다.","2024 - 2028","Zr클래딩 / 산업기술혁신사업 기반 과제"),
("금속소재 제조디지털혁신 플랫폼 구축","금속소재 공정, 물성, 데이터 기반 해석을 연결하는 디지털 제조혁신 플랫폼 구축 연구입니다.","2022 - 2025 추정; 협약서 확인 필요","가상공학 2단계"),
("모빌리티 소재·부품 개발을 위한 AX 제조혁신 인재양성","첨단제조융합인재육성지원사업 관련 포닥양성/인재양성 과제입니다.","확인 필요","needs_source_evidence_current"),
("4단계 BK21 사업 4차산업용 첨단소재 인력양성팀","대학원 교육·연구역량 강화 프로그램과 연구실 학부·석사·박사 과정 연구 참여를 연계합니다.","2020년 이후; 총 사업기간 확인 필요","BK21")]
proj_cards='\n'.join(f'''          <article><h3>{html.escape(n)}</h3><p>{html.escape(d)}</p><ul class="meta-list"><li><strong>Period</strong><span>{html.escape(p)}</span></li><li><strong>Note</strong><span>{html.escape(note)}</span></li></ul></article>''' for n,d,p,note in projects)
proj_body=f'''      <section class="section projects-section"><div class="section-heading compact"><p class="eyebrow">Current Projects</p><h2>Obsidian/Project Registry 기준 현재 과제 목록.</h2><p>Project Registry와 Obsidian preview를 확인해 현재 과제를 정리했습니다. Ti/Zr 클래드 소재는 초고내식 Ti, Zr계 모합금 슬라브·클래드 압연 과제로 통합했습니다. review_required 항목은 공개 확정 전 확인이 필요합니다.</p></div><div class="project-grid expanded-grid">\n{proj_cards}\n        </div></section>'''
(ROOT/'projects.html').write_text(page('Projects','Projects','현재 과제를 Project Registry 기준으로 정리했습니다.','인코넬, 중견/RMPEA, 한화오션, 수소강관, Zr클래딩, 가상공학, 포닥양성, BK 과제를 포함했습니다.',proj_body),encoding='utf-8')

def gallery(files, caption_prefix):
    cards=[]
    for f in files:
        stem=Path(f).stem.replace('-', ' ')
        cards.append(f'''          <figure class="visual-card"><img src="./{f}" alt="{html.escape(caption_prefix + ' ' + stem)}" loading="lazy" /><figcaption>{html.escape(stem)}</figcaption></figure>''')
    return '<div class="visual-grid gallery-grid">\n'+'\n'.join(cards)+'\n        </div>'
facility_imgs=[f'assets/google-sites/research-facility-{i:02d}.png' for i in range(1,15) if (ROOT/f'assets/google-sites/research-facility-{i:02d}.png').exists()]
fac_body=f'''      <section class="section facilities-section"><div class="section-heading compact"><p class="eyebrow">Facilities</p><h2>기존 홈페이지의 Research & Facility 내용을 확장 반영했습니다.</h2><p>Alloy design, microstructural characterization, mechanical properties, neutron analysis 흐름과 장비 사진을 함께 정리했습니다.</p></div><div class="facility-list expanded-grid"><article><h3>Alloy design</h3><p>Arc/induction-melting and melt-spinning facilities for ferritic steels, Ni-based superalloys, Mg-, Ti-, Al-based alloys, HEA and BMG alloy systems.</p></article><article><h3>Microstructural characterization</h3><p>TEM, EBSD, atom probe tomography, neutron/synchrotron diffraction을 활용한 합금계 미세조직 분석.</p></article><article><h3>Mechanical properties</h3><p>Creep, phase-transformation/twin-induced plasticity, precipitation strengthening, shear-banding deformation 등 금속재료 기계적 특성 평가.</p></article><article><h3>Neutron analysis</h3><p>Ni-based superalloys와 NiAl/Ni2TiAl 석출강화 ferritic alloys의 in-situ loading neutron diffraction 분석.</p></article></div></section><section class="section visual-section"><div class="section-heading compact"><p class="eyebrow">Facilities Gallery</p><h2>장비 및 연구 인프라 이미지</h2><p>기존 Google Sites 공개 홈페이지에서 가져온 장비·연구 이미지입니다.</p></div>{gallery(facility_imgs,'ASML facility image')}</section>'''
(ROOT/'facilities.html').write_text(page('Facilities','Facilities','제조, 열처리, 분석, 기계시험을 연결하는 연구 인프라.','기존 홈페이지의 장비 이미지와 연구분야 설명을 함께 반영했습니다.',fac_body),encoding='utf-8')
activity_imgs=[f'assets/google-sites/activity-{i:02d}.jpg' for i in range(1,18) if (ROOT/f'assets/google-sites/activity-{i:02d}.jpg').exists()] + [f'assets/google-sites/activity-{i:02d}.png' for i in range(1,18) if (ROOT/f'assets/google-sites/activity-{i:02d}.png').exists()]
# Keep visual order by numeric stem.
activity_imgs=sorted(activity_imgs, key=lambda x: int(Path(x).stem.split('-')[-1]))
award_imgs=[f for f in ['assets/google-sites/home-03.png'] if (ROOT/f).exists()]
act_body=f'''      <section class="section news-section"><div class="section-heading compact"><p class="eyebrow">News &amp; Awards</p><h2>Lab updates, student awards, and certificates</h2><p>기존 홈페이지의 수상 기록과 상장 이미지를 함께 반영했습니다.</p></div>{gallery(award_imgs,'ASML award certificate')}</section><section class="section activities-section"><div class="section-heading compact"><p class="eyebrow">Activities</p><h2>Conferences, collaborations, and lab events</h2><p>기존 Google Sites Activity 페이지의 학회·국제협력·워크숍·학위수여식·동계 lab MT 사진을 최대한 가져왔습니다.</p></div><div class="activity-list"><article><time>2025</time><h3>금속재료학회 및 공동연구 활동</h3><p>2025 추계·춘계 금속재료학회와 관련 활동.</p></article><article><time>2024</time><h3>MS&amp;T conference, 학회, lab workshop</h3><p>국제공동연구, 추계·춘계 학회, 하계 lab workshop.</p></article><article><time>2023-2019</time><h3>학회, 학위수여식, lab MT</h3><p>TMS conference, 금속재료학회, 학위수여식, 동계 lab MT 등.</p></article></div></section><section class="section visual-section"><div class="section-heading compact"><p class="eyebrow">Activity Gallery</p><h2>연구실 활동 사진</h2></div>{gallery(activity_imgs,'ASML activity image')}</section>'''
(ROOT/'activities.html').write_text(page('News & Activities','News & Awards','Lab updates, student awards, and activities.','수상 기록과 기존 홈페이지의 학회·협력·연구실 활동 사진을 정리했습니다.',act_body),encoding='utf-8')

idx=ROOT/'index.html'
s=idx.read_text(encoding='utf-8').replace('화신볼트·한화오션 인코넬 과제를 포함한 현재 과제를 최근 시작 순으로 정리.','Project Registry 기준 현재 과제와 기존 홈페이지 이미지 보강.')
idx.write_text(s,encoding='utf-8')
print('updated fourth round pages')
print('facility_images',len(facility_imgs),'activity_images',len(activity_imgs),'award_images',len(award_imgs))
