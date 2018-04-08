// On click of images
$(".car-img").click(function() {

});
var curY = 0;

var carousel = {
  el:$('#carouselContainer'),
  x:0, y:0, w:100, h:100,
  update:function() {
    l = this.x,
    t = this.y,
    this.el.css({
      'transform':'translate3d('+l+'px, '+t+'px, 0)'
    });
  }
}

setInterval (move,20)

function move() {
  carousel.y = lerp (carousel.y, curY, 0.1);
  carousel.update()
}

function lerp (start, end, amt){
  return (1-amt)*start+amt*end
}

var fullScreenBtn = $("#fullScreenButton")[0];

fullScreenBtn.addEventListener("click", lerpWindow);

function lerpWindow(){
  if (fullscreenFlag == false) {
    curY = -(carousel.el.height() + (carousel.el.height()*0.13));
    $("#header")[0].style.boxShadow = "0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23)";
    map.setOptions({navigationControl:true,scaleControl:true,draggable:true});
    $(".carousel").carousel('pause');
    fullscreenFlag = true;
  } else {
    curY = 0;
    map.setOptions({navigationControl:false,scaleControl:false,draggable:false});
    $(".carousel").carousel('cycle');
    fullscreenFlag = false;
  }
}

document.body.addEventListener("touchmove", function(event) {
    event.preventDefault();
    event.stopPropagation();
}, false);


var body = document.body,
    overlay = document.querySelector('.overlay'),
    overlayBtts = document.querySelectorAll('button[class$="overlay"]');

[].forEach.call(overlayBtts, function(btt) {
  btt.addEventListener('click', function() {
     /* Detect the button class name */
     var overlayOpen = this.className === 'open-overlay';

     /* Toggle the aria-hidden state on the overlay and the
        no-scroll class on the body */
     overlay.setAttribute('aria-hidden', !overlayOpen);
     body.classList.toggle('noscroll', overlayOpen);

     /* On some mobile browser when the overlay was previously
        opened and scrolled, if you open it again it doesn't
        reset its scrollTop property */
     overlay.scrollTop = 0;
  }, false);
});

window.onload = function () {
$('#myCarousel').on('slide.bs.carousel', function () {
  var muralId = parseInt(($('.carousel-item.active')[0].children[0].children[0].id).replace("mural-", ""));
  allMarkers[muralId-1].setIcon(icons['muralUnselected'].icon);
});

// On completion of slide, get id and move map
$('#myCarousel').on('slid.bs.carousel', function () {
  var muralId = parseInt(($('.carousel-item.active')[0].children[0].children[0].id).replace("mural-", ""));
    var center = new google.maps.LatLng(allMuralData[muralId-1][0]+0.001,allMuralData[muralId-1][1]);
    allMarkers[muralId-1].setIcon(icons['muralSelected'].icon);
    map.panTo(center);
});
}
