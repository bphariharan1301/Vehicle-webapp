var hamburger = document.querySelector(".hamburger");
hamburger.addEventListener("click", function(){
    document.querySelector("body").classList.toggle("active");
})


const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// setTimeout(function() {
//   $('#message').fadeOut('fast');
// }, 3000);

var close = document.getElementsByClassName("close");
close.onclick = function () {
  var div = this.parentElement;
  div.style.opacity = "0";
  setTimeout(function(){ div.style.display = "none"; }, 600);
}


