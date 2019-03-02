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

$(document).ready(function() {
    function switch_forms(){
        var client_names = $('.client input[type=text]');
        client_names.keyup();
        if ($('input[name=checkform]:checked').prop('id') == 'checkin') {
            client_names.each(function() {
                var content = $(this).val();
                if (content != 'ResNet')
                    $(this).data('content', content).prop('disabled', true).val('ResNet');
            })
        }
        else {
            client_names.each(function(){
                $(this).prop('disabled', false).val($(this).data('content'));
            })
        }
    }

    $('input[name=checkform]').on('click change', switch_forms);
    //Take all of the copyable columns (Client, Building, Room) and find
    function insert_row() {
        $('.copyable').each(function(){
            var last_element = $(this).find('.input_container').last();
            var clone = last_element.clone();
            var input_element = clone.find('input[type=text]');
            if($(this).closest('.client').length == 0){
                input_element.prop('disabled', false);
            }
            if(!(input_element.prop('disabled'))) {
                input_element.val("");
            }
            input_element.toggleClass('focused', false);
            last_element.after(clone);
        })
    }

    $('.barcode, .client').on('keyup', 'input[type=text]', function() {
        var last_barcode = $('.barcode input[type=text]').last();
        var second_to_last_barcode = $('.barcode input[type=text]').eq(-2);
        var last_client = $('.client input[type=text]').last();
        var second_to_last_client = $('.client input[type=text]').eq(-2);
        if (last_barcode.val() == "" && second_to_last_barcode.val() == "" && last_client.val() == "" && second_to_last_client.val() == "" ) {
            var row_index = $(this).closest('.copyable').find('.delete').index(this);
            $('.copyable').each(function(){
                $(this).find('.input_container').eq(row_index).remove();
            })
        }
        if (last_barcode.val() != '') {
            insert_row();
        }
    })

    $('.copyable').on('focus', 'input[type=text]', function(){
        var row_index = $(this).closest('.copyable').find('input[type=text]').index(this);
        $('.copyable').each(function(){
            $(this).find('input[type=text]').eq(row_index).toggleClass('focused', true);
        })
    })
    $('.copyable').on('blur', 'input[type=text]', function(){
        var row_index = $(this).closest('.copyable').find('input[type=text]').index(this);
        $('.copyable').each(function(){
            $(this).find('input[type=text]').eq(row_index).toggleClass('focused', false);
        })
    })

    var RMS_LOOKUP_TIMER;
    $('.client').on('keyup', 'input[type=text]', function() {
        $(this).toggleClass('queried', false); // make sure this gets checked against RMS again

        // don't try to look anything up until 300ms after the user is done typing/pasting
        clearTimeout(RMS_LOOKUP_TIMER);
        RMS_LOOKUP_TIMER = setTimeout(rms_location, 300);

        var current_name = $(this).val();
        var regex = /^[mM8]\d{8}$/;
        var row_index = $(this).closest('.copyable').find('input[type=text]').index(this);
        var last_client = $('.client input[type=text]').last();
        if(regex.test(current_name)){
            $('.location').each(function(){
                $(this).find('input[type=text]').eq(row_index).prop('disabled', true);
            })
        } else {
            $('.location').each(function(){
                $(this).find('input[type=text]').eq(row_index).prop('disabled', false);
            })
        }

        if(last_client.val() != ""){
            if($('#client_paste').prop('checked')) {
                input = $(this).val();
                split_input = input.split(" ");
                $(this).val('');
                for(i = 0; i < split_input.length; i++) {
                    $('.client input[type=text]').eq(-1).val(split_input[i]);
                    $('.location').each(function() {
                        $(this).find('input[type=text]').eq(-1).prop('disabled', true);
                    })
                    insert_row();
                }
            } else {
                insert_row();
            }
        }
    })

    $('.room').on('click', '.delete', function() {
        var row_index = $(this).closest('.copyable').find('.delete').index(this);
        if ($('.barcode input[type=text]').length == 1){
            insert_row();
        }
        $('.copyable').each(function(){
            $(this).find('.input_container').eq(row_index).remove();
        })
    })
});
