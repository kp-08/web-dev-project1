var img = document.getElementById('img');

var slides=['static/home_images/10.jpg','static/home_images/23.jpg', 'static/home_images/24.jpg','static/home_images/27.jpg','static/home_images/31.jpg','static/home_images/32.jpg'];

var Start=0;3

function slider(){
    if(Start<slides.length){
        Start=Start+1;
    }
    else{
        Start=1;
    }
    console.log(img);
    img.innerHTML = "<img src="+slides[Start-1]+">";
   
}
setInterval(slider,2500);
