window.addEventListener("DOMContentLoaded", function () {
  console.log("betöltött");
  let h1 = this.document.getElementById("demo");
  h1.addEventListener("click", () => {
    h1.textContent = "Maci";
  });
});
window.addEventListener("load", init);
kepek = [
    {
        cim: "01-es kép",
        eleresiut:"/2022.09.24/képek/photo-1588167056840-13caf6e4562a.webp",
        leírás:"Ez a első kép",
    },
    {
        cim: "02-es kép",
        eleresiut:"./2022.09.24/képek/julien-riedel-xkgyg8jYmvw-unsplash.jpg",
        leírás:"Ez a második cicás kép",
    },
    {
        cim: "03-es kép",
        eleresiut:"./2022.09.24/képek/istockphoto-962287090-612x612.jpg",
        leírás:"Ez a harmadik  kép",
    }
]
function ID(elem){
    return document.getElementById(elem);
}
function init(){
    kiirKepek()
}
function kiirKepek(){
    var txt = " ";
    for (let i = 0; i < kepek.length; i++) {
        txt = txt + "<div>" + "<h3>"+ kepek[i].cim +"</h3>" + "<img src='"+ kepek[i].eleresiut+ "' class='kepek' alt='cicás képek'/>"+
        "<p>"+kepek[i].leírás+"</p> </div>"
    }
    ID("galeria").innerHTML = txt;
}