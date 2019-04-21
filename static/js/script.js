window.addEventListener("DOMContentLoaded", function() {
	let boxes = document.querySelectorAll(".room");

	Array.from(boxes, function(box) {
		box.addEventListener("click", function() {
			var state = this.getAttribute('data-state');
			var room = this.classList[1];
			var URL = 'http://192.168.1.188:5000/' + room;

			if (state === "off") {
				this.style.backgroundColor = "#ddd";
				this.setAttribute('data-state', 'on');
			} else {
				this.style.backgroundColor = "#444";
				this.setAttribute('data-state', 'off');
			}

			$.ajax({
				url: URL,
				type: "GET",
				success: function(result) {
					console.log(result)
				},
				error: function(error) {
					console.log('Error ${error}')
				}
			})

    		});
  	});
});
