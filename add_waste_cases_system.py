from pathlib import Path
import datetime

ROOT = Path(__file__).resolve().parent
DOMAIN = "https://www.seoul.gajogae-waste.com"
PHONE = "010-4720-3895"
BRAND = "가족애폐기물처리"

# 여기만 수정하면 작업후기 관리 가능
# 번호는 images/cases/waste-before-001.jpg, waste-after-001.jpg 와 자동 연결됨
case_titles = [
    ("001", "강남구 가정폐기물 처리 사례", "서울 강남구", "가정폐기물처리", "이사 후 남은 침대, 장롱, 책상, 생활잡화를 정리한 사례입니다."),
    ("002", "마포구 원룸 이사폐기물 정리 사례", "서울 마포구", "이사폐기물처리", "원룸 이사 후 남은 매트리스, 소형가구, 생활폐기물을 정리한 사례입니다."),
    ("003", "영등포구 폐업폐기물 처리 사례", "서울 영등포구", "폐업폐기물처리", "상가 폐업 후 남은 의자, 책상, 진열대, 잡자재를 정리한 사례입니다."),
    ("004", "송파구 대형가구 폐기물 처리 사례", "서울 송파구", "가정폐기물처리", "침대, 소파, 장롱 등 대형가구 중심으로 정리한 사례입니다."),
    ("005", "은평구 빈집정리 폐기물 처리 사례", "서울 은평구", "빈집정리", "오래 비어 있던 주거공간의 생활폐기물과 잔짐을 정리한 사례입니다."),
    ("006", "관악구 생활폐기물 정리 사례", "서울 관악구", "생활폐기물처리", "생활용품, 소형가구, 잡동사니를 분리 정리한 사례입니다."),
]

CSS_ADD = """
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

.case-list-card h3 {
  color: var(--main);
  margin: 0 0 10px;
}

.case-list-card p {
  color: var(--muted);
}

.case-detail-images {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.case-detail-images figure {
  margin: 0;
}

.case-detail-images img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: 20px;
  border: 1px solid var(--line);
}

.case-detail-images figcaption {
  margin-top: 8px;
  text-align: center;
  color: var(--muted);
  font-weight: 800;
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

def add_css():
    css_path = ROOT / "style.css"
    css = css_path.read_text(encoding="utf-8")
    if ".case-list-grid" not in css:
        css_path.write_text(css + "\n\n" + CSS_ADD, encoding="utf-8")

def case_data():
    data = []
    for num, title, region, service, summary in case_titles:
        data.append({
            "num": num,
            "slug": f"case-{num}",
            "title": title,
            "region": region,
            "service": service,
            "summary": summary,
            "before": f"waste-before-{num}.jpg",
            "after": f"waste-after-{num}.jpg",
        })
    return data

def case_card(c, prefix):
    return f"""
    <article class="case-list-card">
      <img src="{prefix}images/cases/{c['after']}" alt="{c['title']} 작업 후 사진">
      <div>
        <span>{c['region']}</span>
        <h3>{c['title']}</h3>
        <p>{c['summary']}</p>
        <a class="primary-btn" href="{prefix}cases/{c['slug']}/">후기 자세히 보기</a>
      </div>
    </article>
"""

def build_cases_index(cases):
    cases_dir = ROOT / "cases"
    cases_dir.mkdir(exist_ok=True)

    cards = "\n".join(case_card(c, "../") for c in cases)

    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>서울 폐기물처리 작업후기 | {BRAND}</title>
  <meta name="description" content="서울 가족애폐기물처리 작업후기 모음. 가정폐기물, 이사폐기물, 빈집정리, 폐업폐기물 처리 사례를 확인하세요.">
  <link rel="canonical" href="{DOMAIN}/cases/">
  <link rel="icon" href="../images/main/favicon.png">
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header class="header">
    <div class="container nav">
      <a class="logo" href="../index.html">{BRAND}<small>서울 폐기물처리 작업후기</small></a>
      <a class="call-btn" href="tel:{PHONE}">{PHONE}</a>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="section-title">
        <span>작업후기</span>
        <h1>서울 폐기물처리 작업후기</h1>
        <p>실제 현장 상황을 바탕으로 정리한 가정폐기물, 이사폐기물, 빈집정리, 폐업폐기물 처리 사례입니다.</p>
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

def build_case_pages(cases):
    for c in cases:
        d = ROOT / "cases" / c["slug"]
        d.mkdir(parents=True, exist_ok=True)

        html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{c['title']} | 서울 {BRAND}</title>
  <meta name="description" content="{c['region']} {c['service']} 작업후기. {c['summary']} 상담전화 {PHONE}.">
  <link rel="canonical" href="{DOMAIN}/cases/{c['slug']}/">
  <link rel="icon" href="../../images/main/favicon.png">
  <link rel="stylesheet" href="../../style.css">
</head>
<body>
  <header class="header">
    <div class="container nav">
      <a class="logo" href="../../index.html">{BRAND}<small>{c['region']} 작업후기</small></a>
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
        <figure>
          <img src="../../images/cases/{c['before']}" alt="{c['title']} 작업 전">
          <figcaption>작업 전</figcaption>
        </figure>
        <figure>
          <img src="../../images/cases/{c['after']}" alt="{c['title']} 작업 후">
          <figcaption>작업 후</figcaption>
        </figure>
      </div>

      <section class="section">
        <div class="cost-box">
          <div>
            <h2>{c['region']} 현장 정리 내용</h2>
            <p>{c['summary']} 폐기물 양과 반출 동선을 확인한 뒤 필요한 범위만 안내하고 작업을 진행했습니다.</p>
          </div>
          <ul class="check-list">
            <li>지역: {c['region']}</li>
            <li>서비스: {c['service']}</li>
            <li>사진 기준: 전·후 비교</li>
            <li>상담전화: {PHONE}</li>
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

def update_index(cases):
    index_path = ROOT / "index.html"
    html = index_path.read_text(encoding="utf-8")

    latest = cases[:6]

    latest_html = f"""
  <section class="section" id="case-reviews">
    <div class="container">
      <div class="section-title">
        <span>작업후기</span>
        <h2>서울 폐기물처리 최근 작업후기</h2>
        <p>작업후기는 지속적으로 추가되며 실제 현장 사례를 바탕으로 구성합니다.</p>
      </div>

      <div class="case-list-grid">
        {''.join(case_card(c, './') for c in latest)}
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
        html = html.replace('<section class="section reviews" id="reviews">', latest_html + '\n\n  <section class="section reviews" id="reviews">', 1)

    if 'id="family-links"' not in html:
        html = html.replace('<section class="section" id="contact">', backlinks + '\n\n  <section class="section" id="contact">', 1)

    index_path.write_text(html, encoding="utf-8")

def update_sitemap(cases):
    path = ROOT / "sitemap.xml"
    today = datetime.date.today().isoformat()

    if not path.exists():
        return

    sitemap = path.read_text(encoding="utf-8")
    urls = [f"{DOMAIN}/cases/"] + [f"{DOMAIN}/cases/{c['slug']}/" for c in cases]

    for url in urls:
        if url not in sitemap:
            block = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""
            sitemap = sitemap.replace("</urlset>", block + "</urlset>")

    path.write_text(sitemap, encoding="utf-8")

def update_rss(cases):
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

cases = case_data()

add_css()
build_cases_index(cases)
build_case_pages(cases)
update_index(cases)
update_sitemap(cases)
update_rss(cases)

print(f"완료: 작업후기 {len(cases)}개 생성 + 메인 최신후기 + 백링크 추가")