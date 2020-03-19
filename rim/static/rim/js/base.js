$(document).ready(function() {
    
    function set_page_cookie(per_page) {
        var expire_date = new Date();
        //Sets the expire_date to be a year from now
        expire_date.setTime(expire_date.getTime() + (365*24*60*60*1000))
        document.cookie = "paginate=" + per_page +";expires=" + expire_date.toUTCString() +";path=/";
    }

    //Destroys the hostname/client name search fields(small_screen_search_fields) if the dropdown menu "More Options" is clicked to avoid 
    //duplicate values in the GET JSON string
    function set_search_fields() {
        //Obtain the elements we need
        let vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
        let search_fields_dropdown_state = false;
        let small_display_search_fields = document.getElementById("small_screen_search_fields");
        dropdown_button_bar = document.getElementById("search_fields_toggle_bar");
        let search_field_values = document.getElementsByTagName("input");
        let small_display_search_fields_parent_element = small_display_search_fields.parentElement;
        let dropdown_button = document.getElementById("search_fields_button");
        let style, button_text;

        if(small_display_search_fields != null && vw >= 1024){
            small_display_search_fields_parent_element.removeChild(small_display_search_fields);
            console.log(vw, "outside if")
        }
        //If "More Options" is clicked
        dropdown_button.addEventListener("click", () => {
            Array.from(search_field_values).forEach(element => {
                element.value = "";
            });
            vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
            search_fields_dropdown_state ? search_fields_dropdown_state = false : search_fields_dropdown_state = true;
            button_text = dropdown_button.innerText;
            //debug
            console.log(search_fields_dropdown_state)
            //If "More Options" is clicked and small_screen_search_fields element exists -> destroy it
            if(document.getElementById("small_screen_search_fields") != null && search_fields_dropdown_state) {
                console.log(vw, search_fields_dropdown_state, "if")
                small_display_search_fields_parent_element.removeChild(small_display_search_fields);
            }
            //If small_screen_search_fields display is "none" and the user clicked "Less Options" button to collapse the search fields -> show it again
            else if(document.getElementById("small_screen_search_fields") == null ){
                small_display_search_fields_parent_element.insertBefore(small_display_search_fields, dropdown_button_bar)
                console.log(vw, "else if")
            }
               
            //Handles the dropdown button text depending on the current state of the button 
            if(button_text == "More Options")
                dropdown_button.innerText = "Less Options"
            else
                dropdown_button.innerText = "More Options"
          });  
          
          window.addEventListener("resize", () =>{
            vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
            button_text = dropdown_button.innerText;
            if(vw >= 1024)
                search_fields_dropdown_state = false
            console.log(button_text)
            if(document.getElementById("small_screen_search_fields") != null && vw >= 1024) {
                console.log(vw, search_fields_dropdown_state, "resize if")
                small_display_search_fields_parent_element.removeChild(small_display_search_fields);
            }
            else if(document.getElementById("small_screen_search_fields") == null && vw < 1024 && !search_fields_dropdown_state){
                small_display_search_fields_parent_element.insertBefore(small_display_search_fields, dropdown_button_bar)
                console.log(vw,search_fields_dropdown_state, "else if")
            }
            
            dropdown_button.innerText = "More Options"
          })
    }
   

    // function handle_orientation_changes(){
    //     let small_display_search_fields, dropdown_button, vw;
    //      //PROBABLY COMBINE WITH set_search_fields FOR CODE EFFICIENCY
    //     window.addEventListener("resize", () => {
    //         vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    //         dropdown_button_bar = document.getElementById("search_fields_toggle_bar");
    //         dropdown_button = document.getElementById("search_fields_button");
    //         button_text = dropdown_button.innerText;
    //         small_display_search_fields = document.getElementById("small_screen_search_fields");
    //         console.log(document.documentElement.clientWidth, document.documentElement.clientHeight, window.innerWidth, window.innerHeight )
    //         if(vw < 1024){
    //             dropdown_button_bar.style.display = ""
                
    //             if(button_text == "Less Options")
    //                 dropdown_button.innerText = "More Options"
    //             console.log("window is ", Foundation.MediaQuery.current)
    //         }
    //         else if(vw >= 1024) {
               
    //             dropdown_button_bar.style.display = "none"
                
                
    //             console.log("(at least large)window is ", Foundation.MediaQuery.current)
    //         }
    //     });
    // }

     //Hides the hamburger menu 
     function hide_menu(){
        let equipment_table = document.getElementsByClassName("equipment-table");
        let nav_menu = document.getElementById("nav_menu");
        let style, vw;

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
    
    set_search_fields();
    hide_menu();
   // handle_orientation_changes();
    $(document).foundation();


});
