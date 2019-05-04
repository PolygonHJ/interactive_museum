window.addEventListener("DOMContentLoaded", function() {
    let boxes = document.querySelectorAll(".room");
    
    Array.from(boxes, function(box) {
	box.addEventListener("click", function() {
	    var state = this.getAttribute('data-state');
	    var room = this.classList[1];
	    var URL = 'http://192.168.0.29:5000/' + room;
	    
	    if (state === "off") {
		this.style.backgroundColor = "#ddd";
		this.setAttribute('data-state', 'on');
	    } else {
		this.style.backgroundColor = "#444";
		this.setAttribute('data-state', 'off');
	    }
	    
	    console.log(room);
	    
	    $.ajax({
		url: URL,
		success: function(result) {
		    console.log(result)
		},
		error: function(error) {
		    console.log('Error ${error}')
		}
	    })
	    
    	});
    });

    let paths = document.querySelectorAll(".path");
    
    Array.from(paths, function(box) {
	box.addEventListener("click", function() {
	    var URL = 'http://192.168.0.29:5000/path';
	    console.log(URL);
	    
	    $.ajax({
		url: URL,
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
