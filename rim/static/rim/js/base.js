$(document).ready(function() {
    function set_page_cookie(per_page) {
        var expire_date = new Date();
        //Sets the expire_date to be a year from now
        expire_date.setTime(expire_date.getTime() + (365*24*60*60*1000))
        document.cookie = "paginate=" + per_page +";expires=" + expire_date.toUTCString() +";path=/";
    }

    //Hides the hamburger menu 
    function hide_menu(){
        let equipment_table = document.getElementsByClassName("addform");
        let nav_menu = document.getElementById("nav_menu");
        let style, vw;
        //Quick and dirty solution to collapse the opened menu when equipment_table is clicked (because it occupies the majority of the page)
        equipment_table[0].addEventListener("click", () => {
            vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
            style = getComputedStyle(nav_menu);
            display = style.getPropertyValue('display');
            if(nav_menu.style.display != "none" && vw < 1024)
                nav_menu.style.display = "none";
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
