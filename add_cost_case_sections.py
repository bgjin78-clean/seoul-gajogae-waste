from pathlib import Path

ROOT = Path(__file__).resolve().parent
index_path = ROOT / "index.html"
css_path = ROOT / "style.css"

cost_case_html = """
<section class="section cost-factor-section" id="cost-factor">
  <div class="container">
    <div class="section-title">
      <span>비용 기준</span>
      <h2>서울 폐기물처리 비용에 영향을 주는 요소</h2>
      <p>기본 비용은 25만원부터이며, 현장 조건에 따라 최종 비용이 달라질 수 있습니다.</p>
    </div>

    <div class="factor-grid">
      <article class="factor-card">
        <strong>01</strong>
        <h3>폐기물 양</h3>
        <p>1톤 차량 1대 분량인지, 2대 이상인지에 따라 비용 차이가 발생합니다.</p>
      </article>

      <article class="factor-card">
        <strong>02</strong>
        <h3>층수와 엘리베이터</h3>
        <p>고층 건물, 계단 작업, 엘리베이터 사용 제한 여부에 따라 작업 인원이 달라질 수 있습니다.</p>
      </article>

      <article class="factor-card">
        <strong>03</strong>
        <h3>대형가구 포함 여부</h3>
        <p>침대, 장롱, 소파, 책상처럼 부피가 큰 품목은 분해와 반출 시간이 더 필요할 수 있습니다.</p>
      </article>

      <article class="factor-card">
        <strong>04</strong>
        <h3>차량 진입 가능 여부</h3>
        <p>주차 공간, 골목 진입, 건물 앞 정차 가능 여부에 따라 작업 시간이 달라질 수 있습니다.</p>
      </article>
    </div>
  </div>
</section>

<section class="section case-section" id="cases">
  <div class="container">
    <div class="section-title">
      <span>작업사례</span>
      <h2>서울 폐기물처리 실제 작업사례</h2>
      <p>가정폐기물, 이사폐기물, 빈집정리, 폐업폐기물까지 현장 상황에 맞춰 진행합니다.</p>
    </div>

    <div class="case-grid">
      <article class="case-card">
        <div class="case-label">가정폐기물</div>
        <h3>서울 강남구 아파트 폐기물 정리</h3>
        <p>이사 후 남은 침대, 장롱, 책상, 생활잡화를 정리한 사례입니다. 엘리베이터 사용 가능 시간을 확인한 뒤 반출 순서를 정해 진행했습니다.</p>
        <ul>
          <li>작업시간: 약 3시간</li>
          <li>차량: 1톤 차량 1대</li>
          <li>품목: 침대, 장롱, 책상, 생활잡화</li>
        </ul>
      </article>

      <article class="case-card">
        <div class="case-label">빈집정리</div>
        <h3>서울 마포구 빌라 빈집 정리</h3>
        <p>오래 비어 있던 주거공간에 남은 가구와 생활폐기물을 분리한 뒤 순차적으로 반출했습니다.</p>
        <ul>
          <li>작업시간: 약 4시간</li>
          <li>차량: 1톤 차량 2대</li>
          <li>품목: 생활폐기물, 가구류, 잔짐</li>
        </ul>
      </article>

      <article class="case-card">
        <div class="case-label">폐업폐기물</div>
        <h3>서울 영등포구 상가 집기 정리</h3>
        <p>폐업 후 남은 의자, 책상, 진열대, 잡자재를 정리한 사례입니다. 상가 앞 정차 시간을 고려해 반출 동선을 먼저 확인했습니다.</p>
        <ul>
          <li>작업시간: 약 5시간</li>
          <li>차량: 1톤 차량 2대</li>
          <li>품목: 의자, 책상, 진열대, 잡자재</li>
        </ul>
      </article>
    </div>
  </div>
</section>
"""

css_add = """
.cost-factor-section {
  background: #fff;
}

.factor-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.factor-card {
  background: var(--soft2);
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 26px;
  box-shadow: var(--shadow);
}

.factor-card strong {
  display: inline-flex;
  width: 46px;
  height: 46px;
  align-items: center;
  justify-content: center;
  background: var(--main);
  color: #fff;
  border-radius: 50%;
  font-weight: 950;
  margin-bottom: 14px;
}

.factor-card h3 {
  margin: 0 0 10px;
  color: var(--main);
  font-size: 21px;
}

.factor-card p {
  margin: 0;
  color: var(--muted);
}

.case-section {
  background: var(--soft);
}

.case-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}

.case-card {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 26px;
  padding: 28px;
  box-shadow: var(--shadow);
}

.case-label {
  display: inline-flex;
  background: #f3e1cc;
  color: var(--main);
  border-radius: 999px;
  padding: 7px 13px;
  font-size: 14px;
  font-weight: 900;
  margin-bottom: 14px;
}

.case-card h3 {
  margin: 0 0 12px;
  color: var(--main);
  font-size: 22px;
}

.case-card p {
  color: var(--muted);
}

.case-card ul {
  margin: 18px 0 0;
  padding: 0;
  list-style: none;
}

.case-card li {
  padding: 7px 0 7px 24px;
  position: relative;
  color: var(--muted);
}

.case-card li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: 900;
}

@media(max-width:900px) {
  .factor-grid,
  .case-grid {
    grid-template-columns: 1fr;
  }
}
"""

html = index_path.read_text(encoding="utf-8")

if 'id="cost-factor"' not in html:
    html = html.replace(
        '<section class="section">\n    <div class="container">\n      <div class="section-title">\n        <span>진행 과정</span>',
        cost_case_html + '\n\n  <section class="section">\n    <div class="container">\n      <div class="section-title">\n        <span>진행 과정</span>'
    )

index_path.write_text(html, encoding="utf-8")

css = css_path.read_text(encoding="utf-8")

if ".cost-factor-section" not in css:
    css_path.write_text(css + "\n\n" + css_add, encoding="utf-8")

print("완료: 비용 영향 요소 + 실제 작업사례 섹션 추가")