function displayText(){
  const boxes = document.getElementsByClassName("box");
  for(let box in boxes) {
    box.addEventListener('mouseover', () => {
      var our_story = document.getElementById("our-story");
      our_story.innerHTML = "hi";
    }
    box.addEventListener('mouseout', () => {
     document.getElementById("our-story").innerHTML = "";
                         }
  }
}
