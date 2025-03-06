$(document).ready(function () {
	
  $("#formID").validationEngine();
  $("#formID").submit(function (event) {
	  event.preventDefault();
	  $("#formID").find('.errors').remove();
	  if ($("#formID").validationEngine('validate') == true) {
		  
		$("#formID").find('button').text('Wysyłanie...').attr('disabled',true);
		
		var datastring = $("#formID").serialize();
		//console.log(datastring);
		jQuery.post("process.py",
			datastring,
			function (data) {
				if (data.status == true) {
					$("#formID").replaceWith(data.content);
					window.location.hash = '#contact';
				} else {
					$("#formID").find('button').text('Wyślij').attr('disabled',false);	
					var txt = '<ul class="list-unstyled errors">';
					for (var i in data.error) {
						txt = txt + '<p>' + data.error[i] + '</p>';
					}
					txt = txt + '</ul>';
					$("#formID").prepend(txt);
				}
			},
			'json'
		)
		.fail(function () {
			var txt = '<ul class="list-unstyled errors"><li>Nie można wykonać polecenia :-(</li></ul>';
				$("#formID").prepend(txt);
		});		  
	  }
  });
});