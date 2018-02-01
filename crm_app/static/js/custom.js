$('document').ready(function(){
    $('#btn-add-client').click(function(){
        var cname = $('#client_name').val();
        var cpers = $('#contact_person').val();
        var cnum = $('#contact_number').val();
        var data = {
            'client_name': cname,
            'contact_person': cpers,
            'contact_number': cnum,
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        };

        $.ajax({
            url: '/add_client/',
            method: 'POST',
            data: data,
            async: false,
            success: function(resp){
                window.location = '/clients/';
            }
        });
    });


     function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});
