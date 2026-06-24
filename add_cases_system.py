from pathlib import Path
import datetime
import re

ROOT = Path(__file__).resolve().parent
DOMAIN = "https://www.seoul.gajogae-waste.com"
PHONE = "010-4720-3895"

cases = [
    {
        "slug": "case-001",
        "title": "강남구 가정폐기물 처리 사례",
        "region": "서울 강남구",
        "service": "가정폐기물처리",
        "summary": "이사 후 남은 침대, 장롱, 책상, 생활잡화를 정리한 사례입니다.",
        "items": "침대, 장롱, 책상, 생활잡화",
        "time": "약 3시간",
        "truck": "1톤 차량 1대",
        "before": "before-01.jpg",
        "process": "process-01.jpg",
        "after": "after-01.jpg",
    },
    {
        "slug": "case-002",
        "title": "마포구 원룸 이사폐기물 정리 사례",
        "region": "서울 마포구",
        "service": "이사폐기물처리",
        "summary": "원룸 이사 후 남은 매트리스, 소형가구, 생활폐기물을 정리한 사례입니다.",
        "items": "매트리스, 책상, 의자, 생활폐기물",
        "time": "약 2시간",
        "truck": "1톤 차량 1대",
        "before": "before-05.jpg",
        "process": "process-04.jpg",
        "after": "after-05.jpg",
    },
    {
        "slug": "case-003",
        "title": "영등포구 폐업폐기물 처리 사례",
        "region": "서울 영등포구",
        "service": "폐업폐기물처리",
        "summary": "상가 폐업 후 남은 의자, 책상, 진열대, 잡자재를 정리한 사례입니다.",
        "items": "의자, 책상, 진열대, 잡자재",
        "time": "약 5시간",
        "truck": "1톤 차량 2대",
        "before": "before-09.jpg",
        "process": "process-07.jpg",
        "after": "after-09.jpg",
    },
]

css_add = """
.case-list-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}

.case-list-card {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: var(--shadow);
}

.case-list-card img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
}

.case-list-card div {
  padding: 22px;
}

.case-list-card span {
  display: inline-flex;
  background: #f3e1cc;
  color: var(--main);
  border-radius: 999px;
  padding: 6px 12px;
  font-size: 14px;
  font-weight: 900;
  margin-bottom: 10px;
}

.case-detail-images {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.case-detail-images img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: 20px;
  border: 1px solid var(--line);
}

.backlink-section {
  background: var(--soft2);
}

.backlink-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.backlink-grid a {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 24px;
  box-shadow: var(--shadow);
}

.backlink-grid strong {
  display: block;
  color: var(--main);
  font-size: 21px;
  margin-bottom: 8px;
}

.backlink-grid span {
  color: var(--muted);
}

@media(max-width:900px) {
  .case-list-grid,
  .case-detail-images,
  .backlink-grid {
    grid-template-columns: 1fr;
  }
}
"""

def write_css():
    path = ROOT / "style.css"
    css = path.read_text(encoding="utf-8")
    if ".case-list-grid" not in css:
        path.write_text(css + "\n\n" + css_add, encoding="utf-8")

def case_card(case, prefix="./"):
    return f"""
    <article class="case-list-card">
      <img src="{prefix}images/main/{case['after']}" alt="{case['title']} 작업 후 사진">
      <div>
        <span>{case['region']}</span>
        <h3>{case['title']}</h3>
        <p>{case['summary']}</p>
        <a class="primary-btn" href="{prefix}cases/{case['slug']}/">후기 자세히 보기</a>
      </div>
    </article>
    """

def build_cases_index():
    cases_dir = ROOT / "cases"
    cases_dir.mkdir(exist_ok=True)

    cards = "\n".join(case_card(c, "../") for c in cases)

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>서울 폐기물처리 작업후기 | 가족애폐기물처리</title>
  <meta name="description" content="서울 가족애폐기물처리 작업후기 모음. 가정폐기물, 이사폐기물, 폐업폐기물 처리 사례를 확인하세요.">
  <link rel="canonical" href="{DOMAIN}/cases/">
  <link rel="icon" href="../images/main/favicon.png">
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header class="header">
    <div class="container nav">
      <a class="logo" href="../index.html">가족애폐기물처리<small>서울 폐기물처리 작업후기</small></a>
      <a class="call-btn" href="tel:{PHONE}">{PHONE}</a>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="section-title">
        <span>작업후기</span>
        <h1>서울 폐기물처리 작업후기</h1>
        <p>실제 현장 상황을 바탕으로 정리한 가정폐기물, 이사폐기물, 폐업폐기물 처리 사례입니다.</p>
      </div>
      <div class="case-list-grid">
        {cards}
      </div>
    </div>
  </section>
