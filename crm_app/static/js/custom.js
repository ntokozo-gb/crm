$('document').ready(() => {

    $('#btn-add-client').click(() => {
        var name = $('#client_name').val();
        var person = $('#contact_person').val();
        var number = $('#contact_number').val();
        var client_data = {
            'name': name,
            'contact_person': person,
            'contact_number': number,
            'csrfmiddlewaretoken': getCookie('csrftoken'),
        };

        $.ajax({
            url: '/add_client/',
            method: 'POST',
            data: client_data,
            async: false,
            success: function(resp){
                window.location = '/clients/';
            }
        });
    });

    $('#btn-add-project').click(() => {
      var name = $('#project_name').val();
      var status = $('#project_status').val();
      var client_id = $('#client').val();
      var project_data = {
          'name': name,
          'status': status,
          'assigned_to': client_id,
          'csrfmiddlewaretoken': getCookie('csrftoken'),
      };

      $.ajax({
          url: '/add_project/',
          method: 'POST',
          data: project_data,
          async: false,
          success: function(resp){
              window.location = '/projects/';
          }
      });
    });

    $('#client-table tbody').on('click', 'tr', function() {
      var id = $(this)[0].attributes[0].value;
      var data = {
        'id': id,
        'csrfmiddlewaretoken': getCookie('csrftoken'),
      };
      var client;

      $.ajax({
        type: "GET",
        url: '/edit_client/',
        data: data,
        async: false,
        success: (data) => {
          client = data;
        }
      });
    });

    // $('#project-table tbody').on('click', 'tr', function() {
    //   var id = $(this)[0].attributes[0].value;
    //   var data = {
    //     'id': id,
    //     'csrfmiddlewaretoken': getCookie('csrftoken'),
    //   };
    //   var client;

    //   $.ajax({
    //     type: "GET",
    //     url: '/edit_project/',
    //     data: data,
    //     dataType: 'json',
    //     success: (response) => {
    //       client = response;
    //     }
    //   });
    // });

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
