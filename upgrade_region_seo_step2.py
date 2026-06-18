from pathlib import Path

ROOT = Path(__file__).resolve().parent

district_types = {
    "gangnam": ("강남구", "아파트형", "아파트와 오피스텔, 사무실이 함께 많은 지역입니다. 이사 후 남은 대형가구, 생활폐기물, 사무실 집기 정리 문의가 함께 발생하는 편입니다."),
    "seocho": ("서초구", "아파트형", "아파트 단지와 오피스텔이 많아 이사폐기물과 대형가구 반출 상담이 자주 발생합니다."),
    "songpa": ("송파구", "아파트형", "대단지 아파트와 주거지역이 많아 침대, 장롱, 소파 같은 대형가구 정리 문의가 많은 편입니다."),
    "gangdong": ("강동구", "아파트형", "주거 밀집 지역이 많아 이사 전후 가정폐기물, 대형폐기물 처리 상담이 꾸준합니다."),
    "nowon": ("노원구", "아파트형", "아파트 단지가 많은 지역으로, 이사폐기물과 오래된 생활가구 반출 문의가 자주 있습니다."),

    "mapo": ("마포구", "원룸·오피스텔형", "원룸, 오피스텔, 소형 주거공간이 많아 소형가구와 생활폐기물 정리 문의가 많은 편입니다."),
    "gwanak": ("관악구", "원룸·오피스텔형", "원룸과 다세대 주택이 많아 이사 후 남은 소량 폐기물, 책상, 매트리스 정리 상담이 많습니다."),
    "dongjak": ("동작구", "원룸·오피스텔형", "주거지와 원룸형 건물이 함께 있어 이사폐기물과 생활폐기물 반출 문의가 꾸준합니다."),
    "gwangjin": ("광진구", "원룸·오피스텔형", "오피스텔, 원룸, 상가주택이 섞여 있어 소형폐기물과 가구 정리 상담이 많습니다."),
    "seodaemun": ("서대문구", "원룸·오피스텔형", "다세대 주택과 원룸형 주거지가 많아 생활폐기물, 이사폐기물 문의가 자주 발생합니다."),

    "yeongdeungpo": ("영등포구", "상가·사무실형", "상가, 사무실, 주거지가 함께 있는 지역으로 폐업폐기물과 사무실 집기 정리 상담이 많습니다."),
    "guro": ("구로구", "상가·사무실형", "사무실, 공장형 공간, 상가가 함께 있어 집기류와 잡자재 정리 문의가 발생합니다."),
    "geumcheon": ("금천구", "상가·사무실형", "사무실과 상가, 작업장이 함께 있어 폐업 후 집기류와 폐기물 처리 상담이 많습니다."),
    "jung": ("중구", "상가·사무실형", "도심 상가와 사무실이 많아 폐업폐기물, 집기류, 진열대 정리 문의가 많은 지역입니다."),
    "jongno": ("종로구", "상가·사무실형", "상가, 사무실, 오래된 건물이 많아 반출 동선과 정차 가능 여부 확인이 중요합니다."),

    "yongsan": ("용산구", "도심형", "도심 주거지와 상가가 함께 있어 차량 정차, 골목 진입, 반출 동선 확인이 중요합니다."),
    "seongdong": ("성동구", "도심형", "오피스텔, 상가, 주거지가 섞여 있어 주차 가능 여부와 반출 동선을 먼저 확인하는 것이 좋습니다."),
    "dongdaemun": ("동대문구", "도심형", "시장, 상가, 주거지가 함께 있는 지역이라 작업 전 차량 진입과 정차 시간을 확인해야 합니다."),
    "gangbuk": ("강북구", "도심형", "다세대 주택과 골목형 주거지가 많아 계단 작업과 차량 진입 여부가 중요합니다."),
    "dobong": ("도봉구", "도심형", "주거지와 골목형 건물이 함께 있어 폐기물 양보다 반출 동선이 작업 시간에 영향을 줄 수 있습니다."),

    "gangseo": ("강서구", "주거혼합형", "아파트, 빌라, 상가주택이 함께 있어 가정폐기물과 이사폐기물 상담이 고르게 발생합니다."),
    "yangcheon": ("양천구", "주거혼합형", "아파트와 빌라가 함께 있는 지역으로 대형가구, 생활폐기물, 이사폐기물 문의가 많습니다."),
    "seongbuk": ("성북구", "주거혼합형", "다세대 주택, 아파트, 오래된 주거지가 함께 있어 현장별 작업 조건 차이가 큰 편입니다."),
    "eunpyeong": ("은평구", "주거혼합형", "주거지역이 넓고 빌라와 아파트가 함께 있어 빈집정리와 가정폐기물 문의가 꾸준합니다."),
    "jungnang": ("중랑구", "주거혼합형", "빌라, 다세대 주택, 아파트가 함께 있어 생활폐기물과 이사폐기물 상담이 많습니다."),
}

def make_section(name, type_name, desc):
    return f"""
  <section class="section region-type-section">
    <div class="container">
      <div class="section-title">
        <span>{type_name} 지역 특성</span>
        <h2>{name} 폐기물처리는 현장 구조에 따라 달라집니다</h2>
        <p>{desc}</p>
      </div>

      <div class="type-grid">
        <article class="type-card">
          <h3>{name} 작업 전 확인사항</h3>
          <p>폐기물 양, 대형가구 포함 여부, 층수, 엘리베이터 사용 가능 여부, 차량 진입 가능 여부를 먼저 확인하면 상담이 빠릅니다.</p>
        </article>

        <article class="type-card">
          <h3>{name} 비용 안내</h3>
          <p>기본 비용은 25만원부터이며, 차량 대수와 작업 인원, 반출 동선에 따라 최종 비용이 달라질 수 있습니다.</p>
        </article>

        <article class="type-card">
          <h3>{name} 상담 팁</h3>
          <p>현장 사진을 3~5장 정도 보내주시면 폐기물 양과 작업 범위를 더 정확하게 안내할 수 있습니다.</p>
        </article>
      </div>
    </div>
  </section>
"""

css_add = """
.region-type-section {
  background: #fff;
}

.type-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.type-card {
  background: var(--soft2);
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 24px;
  box-shadow: var(--shadow);
}

.type-card h3 {
  margin: 0 0 10px;
  color: var(--main);
}

.type-card p {
  margin: 0;
  color: var(--muted);
}

@media(max-width:900px) {
  .type-grid {
    grid-template-columns: 1fr;
  }
}
"""

css_path = ROOT / "style.css"
css = css_path.read_text(encoding="utf-8")

if ".region-type-section" not in css:
    css_path.write_text(css + "\n\n" + css_add, encoding="utf-8")

updated = 0

for slug, (name, type_name, desc) in district_types.items():
    path = ROOT / slug / "index.html"

    if not path.exists():
        print(f"건너뜀: {slug}")
        continue

    html = path.read_text(encoding="utf-8")

    if "region-type-section" in html:
        continue

    section = make_section(name, type_name, desc)

    target = '<section class="section local-seo-section">'
    if target in html:
        html = html.replace(target, section + "\n\n  " + target, 1)
    else:
        target = '<section class="section" id="service">'
        html = html.replace(target, section + "\n\n  " + target, 1)

    path.write_text(html, encoding="utf-8")
    updated += 1

print(f"완료: 지역 특성 기반 SEO 2단계 적용 ({updated}개 페이지)")