let images = document.querySelectorAll('img');


images.forEach((image)=>{
    console.log(image);
    let img_link = image.src;
    image.src = img_link;
})