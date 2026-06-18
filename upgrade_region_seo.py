from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

groups = {
    "review": {
        "districts": ["gangnam", "songpa", "seocho", "yongsan", "seongdong"],
        "label": "후기형",
        "paragraph": "최근 {name} 지역에서는 이사 후 남은 가구와 생활용품 정리 문의가 꾸준히 접수되고 있습니다. 폐기물 양보다도 반출 동선, 주차 가능 여부, 엘리베이터 사용 시간이 작업 시간에 더 큰 영향을 주는 경우가 많습니다.",
        "review": "{name} 고객님은 이사 후 남은 침대와 장롱, 생활잡화를 함께 정리해야 하는 상황이었습니다. 사진 상담 후 필요한 차량과 작업 범위를 안내하고 현장 상황에 맞춰 정리했습니다.",
        "faq": [
            ("이사 후 남은 폐기물도 처리 가능한가요?", "가능합니다. 침대, 장롱, 책상, 생활용품처럼 이사 후 남은 품목을 함께 상담할 수 있습니다."),
            ("아파트 폐기물 반출도 가능한가요?", "가능합니다. 엘리베이터 사용 시간과 관리사무소 반출 기준을 확인한 뒤 진행하는 것이 좋습니다."),
            ("사진으로 비용 상담이 가능한가요?", "가능합니다. 폐기물 사진과 주소, 층수 정보를 함께 보내주시면 대략적인 안내가 가능합니다.")
        ],
    },
    "case": {
        "districts": ["mapo", "yeongdeungpo", "gwanak", "guro", "geumcheon"],
        "label": "사례형",
        "paragraph": "{name} 지역은 주거지와 상가, 사무실이 함께 있는 곳이 많아 가정폐기물과 폐업폐기물 문의가 함께 접수되는 편입니다. 현장마다 폐기물 종류가 다르기 때문에 사진 확인 후 차량 규모와 작업 범위를 안내합니다.",
        "review": "{name} 현장에서는 원룸 이사 후 남은 가구와 생활폐기물을 함께 정리했습니다. 좁은 골목 진입 여부를 먼저 확인하고 반출 동선을 정해 작업했습니다.",
        "faq": [
            ("상가 폐업 후 집기도 정리할 수 있나요?", "가능합니다. 의자, 책상, 진열대, 잡자재 등 폐업 후 남은 집기류도 상담할 수 있습니다."),
            ("원룸이나 오피스텔 소량 폐기물도 가능한가요?", "가능합니다. 소량이라도 품목과 위치를 확인한 뒤 방문 가능 여부를 안내합니다."),
            ("차량 진입이 어려운 골목도 가능한가요?", "현장 상황에 따라 가능합니다. 골목 폭과 주차 가능 여부를 먼저 확인하는 것이 좋습니다.")
        ],
    },
    "guide": {
        "districts": ["nowon", "dobong", "gangbuk", "jungnang", "eunpyeong"],
        "label": "가이드형",
        "paragraph": "{name} 폐기물처리를 준비할 때는 버릴 물건과 보관할 물건을 먼저 구분해두면 작업 시간이 줄어듭니다. 대형가구, 생활폐기물, 재활용 가능 품목을 나누어 사진을 보내주시면 상담이 더 정확해집니다.",
        "review": "{name} 고객님은 오래 사용하지 않은 방 안의 가구와 생활용품을 정리해야 했습니다. 보관할 물품을 먼저 확인한 뒤 폐기 대상만 분리해 반출했습니다.",
        "faq": [
            ("폐기물 처리 전에 무엇을 준비해야 하나요?", "버릴 물건과 남겨둘 물건을 구분해두면 작업 시간이 줄어듭니다."),
            ("대형가구는 분해가 필요한가요?", "품목과 현장 동선에 따라 다릅니다. 침대나 장롱처럼 큰 가구는 분해 후 반출하는 경우가 있습니다."),
            ("폐기물 양을 정확히 몰라도 상담 가능한가요?", "가능합니다. 사진을 보내주시면 대략적인 차량 규모와 작업 범위를 안내할 수 있습니다.")
        ],
    },
    "info": {
        "districts": ["dongdaemun", "seongbuk", "seodaemun", "jongno", "jung"],
        "label": "정보형",
        "paragraph": "{name}처럼 도심과 주거지가 함께 있는 지역은 차량 정차 위치와 반출 시간이 중요합니다. 특히 건물 앞 정차가 어려운 경우에는 작업 인원과 이동 거리에 따라 시간이 달라질 수 있습니다.",
        "review": "{name} 현장에서는 건물 앞 정차 시간이 제한되어 폐기물을 먼저 분리한 뒤 짧은 시간 안에 순차적으로 반출했습니다.",
        "faq": [
            ("도심 지역도 폐기물 반출이 가능한가요?", "가능합니다. 다만 주차와 정차 가능 시간을 먼저 확인하는 것이 좋습니다."),
            ("계단 작업도 가능한가요?", "가능합니다. 층수와 폐기물 양에 따라 작업 인원이 달라질 수 있습니다."),
            ("오래된 가구와 생활용품을 함께 정리할 수 있나요?", "가능합니다. 현장 사진을 확인한 뒤 반출 순서를 안내합니다.")
        ],
    },
    "faq": {
        "districts": ["gangseo", "yangcheon", "gwangjin", "dongjak", "gangdong"],
        "label": "FAQ형",
        "paragraph": "{name} 폐기물처리는 품목보다 현장 조건 확인이 중요합니다. 폐기물 양, 층수, 엘리베이터 사용 여부, 차량 진입 가능 여부를 확인하면 비용과 작업 시간을 더 정확하게 안내할 수 있습니다.",
        "review": "{name} 고객님은 가구와 생활폐기물을 함께 처리해야 했고, 사진 상담 후 차량 1대 기준으로 작업 범위를 안내받았습니다.",
        "faq": [
            ("소량 폐기물도 처리 가능한가요?", "가능합니다. 소량이라도 품목, 위치, 방문 가능 시간을 확인한 뒤 상담할 수 있습니다."),
            ("당일 방문 상담이 가능한가요?", "일정에 따라 가능합니다. 주소와 사진을 먼저 보내주시면 빠르게 확인할 수 있습니다."),
            ("가구와 생활폐기물을 함께 처리할 수 있나요?", "가능합니다. 대형가구와 생활폐기물을 함께 분리하고 반출할 수 있습니다.")
        ],
    },
}

