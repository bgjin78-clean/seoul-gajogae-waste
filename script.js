// EmailJS 설정
// 1) EmailJS 대시보드에서 Public Key, Service ID, Template ID를 확인
// 2) 아래 값을 본인 계정 값으로 변경
const EMAILJS_PUBLIC_KEY = "JKsVOKPtnWHIr2BCV";
const EMAILJS_SERVICE_ID = "gyeonggi-gajogae-yupum";
const EMAILJS_TEMPLATE_ID = "template_wwbariw";

(function(){
  if (typeof emailjs !== "undefined" && EMAILJS_PUBLIC_KEY !== "YOUR_PUBLIC_KEY") {
    emailjs.init(EMAILJS_PUBLIC_KEY);
  }
})();

document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll(".consult-form");

  forms.forEach((form) => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const message = form.querySelector(".form-message");
      const agree = form.querySelector('input[name="agree"]');
      const button = form.querySelector('button[type="submit"]');

      if (!agree || !agree.checked) {
        message.textContent = "개인정보 수집 및 이용에 동의해 주세요.";
        message.style.color = "#b13b2e";
        return;
      }

      const data = {
        title: "[서울 가족애폐기물처리]",
        site_name: "가족애폐기물처리 서울",
        page_title: "서울 폐기물처리",
        name: form.name.value.trim(),
        phone: form.phone.value.trim(),
        region: form.region.value.trim(),
        service: form.service.value,
        message:
          "[가족애폐기물처리 서울 상담접수]\n\n" +
          "이름: " + form.name.value.trim() + "\n" +
          "연락처: " + form.phone.value.trim() + "\n" +
          "주소: " + form.region.value.trim() + "\n" +
          "서비스: " + form.service.value + "\n" +
          "페이지: " + "서울 폐기물처리\n" +
          "접수시간: " + new Date().toLocaleString("ko-KR") + "\n\n" +
          "문의내용:\n" +
          form.message.value.trim(),
        submitted_at: new Date().toLocaleString("ko-KR")
    };

      if (!data.name || !data.phone || !data.region) {
        message.textContent = "이름, 연락처, 주소를 입력해 주세요.";
        message.style.color = "#b13b2e";
        return;
      }

      button.disabled = true;
      button.textContent = "접수 중입니다...";
      message.textContent = "";

      try {
        if (typeof emailjs === "undefined" || EMAILJS_PUBLIC_KEY === "YOUR_PUBLIC_KEY") {
          console.log("EmailJS 미설정 상태 - 전송 데이터:", data);
          message.textContent = "상담 접수 테스트 완료. EmailJS 값을 넣으면 실제 메일이 발송됩니다.";
          message.style.color = "#2c6b3f";
          form.reset();
        } else {
          await emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, data);
          message.textContent = "상담 접수가 완료되었습니다. 확인 후 연락드리겠습니다.";
          message.style.color = "#2c6b3f";
          form.reset();
        }
      } catch (err) {
        console.error(err);
        message.textContent = "접수 중 오류가 발생했습니다. 전화 상담을 이용해 주세요.";
        message.style.color = "#b13b2e";
      } finally {
        button.disabled = false;
        button.textContent = "상담 접수하기";
      }
    });
  });
});