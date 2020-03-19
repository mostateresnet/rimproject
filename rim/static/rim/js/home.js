$(document).ready(function() {

    function set_search_fields() {
        //Obtain the elements we need
        let vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
        let search_fields_dropdown_state = false;
        let small_display_search_fields = document.getElementById("small_screen_search_fields");
        let search_fields = document.getElementById("search_fields")
        let dropdown_button_bar = document.getElementById("search_fields_toggle_bar");
        let search_field_values = document.getElementsByTagName("input");
        let small_display_search_fields_parent_element = small_display_search_fields.parentElement;
        let dropdown_button = document.getElementById("search_fields_button");
        let button_text;

        //Destroy small_display_search_fields if the viewport is LARGE(1024)+
        if(small_display_search_fields != null && vw >= 1024){
            small_display_search_fields_parent_element.removeChild(small_display_search_fields);
        }
        //If "More Options" is clicked
        dropdown_button.addEventListener("click", () => {
            //Set all fields to empty
            Array.from(search_field_values).forEach(element => {
                element.value = "";
            });
            vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
            //Depending on the dropdown state(expanded/collapsed) set to opposite value on click event
            search_fields_dropdown_state ? search_fields_dropdown_state = false : search_fields_dropdown_state = true;
            //Get the current dropdown button text (More/Less Options)
            button_text = dropdown_button.innerText;
            //If "More Options" is clicked and small_screen_search_fields element exists and the dropdown list is expanded -> destroy small_screen_search_fields
            if(document.getElementById("small_screen_search_fields") != null && search_fields_dropdown_state) {
                small_display_search_fields_parent_element.removeChild(small_display_search_fields);
            }
            //If small_screen_search_fields doesn't exist and the user clicked "Less Options" button to collapse the search fields -> recreate it again
            else if(document.getElementById("small_screen_search_fields") == null ){
                //Insert exactly after main search fields to override the empty GET JSON string values (host and client name)
                small_display_search_fields_parent_element.insertBefore(small_display_search_fields, dropdown_button_bar)
            }
            
            //Handles the dropdown button text depending on the current state of the button 
            if(button_text == "More Options")
                dropdown_button.innerText = "Less Options"
            else
                dropdown_button.innerText = "More Options"
        });  
        //If the window is resized(usually on orientation change)
        window.addEventListener("resize", () =>{
            vw = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
            button_text = dropdown_button.innerText;
            //On large (1024+) viewports the dropdown bar gets auto-collapsed, therefore search_fields_dropdown_state should be false (collapsed state)
            if(vw >= 1024)
                search_fields_dropdown_state = false
            //If main search fields are hidden = they are collapsed, therefore search_fields_dropdown_state should be false, otherwise the dropdown is expanded
            //and search_fields_dropdown_state is true. Handles rare cases when the viewport is resized through certain breakpoints and small_screen_search_fields
            //don't get recreated.
            if(getComputedStyle(search_fields).display == "none")
                search_fields_dropdown_state = false
            else
                search_fields_dropdown_state = true
            //If small_screen_search_fields and screen is LARGE+ -> destroy it
            if(document.getElementById("small_screen_search_fields") != null && vw >= 1024) {

                small_display_search_fields_parent_element.removeChild(small_display_search_fields);
            }
            //If small_screen_search_fields does not exist, viewport is < LARGE and the dropdown list is not expanded
            else if(document.getElementById("small_screen_search_fields") == null && vw < 1024 && !search_fields_dropdown_state){
                small_display_search_fields_parent_element.insertBefore(small_display_search_fields, dropdown_button_bar)
            }
            //resets the dropdown button text to avoid "Less Options" text on a collapsed menu on resize
            dropdown_button.innerText = "More Options"
        })
    }

    set_search_fields();
})