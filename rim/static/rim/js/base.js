$(document).ready(function() {
    $(document).foundation();
    function set_page_cookie(per_page) {
        var expire_date = new Date();
        //Sets the expire_date to be a year from now
        expire_date.setTime(expire_date.getTime() + (365*24*60*60*1000))
        document.cookie = "paginate=" + per_page +";expires=" + expire_date.toUTCString() +";path=/";
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

    var timer;
    $('#id_serial_no').on('input', function(e) {
        clearTimeout(timer)
        timer = setTimeout(check_serial_nums, 300);
    })

    function check_serial_nums() {
        var existing_serial_nums = [];
        $('#serial_no_errors').remove()
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
        $.ajax({
            url: "/check_serial_nums/",
            data: {'serial_nums': JSON.stringify($('#id_serial_no').val().trim().split('\n'))},
            type: 'POST',
            success: function(data) {
                existing_serial_nums = data['context'];
                if (existing_serial_nums.length != 0) {
                    add_errors(existing_serial_nums);
                }
            }
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

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

});
