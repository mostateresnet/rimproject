$(document).ready(function() {
    $(document).foundation();
    function set_page_cookie(per_page) {
        var expire_date = new Date();
        //Sets the expire_date to be a year from now
        expire_date.setTime(expire_date.getTime() + (365*24*60*60*1000))
        document.cookie = "paginate=" + per_page +";expires=" + expire_date.toUTCString() +";path=/";
        window.location.reload();
    }

    $('#page_submit').click(function() {
        set_page_cookie($('#page_input').val());
    })
});
