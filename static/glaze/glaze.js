
/*** Start Activate Glaze  ****************************************************/

  function redirectGlaze(redirect_url) {
    if (redirect_url != undefined) {
      document.location = redirect_url;
    }
  }


  function renderGlaze(aGlazeUrl) {
    // Inject the desired content into the glaze bootstrap modal
    $("#id-modal-content").html("").load(aGlazeUrl);
    $("#glaze").modal("show");
  }


  function resetGlaze() {
    // Remove the session variable held on server
    $.ajax({
      type: "GET",
      url: $("#id-glaze-url").attr("glaze-reset"),
    });
    // Remove div handling instances where a request has been made to the session
    $("#id-glaze-url").remove();
  }


  $(document).ready(function() {
    // Load glaze if requested of the session
    var glazeUrl = $("#id-glaze-url").attr("glaze-url");
    if (glazeUrl != undefined) {
      renderGlaze(glazeUrl);
      resetGlaze();
    };
  })

/*** End Activate Glaze  ******************************************************/

/*** Start Glaze Form *********************************************************/

  function glazeSubmitForm(anInputButton) {
    var button = $(anInputButton);
    var glaze_form = button.closest("form");
    glaze_form.on("submit", function(e) {
      // Generate AJAX response
      $.ajax({
        type: glaze_form.attr("method"),
        url: glaze_form.attr("action"),
        data: serializeGlazeForm(glaze_form),
        dataType: "json",
        success: function (data) {
          if (data.is_glaze) {
            if (data.success_url == undefined) {
              $("#id-modal-content").html(data.glaze_html);
            } else {
              renderGlaze(data.success_url);
            }
          } else {
            document.location = data.success_url;
          }
        },
      });
      return false;
    });
  };


  function serializeGlazeForm(form) {
    var serialized_data = $(form).serializeArray();
    return $.param(serialized_data)
  }

/*** End Glaze Form ***********************************************************/
