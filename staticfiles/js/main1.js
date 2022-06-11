
  //   $(function() {
  //     // this will get the full URL at the address bar
  //     var url = window.location.href;

  //     // passes on every "a" tag
  //     $(".topmenu a").each(function() {
  //         // checks if its the same on the address bar
  //         if (url == (this.href)) {
  //             $(this).closest("li").addClass("active");
  //             //for making parent of submenu active
  //            $(this).closest("li").parent().parent().addClass("active");
  //         }
  //     });
  // });

/*====================================================
                        NAVIGATION
====================================================*/
// Show/Hide transparent black navigation
$(function () {

  $(window).scroll(function () {

      if ($(this).scrollTop() < 5000) {
          // hide nav
          $("nav").removeClass("default-header");
          $("#back-to-top").fadeOut();

      } else {
          // show nav
          $("nav").addClass("default-header");
          $("#back-to-top").fadeIn();
      }
  });
});





function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}

function myFunction1() {
    var dots1 = document.getElementById("dots1");
    var moreText1 = document.getElementById("more1");
    var btnText1 = document.getElementById("myBtn1");
  
    if (dots1.style.display === "none") {
      dots1.style.display = "inline";
      btnText1.innerHTML = "Read more"; 
      moreText1.style.display = "none";
    } else {
      dots1.style.display = "none";
      btnText1.innerHTML = "Read less"; 
      moreText1.style.display = "inline";
    }
  }

  function myFunction2() {
    var dots2 = document.getElementById("dots2");
    var moreText2 = document.getElementById("more2");
    var btnText2 = document.getElementById("myBtn2");
  
    if (dots2.style.display === "none") {
      dots2.style.display = "inline";
      btnText2.innerHTML = "Read more"; 
      moreText2.style.display = "none";
    } else {
      dots2.style.display = "none";
      btnText2.innerHTML = "Read less"; 
      moreText2.style.display = "inline";
    }
  }


  /*====================================================
                        TEAM
====================================================*/
$(function () {

    $("#team-members").owlCarousel({
        items: 3,
        autoplay: true,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
		responsive: {
		  0: {
			items: 1
		  },
		  480: {
			items: 2
		  },
		  768: {
			items: 3
		  }
		}
    });
});

// hovering
// $('h4.team-member-name').on('mouseenter', function(){
//   $(this).toggleClass('h4.team-member-name1')
// })

  
