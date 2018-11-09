$(document).ready(function() {
    function switch_forms(){
        var client_names = $('.client input[type=text]');
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

    $('.barcode').on('keyup', 'input[type=text]', function() {
        var last_barcode = $('.barcode input[type=text]').last();
        if(last_barcode.val() != ""){
            $('.copyable').each(function(){
                var last_element = $(this).find('input[type=text]').last();
                var clone = last_element.clone();
                if(!(last_element.prop('disabled'))) {
                    clone.val("");
                }
                clone.toggleClass('focused', false);
                last_element.after(clone);
            })
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

});
