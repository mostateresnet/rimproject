$(document).ready(function() {
  //Hides the hamburger menu 
    function hide_menu(){
        let topnav = document.getElementById("topnav");
        let style, vw;
        //Quick and dirty solution to collapse the opened menu when anything is clicked outside of the nav_menu
        document.addEventListener("click", (event) => {
            let topnav_clicked = topnav.contains(event.target)
            if(!topnav_clicked){
                vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
                style = getComputedStyle(nav_menu);
                display = style.getPropertyValue('display');
                
                if(nav_menu.style.display != "none" && vw < 1024)
                    nav_menu.style.display = "none";
            }
        })
    }

    hide_menu();
})