$(document).ready(function() {
    
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
    $(document).foundation();
});
