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

    $('#modal-project').on('submit', '.js-project-create-form', function () {
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#project-table tbody").html(data.html_project_list);
                    $("#modal-project").modal("hide");
                }
                else {
                    $('#modal-project .modal-content').html(data.html_form);
                }
            }
        });
        return false;
    });
  
  });