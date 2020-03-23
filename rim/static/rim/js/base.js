$(document).ready(function() {
    function set_page_cookie(per_page) {
        var expire_date = new Date();
        //Sets the expire_date to be a year from now
        expire_date.setTime(expire_date.getTime() + (365*24*60*60*1000))
        document.cookie = "paginate=" + per_page +";expires=" + expire_date.toUTCString() +";path=/";
    }
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
  
    $('#paginate_form').submit(function(e) {
        e.preventDefault();
        set_page_cookie($('#page_input').val());
        var searchParam = new URLSearchParams(window.location.search);
        if (searchParam.has('page')) {
            searchParam.delete('page');
            window.location.search = '?' + searchParam.toString();
        }
        else {
            window.location.reload();
        }
    })
    
    hide_menu();
    $(document).foundation();

});
