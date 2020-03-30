$(document).ready(function() {

    

    var timer;
    $('#id_serial_no').on('input', function(e) {
        clearTimeout(timer)
        timer = setTimeout(check_serial_nums, 300);
    })

    function check_serial_nums() {
        var existing_serial_nums = [];
        $('#serial_no_errors').remove()
        $.ajax({
            url: SERIAL_NUM_CHECK_URL,
            data: {'serial_nums': JSON.stringify($('#id_serial_no').val().trim().split('\n'))},
            type: 'POST',
            success: function(data) {
                $('.button').prop('disabled', false);
                errors = data['context'];
                if (errors.length != 0) {
                    $('.button').prop('disabled', true);
                    add_errors(errors);
                }
            }
        });
    }

    function add_errors(errors) {
        var errorListElement = makeErrorList(errors);
        errorListElement.classList.add('errorlist')
        input = document.getElementById('id_serial_no');
        
        input.parentElement.insertBefore(errorListElement, input);
    }

    function makeErrorList(errors) {
        var list = document.createElement('ul');
    
        for (var i = 0; i < errors.length; i++) {
            var item = document.createElement('li');
            item.appendChild(document.createTextNode(errors[i]));
            list.appendChild(item);
        }
        list.classList.add('errorlist')
        list.setAttribute('id', 'serial_no_errors')
        return list;
    }
})