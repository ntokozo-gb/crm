$('document').ready(function(){
    $('#btn-add-client').click(function() {
        var name = $('#client_name').val();
        var person = $('#contact_person').val();
        var number = $('#contact_number').val();
        var projects = $('#client_projects').val();
        var data = {
            'name': name,
            'contact_person': person,
            'contact_number': number,
            'projects': projects,
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

    $('#btn-add-project').click(function() {
        var name = $('#project_name').val();
        var status = $('#project_status').val();
        var data = {
            'name': name,
            'status': status,
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        };

        $.ajax({
            url: '/add_project/',
            method: 'POST',
            data: data,
            async: false,
            success: function(resp){
                window.location = '/projects/';
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
