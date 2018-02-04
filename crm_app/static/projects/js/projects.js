$(function () {
    $('.js-create-project').click(function () {
      $.ajax({
        url: '/projects/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $('#modal-project').modal('show');
        },
        success: function (data) {
          $('#modal-project .modal-content').html(data.html_form);
        }
      });
    });
  
  });