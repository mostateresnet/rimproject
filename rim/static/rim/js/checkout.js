function rms_location(){
    // gather the value from every client input that hasn't already been queried
    var queries = [];
    var queried_rows = [];
    $('.client input[type=text]').each(function(index) {
        var $this = $(this);
        if ($this.is('.queried')) {
            return;
        }

        $this.toggleClass('queried', true);
        queries.push($this.val());
        queried_rows.push(index);
    });

    $.post(
        window.location.href.split('?')[0],
        {
            queries: queries,
            queried_rows: queried_rows,
        },
        function(response) {
            for (var row in response) {
                $('.building input[type=text]').eq(row).val(response[row][1]);
                $('.room input[type=text]').eq(row).val(response[row][2]);
            }
        }
    );
}

function hasWhiteSpace(s) {
  return /\s/g.test(s);
}

$(document).ready(function() {
    var localStorage = window.localStorage;
    restoreData();
      
    function switch_forms(){
        var client_names = $('.client textarea[type=text]');
        if ($('input[name=checkform]:checked').prop('id') == 'checkin') {
            client_names.each(function() {
                var content = $(this).val();
                if (content != 'ResNet')
                    $(this).data('content', content).prop('disabled', true).val('ResNet');
            })
            $('.location textarea').each(function() {
                $(this).prop('disabled', false);
            })
        }
        else {
            client_names.each(function(){
                $(this).prop('disabled', false).val($(this).data('content'));
            })
            var value = $(this).val();
            if(value != '') {
                client_names.keyup();
            }
        }
    }

    $('input[name=checkform]').on('click change', switch_forms);
    //Take all of the copyable columns (Client, Building, Room) and find
    function insert_row() {
        $('.copyable').each(function(){
            var last_element = $(this).find('.input_container').last();
            var clone = last_element.clone();
            var input_element = clone.find('textarea[type=text]');
            if($(this).closest('.client').length == 0){
                input_element.prop('disabled', false);
            }
            if(!(input_element.prop('disabled'))) {
                input_element.val("");
            }
            input_element.toggleClass('focused', false);
            input_element.toggleClass('duplicate', false);
            last_element.after(clone);
        })
    }


    $('.copyable').on('keyup', 'textarea[type=text]', function(e) {  
        findDuplicates(e);

    })

    $('.copyable').on('keyup', 'textarea[type=text]', function() {
        var add_row = false;
        var remove_row = true;
        $('.copyable').each(function() {
            var last_element = $(this).find('textarea').last();
            var second_to_last_element = $(this).find('textarea').eq(-2);

            if(last_element.val() != '' || second_to_last_element.val() != '') {
                remove_row = false;
                if(last_element.val() != '' && !last_element.prop('disabled')) {
                    insert_row();
                }
            }
        })

        if(remove_row) {
            var row_index = $(this).closest('.copyable').find('.delete').index(this);
            $('.copyable').each(function(){
                $(this).find('.input_container').eq(row_index).remove();
            })
        }
    })



    $('.copyable').on('focus', 'textarea[type=text]', function(){
        var row_index = $(this).closest('.copyable').find('textarea[type=text]').index(this);
        $('.copyable').each(function(){
            $(this).find('textarea[type=text]').eq(row_index).toggleClass('focused', true);
        })
    })
    $('.copyable').on('blur', 'textarea[type=text]', function(){
        var row_index = $(this).closest('.copyable').find('textarea[type=text]').index(this);
        $('.copyable').each(function(){
            $(this).find('textarea[type=text]').eq(row_index).toggleClass('focused', false);
        })
    })

    var RMS_LOOKUP_TIMER;
    $('.client').on('keyup', 'textarea[type=text]', function() {
        $(this).toggleClass('queried', false); // make sure this gets checked against RMS again

        // don't try to look anything up until 300ms after the user is done typing/pasting
        clearTimeout(RMS_LOOKUP_TIMER);
        RMS_LOOKUP_TIMER = setTimeout(rms_location, 300);

        var current_name = $(this).val();
        var regex = /^[mM8]\d{8}$/;
        var row_index = $(this).closest('.copyable').find('textarea[type=text]').index(this);
        var last_client = $('.client textarea[type=text]').last();
        if(regex.test(current_name)){
            $('.location').each(function(){
                $(this).find('textarea[type=text]').eq(row_index).prop('disabled', true);
            })
           
        } else {
            $('.location').each(function(){
                $(this).find('textarea[type=text]').eq(row_index).prop('disabled', false);
            })
        }
    })

    $('.room').on('click', '.delete', function() {
        var row_index = $(this).closest('.copyable').find('.delete').index(this);
        if ($('.barcode textarea[type=text]').length == 1){
            insert_row();
        }
        $('.copyable').each(function(){
            $(this).find('.input_container').eq(row_index).remove();
            id = 'checkout_'+ $(this).closest('.copyable').attr('id') + '_'+row_index;
            localStorage.removeItem(id);
            
        })
        updateStorage();
 
    })


   // Function which detects when the [enter], [tab] or [tab+shift] button is clicked within a textarea.
    $('.client , .barcode , .building , .room').on('keydown', 'textarea[type=text]', function(e) {

        var code = e.keyCode || e.which;

        // If [enter] is pressed.
        if (code == 13 ){
            enterAction(e);
        }

        // If [shift-tab] is pressed. 
        if (e.shiftKey && code == 9) { 
            shiftTabAction(e);
        }

        else{
            // If [tab] is pressed.
            if (code == '9'){
                tabAction(e);
            }
        }
    })


    // Function which separates pasted input into separate rows.
    $('.client , .barcode , .building , .room').on('input', 'textarea[type=text]', function(e) {
        pasteInput(e);
    })

    // Autosave data into local storage.
    $('.copyable').on('blur', 'textarea[type=text]', function(){
        updateStorage();
    })

    // Function to reset the checkout form.
    $('#btn_reset').on('click', function(){
        // Reset each textarea.
        $('.copyable').find('.textarea').each(function(){
            $(this).val('');
        })
        localStorage.clear();
        location.reload();
    })


    function findDuplicates(e){
        var values = {};

        $(e.target).closest('.copyable').find('textarea[type=text]').each(function() {
            var current_val = $(this).val().toLowerCase();
            if(current_val in values && current_val != "") {
                values[current_val]++;
            } else {
                values[current_val] = 1;
            }
        })

        $(e.target).closest('.copyable').find('textarea[type=text]').each(function() {
            var current_val = $(this).val().toLowerCase();
            if(values[current_val] > 1) {
                $(this).toggleClass("duplicate", true);
            } else {
                $(this).toggleClass("duplicate", false);
            }
        })
    }

    function restoreData(){
        
        var row_count = 0;
        // Determine how many rows are needed.
        do{
            var id = 'checkout_'+ $('#client').attr('id') + '_'+row_count;
            var text = localStorage.getItem(id);
            var next_row = $('.client textarea[type=text]').eq(row_count+1);

            // If data exists and row does not exist, insert new row.
            if ((text != null && next_row.length == 0)){
                insert_row();
            }
            row_count  ++;
        }
        while(text != null);

        // Fill the rows with data from localStorage. 
        $('.copyable').each(function(){
            row_index = 0;

            var text_area = $(this).find('textarea[type=text]').eq(row_index);
            var text_area_all = $(this).find('textarea[type=text]');

            $(text_area_all).each(function(){
                row_index = $(this).closest('.copyable').find('textarea[type=text]').index(this);
                var current_class = $(text_area).closest('.copyable').attr('id');
                var id = 'checkout_'+ current_class+ '_'+row_index;
                var text = localStorage.getItem(id);
                $(this).val(text);

            })

            // Detect duplicates in restored data
            var col_textarea = {target:text_area};
            findDuplicates(col_textarea);

        })     
    }

    // Function which updates the local storage for all textareas.
    function updateStorage(){

        // Clear the old values for new values
        localStorage.clear();

        // var last_element = $('.room textarea[type=text]').last();
        var last_element = $('.copyable textarea[type=text]').last();
        var last_element_index = $(last_element).closest('.copyable').find('textarea[type=text]').index(last_element);
        var row_index = 0;
        var save_index = 0;

        // While not the last line
        while (row_index <= last_element_index){
            
            empty_flag = true;      // Set a flag for each row. Assume row is empty.

              $('.copyable').each(function(){
                    
                    var text_area = $(this).find('textarea[type=text]').eq(row_index);
                    var current_class = $(text_area).closest('.copyable').attr('id');
                    var id = 'checkout_'+ current_class + '_'+save_index;
                    var last_textarea = $('#room').find('textarea[type=text]').eq(row_index);
                    var text = $(text_area).val();
                

                    // If currently on the check-in form
                    if ($('input[name=checkform]:checked').prop('id') == 'checkin' && text == 'ResNet') {
                        var client_names = $('.client textarea[type=text]').eq(row_index);
                        text = $(client_names).data('content');
                    }

                    // If there is an valid value in the row, row is not empty.
                    if (text != ""){
                        empty_flag = false;
                    }

                    // If at last textarea in the row 
                    if (text_area.is(last_textarea)){

                          // If row is empty. Then remove the values from localStorage. 
                        if (empty_flag == true){
        
                            $('.copyable').each(function(){
                                id = 'checkout_'+ $(this).closest('.copyable').attr('id') + '_'+save_index;
                                localStorage.removeItem(id);
                            })
                            // Move to next row
                            row_index++;
                            }

                        // Else there is data in previous textareas, continue; 
                        else{
                            localStorage.setItem(id, text);
                            row_index++;
                            save_index++;
                        }
                    }
                
                    // Else, still current row, do not increment counter. 
                    else{
                        localStorage.setItem(id, text);
                    }
                })
        }
    }

    function pasteInput(e){

            var input = $(e.target).val();              // Get input from textarea           
            var has_space = hasWhiteSpace(input);       //Check if input has whitespace

            if (has_space) {
                
                var split_input = input.split(/\r\n|\n|\r/);                                        // Split the textarea string on newline / linebreak.
                var row_index = $(e.target).closest('.copyable').find('.textarea').index(e.target); // Determine row index of the current textarea
                            
                for(i = 0; i < split_input.length; i++) {                                           // For each value, which isn't an empty string.  
                    if (split_input[i] != ""){
                            
                            var next_row = $('.copyable').first().find('.textarea').eq(row_index+1)[0]; 
                  
                            if (typeof next_row === 'undefined'){               // If the row does not exist or is undefined, then insert a new row.
                                insert_row();
                            }
                            // Paste input into the textareas of the column.
                            $(e.target).closest('.copyable').find('textarea').eq(row_index).val(split_input[i]);                           
                            $(e.target).closest('.copyable').find('textarea').eq(row_index).focus(); // Change focus to the last item
                            row_index+=1; // Increment to the next row
                    }   
                }  
            }
        }


    // Function for moving to the textarea below once enter is clicked. 
    function enterAction(e){
        e.preventDefault();

        // Determine row index of the current textarea
        var row_index = $(e.target).closest('.copyable').find('.textarea').index(e.target);
        row_index +=1;

        //  Find the following row below 
        var next_row = $(e.target).closest('.copyable').find('textarea[type=text]').eq(row_index);

        var is_disabled = next_row.prop('disabled');
        while (is_disabled){
            row_index +=1;
            next_row = $(e.target).closest('.copyable').find('textarea[type=text]').eq(row_index);
            is_disabled = next_row.prop('disabled');
        }

        // Change focus to next row.
        $(next_row).focus();   
        
        // If the row is empty, then go to submit button.
        if (next_row.length == 0){
            $('#btn_submit').focus();
        }
    }

    // Function for shift tabbing to previous textareas.
    function shiftTabAction(e){
        
        e.preventDefault();                                     // Prevent the default tabbing action.
        var current_class = $(e.target).closest('.copyable');   // Get the current class of the textarea
        var row_index = $(e.target).closest('.copyable').find('.textarea').index(e.target); // Determine row index of the current textarea
        var first_textarea = $('.client textarea[type=text]');                      // The first textarea on the current row.
        var first_row_textarea = $('.client textarea[type=text]').first();          // The first textarea on the first row & first column. 
        var prev_textarea = current_class.prev().find('.textarea').eq(row_index);   // Find prev textarea in the same row
        var is_disabled = prev_textarea.prop('disabled');
      
        //If at first row and first textarea, change to default tabbing.
        if ($(e.target).is(first_row_textarea)){
            return true;   
        }
        //Else, Check if at first column / first textarea to wrap around to prev row
        else{     
            
            if ($(e.target).is(first_textarea)){
                row_index = row_index -1;
                prev_textarea = $('.room textarea[type=text]').eq(row_index);
                is_disabled = prev_textarea.prop('disabled');        
            }
        }

        // Check if prev textarea is disabled.
        while (is_disabled){
            // Check if prev textarea is the first element in the row & is disabled.
            // If first element, move to previous row.
            if ($(prev_textarea).is(first_textarea) && (prev_textarea.prop('disabled'))){
                current_class = $(e.target).closest('.copyable').parent().children();
                row_index = row_index -1;
                prev_textarea = $('.room textarea[type=text]').eq(row_index);
            }
            else{ 
                current_class = $(prev_textarea).closest('.copyable');                  // Get the class of the prev textarea
                prev_textarea = current_class.prev().find('.textarea').eq(row_index);   // Find prev textarea element.
            }

            //Check if prev element is disabled
            is_disabled = prev_textarea.prop('disabled');                 
        }
        // Change focus to previous textarea 
        $(prev_textarea).focus();
    }


    // Function for horizontal tabbing. 
        function tabAction(e){
        
            e.preventDefault();                                                 // Prevent the default tabbing action.
            var current_class = $(e.target).closest('.copyable');               // Get the current class of the textarea
            var row_index = $(e.target).closest('.copyable').find('.textarea').index(e.target);

            var last_col = $('.copyable').last().find('.textarea');                     // The last textarea on the current row
            var last_room = $(last_col).last();                                         // The final textarea on the last row & last column.
    
            var next_textarea = current_class.next().find('.textarea').eq(row_index); // Find next textarea in the same row
            var is_disabled = next_textarea.prop('disabled');                       // Check if next textarea is disabled.

            // If textarea element is the last on the row.
            if ($(e.target).is(last_col)){ 
                    // Get the class of the textarea in next row
                    current_class = $(e.target).closest('.copyable').parent().children();
                    row_index = row_index +1;
                    next_textarea = current_class.find('.textarea').eq(row_index);
                    is_disabled = next_textarea.prop('disabled');
            }
            // If textarea disabled. 
            while (is_disabled){
                // Check if next textarea is the last element in the row & is disabled.
                // If last element, move to next row.
                if ($(next_textarea).is(last_col) && (next_textarea.prop('disabled'))){

                    current_class = $(e.target).closest('.copyable').parent().children();
                    row_index = row_index +1;
                    next_textarea = current_class.find('.textarea:not([disabled])').eq(row_index);
                }
                else{
                    current_class = $(next_textarea).closest('.copyable').next();   // Get the class of the next textarea
                    next_textarea = current_class.find('.textarea').eq(row_index);  // Find next textarea element.
                }
                is_disabled = next_textarea.prop('disabled');                       // Check if next element is disabled              
            }
            $(next_textarea).focus();                                               // Switch to next available element.

           // If at last row and last textarea, tab will move to submit button.
           if ($(e.target).is(last_room)){
                $('#btn_submit').focus();
           }
        }

});
