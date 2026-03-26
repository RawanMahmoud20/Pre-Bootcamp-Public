let likesArray = [9, 12, 9];

function addLike(index) {

    likesArray[index]+=1;

let allCounters = document.querySelectorAll(".likes-counter");
    // تحديث الرقم في الصفحة
    allCounters[index].innerText = likesArray[index];
}