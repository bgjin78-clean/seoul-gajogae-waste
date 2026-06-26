from pathlib import Path

ROOT = Path(__file__).resolve().parent

reviews_html = """
<section class="section reviews" id="reviews">
  <div class="container">
    <div class="section-title">
      <span>고객후기</span>
      <h2>서울 폐기물처리 고객후기</h2>
      <p>서울 각 지역에서 진행된 폐기물 정리 상담 사례를 바탕으로 구성했습니다.</p>
    </div>

    <div class="review-grid">
      <article class="review-card"><div class="review-stars">★★★★★</div><p>이사 후 남은 가구와 생활폐기물이 많았는데 비용 기준을 먼저 안내받아 편했습니다.</p><strong>강남구 고객님</strong></article>
      <article class="review-card"><div class="review-stars">★★★★★</div><p>오래 방치된 짐이 많아 막막했는데 분리부터 반출까지 순서대로 진행해주셔서 좋았습니다.</p><strong>송파구 고객님</strong></article>
      <article class="review-card"><div class="review-stars">★★★★★</div><p>폐업 후 남은 집기와 잡동사니가 많았는데 현장 확인 후 빠르게 정리해주셨습니다.</p><strong>영등포구 고객님</strong></article>
      <article class="review-card"><div class="review-stars">★★★★★</div><p>부모님 집 정리 때문에 문의했는데 필요한 부분만 설명해주셔서 부담이 줄었습니다.</p><strong>마포구 고객님</strong></article>
      <article class="review-card"><div class="review-stars">★★★★★</div><p>대형가구와 생활폐기물을 함께 처리해야 했는데 차량과 인원 안내가 명확했습니다.</p><strong>강서구 고객님</strong></article>
      <article class="review-card"><div class="review-stars">★★★★★</div><p>엘리베이터 사용이 어려운 현장이었는데 작업 순서를 잘 잡아주셔서 무사히 마쳤습니다.</p><strong>노원구 고객님</strong></article>
      <article class="review-card"><div class="review-stars">★★★★★</div><p>사진 상담 후 대략적인 비용을 먼저 알 수 있어서 결정하기 쉬웠습니다.</p><strong>관악구 고객님</strong></article>
      <article class="review-card"><div class="review-stars">★★★★★</div><p>빈집에 남은 잔짐과 폐기물을 한 번에 정리해서 시간이 많이 절약됐습니다.</p><strong>은평구 고객님</strong></article>
    </div>
  </div>
</section>
"""

gallery_html = """
<section class="section gallery-section" id="gallery">
  <div class="container">
    <div class="section-title">
      <span>작업사진</span>
      <h2>폐기물 정리 전·중·후 현장 이미지</h2>
      <p>현장 상황에 따라 분리정리, 반출, 마무리 정돈 순서로 진행합니다.</p>
    </div>

    <h3 class="gallery-subtitle">작업 전</h3>
    <div class="gallery-grid">
      <img src="./images/main/before-01.jpg" alt="서울 폐기물처리 작업 전 사진 1">
      <img src="./images/main/before-05.jpg" alt="서울 폐기물처리 작업 전 사진 2">
      <img src="./images/main/before-09.jpg" alt="서울 폐기물처리 작업 전 사진 3">
      <img src="./images/main/before-13.jpg" alt="서울 폐기물처리 작업 전 사진 4">
      <img src="./images/main/before-17.jpg" alt="서울 폐기물처리 작업 전 사진 5">
      <img src="./images/main/before-21.jpg" alt="서울 폐기물처리 작업 전 사진 6">
      <img src="./images/main/before-25.jpg" alt="서울 폐기물처리 작업 전 사진 7">
      <img src="./images/main/before-29.jpg" alt="서울 폐기물처리 작업 전 사진 8">
    </div>

    <h3 class="gallery-subtitle">작업 중</h3>
    <div class="gallery-grid">
      <img src="./images/main/process-01.jpg" alt="서울 폐기물처리 작업 중 사진 1">
      <img src="./images/main/process-04.jpg" alt="서울 폐기물처리 작업 중 사진 2">
      <img src="./images/main/process-07.jpg" alt="서울 폐기물처리 작업 중 사진 3">
      <img src="./images/main/process-10.jpg" alt="서울 폐기물처리 작업 중 사진 4">
      <img src="./images/main/process-13.jpg" alt="서울 폐기물처리 작업 중 사진 5">
      <img src="./images/main/process-16.jpg" alt="서울 폐기물처리 작업 중 사진 6">
      <img src="./images/main/process-19.jpg" alt="서울 폐기물처리 작업 중 사진 7">
      <img src="./images/main/process-22.jpg" alt="서울 폐기물처리 작업 중 사진 8">
    </div>

    <h3 class="gallery-subtitle">작업 후</h3>
    <div class="gallery-grid">
      <img src="./images/main/after-01.jpg" alt="서울 폐기물처리 작업 후 사진 1">
      <img src="./images/main/after-05.jpg" alt="서울 폐기물처리 작업 후 사진 2">
      <img src="./images/main/after-09.jpg" alt="서울 폐기물처리 작업 후 사진 3">
      <img src="./images/main/after-13.jpg" alt="서울 폐기물처리 작업 후 사진 4">
      <img src="./images/main/after-17.jpg" alt="서울 폐기물처리 작업 후 사진 5">
      <img src="./images/main/after-21.jpg" alt="서울 폐기물처리 작업 후 사진 6">
      <img src="./images/main/after-25.jpg" alt="서울 폐기물처리 작업 후 사진 7">
      <img src="./images/main/after-29.jpg" alt="서울 폐기물처리 작업 후 사진 8">
    </div>
  </div>
</section>
"""

