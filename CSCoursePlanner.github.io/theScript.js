
(function()
{
  //drop event to allow the element to be dropped into valid targets
  let count = 0;
  let creditDisplay = document.querySelector('.counter-display')
  let myEle = document.getElementById("spring");
  document.addEventListener('drop', function(e)
  {
    if(myEle){
        console.log("spring")
    }
    else
        console.log("HEREHEHEH")
        count = count + 3;
        updateDisplay();
  
  }, false);

  function updateDisplay(){
    creditDisplay.innerHTML = count;
};
  
  //dragend event to clean-up after drop or abort
  //which fires whether or not the drop target was valid
  

})(); 