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

    $('.copyable').on('keyup', 'textarea[type=text]', function() {
        var values = {};

        $(this).closest('.copyable').find('textarea[type=text]').each(function() {
            var current_val = $(this).val().toLowerCase();
            if(current_val in values && current_val != "") {
                values[current_val]++;
            } else {
                values[current_val] = 1;
            }
        })

        $(this).closest('.copyable').find('textarea[type=text]').each(function() {
            var current_val = $(this).val().toLowerCase();
            if(values[current_val] > 1) {
                $(this).toggleClass("duplicate", true);
            } else {
                $(this).toggleClass("duplicate", false);
            }
        })
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
        })
    })


    // Function which detects when the [tab] or [tab+shift] button is clicked within a textarea.
    $('.client , .barcode , .building , .room').on('keydown', 'textarea[type=text]', function(e) {

        var code = e.keyCode || e.which;

        // If enter button is pressed.
        if (code == 13 ){
            e.preventDefault();

            // Determine row index of the current textarea
            var row_index = $(e.target).closest('.copyable').find('.textarea').index(e.target);

            //  Find the following row below 
            var next_row = $(e.target).closest('.copyable').find('textarea[type=text]').eq(row_index+1)[0];
    
            
            // If the row is empty, then go to submit button.
            if (typeof next_row === 'undefined'){
                $('#btn_submit').focus();
            }

            // Change focus to the last item
            $(next_row).focus(); 
             
        }


        // If [shift-tab] is pressed. 
        if (e.shiftKey && code == 9) { 
            // Prevent the default tabbing action.
            e.preventDefault();

            // Get the current class of the textarea
            var current_class = $(this).closest('.copyable');
          
            // Determine row index of the current textarea
            var row_index = $(this).closest('.copyable').find('.textarea').index(this);
  
            // The first textarea on the current row.
            var first_textarea = $('.client textarea[type=text]');
            
            // The first textarea on the first row & first column. 
            var first_row_textarea = $('.client textarea[type=text]').first();

            // Find prev textarea in the same row
            var prev_textarea = current_class.prev().find('.textarea').eq(row_index);
       
            //If at first row and first textarea, change to default tabbing.
            if ($(this).is(first_row_textarea)){
                return true;
             
            }
            //Else, Check if at first column / first textarea to wrap around to prev row
            else{
                if ($(this).is(first_textarea)){
                    var prev_textarea = $('.room textarea[type=text]')[row_index -1];
                }
                          
                // Change focus to previous textarea 
                $(prev_textarea).focus();
            }

        }

        else{

            // If [tab] is pressed.
            if (code == '9'){

                // Prevent the default tabbing action.
                e.preventDefault();

                // Get the current class of the textarea
                var current_class = $(this).closest('.copyable');
                
                // Determine row index of the current textarea
                var row_index = $(this).closest('.copyable').find('.textarea').index(this);
                // The final textarea on the current row
                var last_col = $('.room textarea[type=text]');
                // The final textarea on the last row & last column. 
                var last_room = $('.room textarea[type=text]').last();
                
                // Find next textarea in the same row
                var next_textarea = current_class.nextAll().find('.textarea')[row_index];

               // If at last row and last textarea, tab will move to submit button.
               if ($(this).is(last_room)){
                    $('#btn_submit').focus();
                 
               }
                // Else, Check if at last column / textarea to wrap around to next row
               else{
                if ($(this).is(last_col)){
                    
                    // Get the class of the textarea in next row
                    current_class = $(this).closest('.copyable').parent().children();
                    next_textarea = current_class.find('.textarea')[row_index + 1];
                }
                          
                // Change focus to next textarea 
                $(next_textarea).focus();

               }

            }


        }

        

    })


    // Function which separates pasted input into separate rows.
    $('.client , .barcode , .building , .room').on('input', 'textarea[type=text]', function(e) {


        // Get input from textarea
        var input = $(e.target).val();

        //Check if input has whitespace
        var has_space = hasWhiteSpace(input);

        if (has_space) {
            // Split the textarea string on newline / linebreak.
            var split_input = input.split(/\r\n|\n|\r/);
           
            // Determine row index of the current textarea
            var row_index = $(e.target).closest('.copyable').find('.textarea').index(e.target);
            //var last_row_index = row_index + (split_input.length - 1);
              
            // For each value, which isn't an empty string.              
            for(i = 0; i < split_input.length; i++) {
                if (split_input[i] != ""){

                        //  Find the following row below 
                        var next_row = $('.client textarea[type=text]').eq(row_index+1)[0];
                        
                        // If the row does not exist or is undefined, then insert a new row.
                        if (typeof next_row === 'undefined'){
                            insert_row();
                        }

                        // Paste input into the textareas of the column.
                        $(e.target).closest('.copyable').find('textarea').eq(row_index).val(split_input[i]);
                        // Change focus to the last item
                        $(e.target).closest('.copyable').find('textarea').eq(row_index).focus();


                        // Increment to the next row
                        row_index+=1;
                }   
            }  
        }

    })

});