</body>
</html>
"""
    (cases_dir / "index.html").write_text(html, encoding="utf-8")

def build_case_pages():
    for c in cases:
        d = ROOT / "cases" / c["slug"]
        d.mkdir(parents=True, exist_ok=True)

        html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{c['title']} | 서울 가족애폐기물처리</title>
  <meta name="description" content="{c['region']} {c['service']} 작업후기. {c['summary']} 상담전화 {PHONE}.">
  <link rel="canonical" href="{DOMAIN}/cases/{c['slug']}/">
  <link rel="icon" href="../../images/main/favicon.png">
  <link rel="stylesheet" href="../../style.css">
</head>
<body>
  <header class="header">
    <div class="container nav">
      <a class="logo" href="../../index.html">가족애폐기물처리<small>{c['region']} 작업후기</small></a>
      <a class="call-btn" href="tel:{PHONE}">{PHONE}</a>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="section-title">
        <span>{c['service']}</span>
        <h1>{c['title']}</h1>
        <p>{c['summary']}</p>
      </div>

      <div class="case-detail-images">
        <img src="../../images/main/{c['before']}" alt="{c['title']} 작업 전">
        <img src="../../images/main/{c['process']}" alt="{c['title']} 작업 중">
        <img src="../../images/main/{c['after']}" alt="{c['title']} 작업 후">
      </div>

      <section class="section">
        <div class="cost-box">
          <div>
            <h2>{c['region']} 현장 정리 내용</h2>
            <p>{c['summary']} 현장 상황에 따라 폐기물 양과 반출 동선을 확인한 뒤 작업을 진행했습니다.</p>
          </div>
          <ul class="check-list">
            <li>지역: {c['region']}</li>
            <li>서비스: {c['service']}</li>
            <li>처리 품목: {c['items']}</li>
            <li>작업시간: {c['time']}</li>
            <li>차량: {c['truck']}</li>
          </ul>
        </div>
      </section>

      <div style="text-align:center">
        <a class="primary-btn" href="../../index.html#contact">상담 접수하기</a>
        <a class="secondary-btn" href="../">작업후기 목록</a>
      </div>
    </div>
  </section>
</body>
</html>
"""
        (d / "index.html").write_text(html, encoding="utf-8")

def update_index():
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")

    latest_cases = f"""
  <section class="section" id="case-reviews">
    <div class="container">
      <div class="section-title">
        <span>작업후기</span>
        <h2>서울 폐기물처리 최근 작업후기</h2>
        <p>주기적으로 작업후기를 추가해 실제 현장 사례를 업데이트합니다.</p>
      </div>
      <div class="case-list-grid">
        {''.join(case_card(c, './') for c in cases[:3])}
      </div>
      <div style="text-align:center;margin-top:28px">
        <a class="primary-btn" href="./cases/">작업후기 전체 보기</a>
      </div>
    </div>
  </section>
"""

    backlinks = """
  <section class="section backlink-section" id="family-links">
    <div class="container">
      <div class="section-title">
        <span>가족애 관련 사이트</span>
        <h2>서울·경기 가족애 서비스 바로가기</h2>
        <p>서울과 경기 지역은 유품정리와 폐기물처리 사이트를 구분해 운영합니다.</p>
      </div>
      <div class="backlink-grid">
        <a href="https://www.seoul.gajogae-yupum.com/" target="_blank" rel="noopener">
          <strong>서울 가족애유품정리</strong>
          <span>서울 유품정리 · 고독사청소 상담</span>
        </a>
        <a href="https://www.gyeonggi.gajogae-waste.com/" target="_blank" rel="noopener">
          <strong>경기 가족애폐기물처리</strong>
          <span>경기도 폐기물처리 · 가정폐기물 상담</span>
        </a>
        <a href="https://www.gyeonggi.gajogae-yupum.com/" target="_blank" rel="noopener">
          <strong>경기 가족애유품정리</strong>
          <span>경기도 유품정리 · 특수청소 상담</span>
        </a>
      </div>
    </div>
  </section>
"""

    if 'id="case-reviews"' not in html:
        html = html.replace('<section class="section reviews" id="reviews">', latest_cases + '\n\n  <section class="section reviews" id="reviews">', 1)

    if 'id="family-links"' not in html:
        html = html.replace('<section class="section" id="contact">', backlinks + '\n\n  <section class="section" id="contact">', 1)

    path.write_text(html, encoding="utf-8")

def update_sitemap():
    path = ROOT / "sitemap.xml"
    today = datetime.date.today().isoformat()
    base = path.read_text(encoding="utf-8") if path.exists() else ""

    inserts = [f"{DOMAIN}/cases/"] + [f"{DOMAIN}/cases/{c['slug']}/" for c in cases]

    if "</urlset>" in base:
        for url in inserts:
            if url not in base:
                base = base.replace("</urlset>", f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>""")
        path.write_text(base, encoding="utf-8")

def update_rss():
    path = ROOT / "rss.xml"
    if not path.exists():
        return
    rss = path.read_text(encoding="utf-8")
    for c in cases:
        if f"/cases/{c['slug']}/" not in rss:
            item = f"""
    <item>
      <title>{c['title']}</title>
      <link>{DOMAIN}/cases/{c['slug']}/</link>
      <description>{c['summary']}</description>
    </item>
"""
            rss = rss.replace("</channel>", item + "\n  </channel>")
    path.write_text(rss, encoding="utf-8")

write_css()
build_cases_index()
build_case_pages()
update_index()
update_sitemap()
update_rss()

print("완료: 작업후기 시스템 + 메인 백링크 3개 추가")