seo_html = """
<section class="section seo-section">
  <div class="container">
    <div class="section-title">
      <span>서울 폐기물처리 안내</span>
      <h2>폐기물 양보다 중요한 것은 현장 동선과 분리 정리입니다</h2>
      <p>같은 양의 폐기물이라도 엘리베이터 유무, 차량 진입, 층수, 작업 인원에 따라 비용과 시간이 달라집니다.</p>
    </div>

    <div class="card-grid">
      <article class="card">
        <h3>아파트·빌라 폐기물</h3>
        <p>서울 주거지역은 주차와 반출 동선이 중요합니다. 관리사무소 반출 시간, 엘리베이터 사용 가능 여부를 함께 확인합니다.</p>
      </article>
      <article class="card">
        <h3>이사 후 남은 폐기물</h3>
        <p>침대, 장롱, 책상, 생활용품처럼 종류가 섞여 있을 때는 먼저 분리정리 후 차량 적재 기준으로 안내합니다.</p>
      </article>
      <article class="card">
        <h3>상가·사무실 폐기물</h3>
        <p>폐업이나 이전 후 남은 집기, 진열대, 의자, 책상 등은 현장 확인 후 필요한 인원과 차량을 산정합니다.</p>
      </article>
    </div>
  </div>
</section>
"""

css_add = """
.gallery-section {
  background: #fff;
}

.gallery-subtitle {
  margin: 38px 0 16px;
  font-size: 24px;
  color: var(--main);
  letter-spacing: -0.03em;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}

.gallery-grid img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: 18px;
  border: 1px solid var(--line);
  box-shadow: 0 10px 22px rgba(66,48,36,.12);
}

.seo-section {
  background: var(--soft2);
}

@media(max-width:900px) {
  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
"""

local_patterns = [
    "후기형 현장 안내: 실제 상담에서는 폐기물 양보다 반출 동선, 엘리베이터 사용 여부, 차량 진입 가능 여부가 비용과 작업 시간에 큰 영향을 줍니다.",
    "사례형 현장 안내: 이사 후 남은 가구, 생활용품, 잔짐이 함께 있는 경우에는 현장에서 먼저 분리한 뒤 차량 적재 기준으로 정리합니다.",
    "정보형 현장 안내: 서울 지역은 주차 공간과 반출 시간이 제한되는 경우가 많아 상담 시 주소와 사진을 함께 확인하는 것이 좋습니다.",
    "가이드형 현장 안내: 폐기물 처리 전에는 대형가구, 생활폐기물, 재활용 가능 품목을 구분하면 작업 시간이 줄고 비용 안내도 더 정확해집니다.",
]

def replace_section(text, start_marker, end_marker, new_html):
    start = text.find(start_marker)
    if start == -1:
        return text
    end = text.find(end_marker, start)
    if end == -1:
        return text
    return text[:start] + new_html + text[end:]

# CSS 추가
css_path = ROOT / "style.css"
css = css_path.read_text(encoding="utf-8")
if ".gallery-grid" not in css:
    css_path.write_text(css + "\n\n" + css_add, encoding="utf-8")

# 메인 index 업그레이드
index_path = ROOT / "index.html"
html = index_path.read_text(encoding="utf-8")

# 기존 후기 섹션 교체
html = replace_section(
    html,
    '<section class="section reviews" id="reviews">',
    '<section class="section areas" id="areas">',
    reviews_html + "\n\n  "
)

# 갤러리 없으면 후기 앞에 삽입
if 'id="gallery"' not in html:
    html = html.replace('<section class="section reviews" id="reviews">', gallery_html + "\n\n  " + '<section class="section reviews" id="reviews">')

# SEO 섹션 없으면 서비스 섹션 앞에 삽입
if 'seo-section' not in html:
    html = html.replace('<section class="section" id="service">', seo_html + "\n\n  " + '<section class="section" id="service">')

index_path.write_text(html, encoding="utf-8")

# 25개 구 페이지 랜덤화
district_dirs = [
    p for p in ROOT.iterdir()
    if p.is_dir() and p.name != "images" and (p / "index.html").exists()
]

for idx, folder in enumerate(sorted(district_dirs)):
    page_path = folder / "index.html"
    page = page_path.read_text(encoding="utf-8")
    pattern = local_patterns[idx % len(local_patterns)]

    # 지역 안내 문단 뒤에 고유 문장 삽입
    if pattern not in page:
        page = page.replace(
            '</p>\n      </div>\n    </div>\n  </section>\n\n  <section class="section" id="service">',
            f'</p><p style="margin-top:14px;color:var(--muted)">{pattern}</p>\n      </div>\n    </div>\n  </section>\n\n  <section class="section" id="service">',
            1
        )

    # 지역 페이지 이미지 경로 보정용 갤러리 삽입
    district_gallery = gallery_html.replace('./images/', '../images/')
    if 'id="gallery"' not in page:
        page = page.replace('<section class="section reviews" id="reviews">', district_gallery + "\n\n  " + '<section class="section reviews" id="reviews">')

    # 후기 8개 교체
    page = replace_section(
        page,
        '<section class="section reviews" id="reviews">',
        '<section class="section areas" id="areas">',
        reviews_html + "\n\n  "
    )

    page_path.write_text(page, encoding="utf-8")

print("완료: 메인페이지 갤러리/후기/SEO 섹션 추가 + 25개 구 페이지 랜덤화 적용")
