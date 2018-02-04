$(function () {

  var loadForm = function () {
    var btn = $(this); 
    $.ajax({
      url: btn.attr('data-url'),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $('#modal-client').modal('show');
      },
      success: function (data) {
        $('#modal-client .modal-content').html(data.html_form);
      }
    });
  };

  var makeHttp = function() {
    var form = $(this);
    $.ajax({
      url: form.attr('action'),
      data: form.serialize(),
      type: form.attr('method'),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#project-table tbody").html(data.html_client_list);
          $("#modal-client").modal("hide");
        }
        else {
          $('#modal-project .modal-content').html(data.html_form);
        }
      }
    });
    return false;
  }

  $('.js-create-client').click(loadForm);
  $('#modal-client').on('submit', '.js-client-create-form', makeHttp);

  $("#client-table").on("click", ".js-update-client", loadForm);
  $("#modal-client").on("submit", ".js-client-update-form", makeHttp);

  // $("#client-table").on("click", ".js-delete-client", loadForm);
  // $("#modal-client").on("submit", ".js-client-delete-form", makeHttp);
  
});