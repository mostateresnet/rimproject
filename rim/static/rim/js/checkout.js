$(document).ready(function() {
    function switch_forms(){
        var $client_names = $('#client_names');
        var content = $client_names.val();
        if ($('input[name=checkform]:checked').prop('id') == 'checkin') {
            if (content != 'ResNet')
                $client_names.data('content', content).prop('disabled', true).val('ResNet');
        }
        else {
            $client_names.prop('disabled', false).val($client_names.data('content'));
        }
    }

    $('input[name=checkform]').on('click change', switch_forms);

});