district_names = {
    "gangnam": "강남구",
    "gangdong": "강동구",
    "gangbuk": "강북구",
    "gangseo": "강서구",
    "gwanak": "관악구",
    "gwangjin": "광진구",
    "guro": "구로구",
    "geumcheon": "금천구",
    "nowon": "노원구",
    "dobong": "도봉구",
    "dongdaemun": "동대문구",
    "dongjak": "동작구",
    "mapo": "마포구",
    "seodaemun": "서대문구",
    "seocho": "서초구",
    "seongdong": "성동구",
    "seongbuk": "성북구",
    "songpa": "송파구",
    "yangcheon": "양천구",
    "yeongdeungpo": "영등포구",
    "yongsan": "용산구",
    "eunpyeong": "은평구",
    "jongno": "종로구",
    "jung": "중구",
    "jungnang": "중랑구",
}

phone = "010-4720-3895"

def make_extra_section(name, group):
    faq_items = "\n".join(
        f"""
        <div class="local-faq-item">
          <h3>{q}</h3>
          <p>{a}</p>
        </div>
        """
        for q, a in group["faq"]
    )

    return f"""
  <section class="section local-seo-section">
    <div class="container">
      <div class="section-title">
        <span>{name} 지역 SEO 강화</span>
        <h2>{name} 폐기물처리 상담 전 확인할 점</h2>
        <p>{group["paragraph"].format(name=name)}</p>
      </div>

      <div class="local-seo-box">
        <article>
          <strong>{group["label"]}</strong>
          <h3>{name} 폐기물처리 현장 사례</h3>
          <p>{group["review"].format(name=name)}</p>
        </article>

        <article>
          <strong>비용 기준</strong>
          <h3>{name} 폐기물 처리비용 안내</h3>
          <p>기본 비용은 25만원부터이며, 폐기물 양, 차량 대수, 층수, 엘리베이터 사용 여부, 차량 진입 가능 여부에 따라 달라질 수 있습니다. 상담 시 사진을 보내주시면 더 빠르게 안내할 수 있습니다.</p>
        </article>
      </div>

      <div class="local-faq">
        {faq_items}
      </div>
    </div>
  </section>
"""

css_add = """
.local-seo-section {
  background: #fffaf4;
}

.local-seo-box {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 24px;
}

.local-seo-box article {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 26px;
  box-shadow: var(--shadow);
}

.local-seo-box strong {
  display: inline-flex;
  background: #f3e1cc;
  color: var(--main);
  border-radius: 999px;
  padding: 7px 13px;
  font-size: 14px;
  font-weight: 900;
  margin-bottom: 12px;
}

.local-seo-box h3 {
  margin: 0 0 10px;
  color: var(--main);
}

.local-seo-box p {
  margin: 0;
  color: var(--muted);
}

.local-faq {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.local-faq-item {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 22px;
}

.local-faq-item h3 {
  margin: 0 0 8px;
  color: var(--main);
  font-size: 18px;
}

.local-faq-item p {
  margin: 0;
  color: var(--muted);
}

@media(max-width:900px) {
  .local-seo-box,
  .local-faq {
    grid-template-columns: 1fr;
  }
}
"""

# CSS 추가
css_path = ROOT / "style.css"
css = css_path.read_text(encoding="utf-8")
if ".local-seo-section" not in css:
    css_path.write_text(css + "\n\n" + css_add, encoding="utf-8")

# slug -> group 매핑
slug_to_group = {}
for group in groups.values():
    for slug in group["districts"]:
        slug_to_group[slug] = group

updated = 0

for slug, name in district_names.items():
    page_path = ROOT / slug / "index.html"
    if not page_path.exists():
        print(f"건너뜀: {slug}/index.html 없음")
        continue

    html = page_path.read_text(encoding="utf-8")
    group = slug_to_group.get(slug)

    if not group:
        print(f"건너뜀: {slug} 그룹 없음")
        continue

    # 메타디스크립션 강화
    new_desc = f"{name} 폐기물처리 비용 25만원부터. 가정폐기물, 이사폐기물, 빈집정리, 폐업폐기물, 쓰레기집청소 상담. {name} 현장 사진 상담 가능 {phone}."
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{new_desc}">',
        html,
        count=1
    )

    # 제목 약간 강화
    html = re.sub(
        r"<title>.*?</title>",
        f"<title>{name} 폐기물처리 비용 25만원부터 | 가정·이사폐기물 상담</title>",
        html,
        count=1
    )

    # 기존 local seo 섹션 제거 후 재삽입 방지
    if 'local-seo-section' not in html:
        insert_html = make_extra_section(name, group)

        # 서비스 섹션 앞에 삽입
        target = '<section class="section" id="service">'
        if target in html:
            html = html.replace(target, insert_html + "\n\n  " + target, 1)
        else:
            print(f"주의: {slug} 서비스 섹션 위치 못 찾음")
            continue

    page_path.write_text(html, encoding="utf-8")
    updated += 1

print(f"완료: 서울 25개 구 지역 SEO 강화 적용 ({updated}개 페이지)")