//2024-03-13 リファクタリング中
var due_date = new Date('2024');

document.getElementById("loginButton").addEventListener("click",function(){
    alert("修理中");
})

//var trialButton = document.querySelectorAll('.trialButton');

document.querySelectorAll(".trialButton").forEach(function(button) {
    console.log('test');
    button.addEventListener("click", function() {
        var body = document.querySelector("body");
        var opacity = 1.0;

        var fadeOutInterval = setInterval(function(){
            opacity -= 0.001;
            body.style.opacity = opacity;

            if(opacity <= 0) {
                clearInterval(fadeOutInterval);
                opacity = 1.0;
            }
            
        })
    })
})

/////////////////////////////////////////////////////////


// 화살표 버튼 애니메이션
let section = document.querySelectorAll('.section_Y');
let scrollBtn = document.querySelectorAll('.uil-arrow-circle-down_Y');

// 각 섹션 위치 변수저장
let firstTop = section[0].offsetTop;
let secondTop = section[1].offsetTop;
let thirdTop = section[2].offsetTop;
let fourTop = section[3].offsetTop;

// 헤더 불러옴
let menu = document.querySelector('.header_Y');
let scrollTop = window.scrollY;
let menu2 = document.querySelector('.header');

// 라이트바 애니메이션
let right = document.querySelector('#rightBar_Y').children;


// 스크롤 애니메이션
let flag = false;
window.addEventListener('scroll', function () {
    scrollTop = window.scrollY;
    // 스크롤 Y축이 6이상 넘어갈 경우 백그라운드 컬러 표츌
    if (scrollTop > 6) {
        menu.style.background = 'linear-gradient(to bottom, rgba(41, 40, 38, 1), rgba(41,40,38, 0))';
    // 6안쪽으로 들어왔을때 백그라운드 투명
    } else {
        menu.style.background = 'transparent';
    }
});


// 라이트바 1번 박스 클릭 이벤트
right[0].addEventListener('click',function(){
    window.scroll({ top: firstTop, behavior: 'smooth' });
    color(0,1,2,3);
})
// 라이트바 2번 박스 클릭 이벤트
right[1].addEventListener('click',function(){
    window.scroll({ top: secondTop, behavior: 'smooth' });
    color(1,0,2,3);
})
// 라이트바 3번 박스 클릭 이벤트
right[2].addEventListener('click',function(){
    window.scroll({ top: thirdTop, behavior: 'smooth' });
    color(2,0,1,3);
})
// 라이트바 4번 박스 클릭 이벤트
right[3].addEventListener('click',function(){
    window.scroll({ top: fourTop, behavior: 'smooth' });
    color(3,0,1,2);
})

//윈도우 리사이즈 되면 섹션들 위치 다시 계산
window.addEventListener('resize' , function(){
    //최상위 객체 Y축 호출
    scrollTop = window.scrollY;

    firstTop = section[0].offsetTop;
    secondTop = section[1].offsetTop;
    thirdTop = section[2].offsetTop;
    fourTop = section[3].offsetTop;
    console.log(firstTop , secondTop , thirdTop , fourTop);  
})

// 메인페이지 각 섹션 화살표 버튼

// 1번 섹션 클릭시 2번 섹션으로 이동
scrollBtn[0].onclick = function () {
    window.scroll({ top: secondTop, behavior: 'smooth' });
    // 1번 라이트 박스 색상 변경
    color(1,0,2,3);
}

scrollBtn[1].onclick = function () {
    window.scroll({ top: thirdTop, behavior: 'smooth' });
    color(2,0,1,3);
}
scrollBtn[2].onclick = function () {
    window.scroll({ top: fourTop, behavior: 'smooth' });
    color(3,0,1,2);
}
scrollBtn[3].onclick = function () {
    window.scroll({ top: firstTop, behavior: 'smooth' });
    color(0,1,2,3);
}



// right bar BOX 이펙트 함수
// effect에 들어가는 인자값이 이벤트 발생시 효과 발생
function color(effect,ele,ele2,ele3){
    right[effect].style.background='#F9D142';
    right[effect].style.transition='.3s';
    right[ele].style.background='#f9d14261';
    right[ele2].style.background='#f9d14261';
    right[ele3].style.background='#f9d14261';
}


