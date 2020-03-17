$(document).ready(function() {
    
    function set_page_cookie(per_page) {
        var expire_date = new Date();
        //Sets the expire_date to be a year from now
        expire_date.setTime(expire_date.getTime() + (365*24*60*60*1000))
        document.cookie = "paginate=" + per_page +";expires=" + expire_date.toUTCString() +";path=/";
    }

    function set_search_fields() {

        let small_display_search_fields = document.getElementById("small_screen_search_fields");
        let dropdown_button = document.getElementById("search_fields_button");
        let style, display, button_text;

        dropdown_button.addEventListener("click", () => {
            style = getComputedStyle(small_display_search_fields);
            display = style.getPropertyValue('display');
            button_text = dropdown_button.innerText;

            if(display != "none")
                small_display_search_fields.style.display = "none";
            else
                small_display_search_fields.style.display = "initial";
            
            if(button_text == "More Options")
                dropdown_button.innerText = "Less Options"
            else
                dropdown_button.innerText = "More Options"
          });  
    }

    function hide_menu(){
        let equipment_table = document.getElementsByClassName("equipment-table");
        let nav_menu = document.getElementById("nav_menu");
        let style, display;

        equipment_table[0].addEventListener("click", () => {
            style = getComputedStyle(nav_menu);
            display = style.getPropertyValue('display');
            if(nav_menu.style.display != "none" && Foundation.MediaQuery.current < Foundation.MediaQuery.get('large'))
                nav_menu.style.display = "none";
        })
    }

    function handle_orientation_changes(){
        const LARGE = 1024;
        let small_display_search_fields;
        let dropdown_button, style, width ;

        window.addEventListener("resize", () => {
            dropdown_button_bar = document.getElementById("search_fields_toggle_bar");
            dropdown_button = document.getElementById("search_fields_button");
            button_text = dropdown_button.innerText;
            small_display_search_fields = document.getElementById("small_screen_search_fields");
            style = getComputedStyle(nav_menu);
            display = style.getPropertyValue('display');
            width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0)
            console.log(document.documentElement.clientWidth, document.documentElement.clientHeight, window.innerWidth, window.innerHeight )
            if(Foundation.MediaQuery.current < Foundation.MediaQuery.get('large')){
                dropdown_button_bar.style.display = ""
                small_display_search_fields.style.display = ""
                console.log("window is ", Foundation.MediaQuery.current)
            }
            else if(Foundation.MediaQuery.atLeast('large')) {
                small_display_search_fields.style.display = "none"
                dropdown_button_bar.style.display = "none"
                
                if(button_text == "Less Options")
                    dropdown_button.innerText = "More Options"
                console.log("(at least large)window is ", Foundation.MediaQuery.current)
            }
        });
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
    
    set_search_fields();
    hide_menu();
    handle_orientation_changes();
    $(document).foundation();


});
